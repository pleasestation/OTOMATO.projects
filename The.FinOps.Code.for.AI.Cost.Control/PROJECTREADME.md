# FinOps AI OpenTelemetry Demo

A demonstration project showing how to implement FinOps cost allocation tracking for AI/LLM workloads using OpenTelemetry and Google's Agent Development Kit (ADK).

## What it does

This project demonstrates how to:
- Track AI agent usage with custom FinOps attributes (team_id, project_code)
- Monitor LLM token consumption and costs per team/project
- Use OpenTelemetry spans to capture detailed telemetry data
- Implement different AI agents based on team requirements

The application creates two different AI agents:
- **Marketing Copywriter**: Generates marketing headlines and copy
- **Engineering Assistant**: Creates technical documentation and code examples

Each agent session is wrapped in OpenTelemetry spans with FinOps allocation tags for cost tracking and attribution.

## Prerequisites

- Python 3.13+
- Google Gemini API key

## Setup

1. Clone the repository and navigate to the project directory

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set your Gemini API key:
```bash
export GEMINI_API_KEY="your-api-key-here"
```

## Running the application

### Run the main demo:
```bash
python agent.py
```

This will execute two scenarios:
1. Marketing team generating a blog post headline
2. Engineering team creating function documentation

### Run the basic hello world:
```bash
python main.py
```

## Output

The application outputs OpenTelemetry trace data to the console, showing:
- Span details with FinOps allocation attributes
- Token usage and model information
- Team and project cost attribution
- Agent responses

Look for `[SpanExporter]` output in the console to see the detailed telemetry data with FinOps tags.

## Project Structure

- `agent.py` - Main application with OpenTelemetry integration and FinOps tracking
- `main.py` - Simple hello world entry point
- `pyproject.toml` - Project configuration and dependencies
- `requirements.txt` - Python package requirements
