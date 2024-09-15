You are tasked with creating a report for failed login attempts on a secure system. Given the table login_attempts, which has the following columns:

user_id: ID of the user
timestamp: Date and time of the login attempt
status: Status of the login attempt (either 'success' or 'failure')
Write a SQL query to find all users who had more than 3 failed login attempts within a 24-hour period. For each user, show the user_id and the total count of failed attempts within that period.

Schema:
login_attempts(user_id, timestamp, status)
