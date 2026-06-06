import os
import asyncio
from google.adk import Runner
from google.adk.agents import LlmAgent
from google.adk.sessions import InMemorySessionService
from google.adk.events import Event
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

# --- 1. OpenTelemetry Setup ---
def setup_opentelemetry_tracer():
    """Configures the Tracer to output to the console for a runnable demo."""
    
    # 1. Create a TracerProvider
    provider = TracerProvider()
    
    # 2. Add a simple processor that exports traces to the console
    # This shows the raw trace data and attributes!
    provider.add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter())) 
    
    # 3. Set it as the global provider
    trace.set_tracer_provider(provider)
    
    return trace.get_tracer("finops.adk.agent")

# --- 2. FinOps Agent Execution Logic ---
async def run_finops_session(tracer, prompt: str, team_id: str, project_code: str):
    """
    Runs the ADK Agent inside a custom FinOps-tagged OpenTelemetry Span.
    
    Args:
        tracer: The configured OpenTelemetry Tracer.
        prompt: The user input for the agent.
        team_id: The FinOps ID for cost allocation (who).
        project_code: The FinOps ID for the project (what).
    """
    
    # --- Define the Agent based on team ---
    if "Marketing" in team_id:
        agent = LlmAgent(
            name="Marketing_Copywriter",
            model="gemini-2.5-flash", 
            instruction="You are a professional copywriter. Write a concise, 1-sentence headline for the given topic.",
        )
    else:
        agent = LlmAgent(
            name="Engineering_Assistant",
            model="gemini-2.5-flash", 
            instruction="You are a software engineering assistant. Generate clear, professional documentation and code examples.",
        )

    # --- Create the FinOps Allocation Span ---
    # All agent activity (including LLM calls) inside this 'with' block 
    # will be a child of this span and inherit its tags!
    with tracer.start_as_current_span("adk-agent-session") as span:
        
        # MANDATORY FinOps Allocation Tags
        span.set_attribute("finops.team_id", team_id) 
        span.set_attribute("finops.project_code", project_code)
        span.set_attribute("llm.model_used", agent.model)
        
        print(f"\n--- New Session Started ---\nProject: {project_code} | Team: {team_id}")
        
        # --- Run the ADK Agent ---
        session_service = InMemorySessionService()
        runner = Runner(app_name="finops-agent", agent=agent, session_service=session_service)

        try:
            session = await session_service.create_session(app_name="finops-agent", user_id=team_id)
            
            # Create message object with required attributes
            class Message:
                def __init__(self, content, role="user"):
                    self.content = content
                    self.role = role
                    self.parts = [{"text": content}]
            
            message = Message(prompt)
            async for response in runner.run_async(user_id=team_id, session_id=session.id, new_message=message):
                if hasattr(response, 'response') and response.response:
                    print(f"Agent Response: {response.response.text}")
                    break
            
        except Exception as e:
            span.set_attribute("error", True)
            span.set_attribute("error.message", str(e))
            print(f"!! ADK ERROR: {e}")
            
# --- 3. Main Execution ---
async def main():
    if not os.getenv("GEMINI_API_KEY"):
        print("ERROR: Please set the GEMINI_API_KEY environment variable to run this code.")
        return

    # Initialize OpenTelemetry and get the tracer
    tracer = setup_opentelemetry_tracer()

    # SCENARIO 1: Marketing Team's blog post draft
    await run_finops_session(
        tracer,
        prompt="A short, catchy headline for a new blog post about AI cost optimization.", 
        team_id="Marketing-A", 
        project_code="BLOG-FINOPS-001"
    )

    # SCENARIO 2: Engineering Team's internal tool (different allocation)
    await run_finops_session(
        tracer,
        prompt="Generate a docstring for a function that calculates token cost.", 
        team_id="Engineering-B", 
        project_code="INTERNAL-DEV-005"
    )
    
    print("\n--- Execution Complete ---\nCheck the console output above. The [SpanExporter] output should clearly show the token counts (under Span Attributes) nestled under the custom FinOps tags!")


if __name__ == "__main__":
    asyncio.run(main())
