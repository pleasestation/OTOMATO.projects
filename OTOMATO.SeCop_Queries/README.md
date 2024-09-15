# SecOps SQL Queries

Welcome to the SecOps SQL Queries repository. This repository contains various SQL queries designed to help identify potential security threats by analyzing login attempt data. The queries focus on failed login attempts, login patterns, and suspicious user behavior, which are essential for Security Operations (SecOps) teams.

## Table Structure

The `login_attempts` table contains the following fields:

- **`user_id`**: A unique identifier for the user attempting to log in.
- **`timestamp`**: The date and time of the login attempt.
- **`status`**: The result of the login attempt, either `'success'` or `'failure'`.

## Purpose

The purpose of this repository is to provide SQL queries that can be used to:

- **Detect Anomalies in Failed Login Attempts**: Identify users with abnormal numbers of failed login attempts, which could indicate a brute-force attack or suspicious activity.
- **Monitor User Login Behavior**: Track failed and successful login attempts for specific users over different time periods.
- **Generate Security Reports**: Use the queries to create detailed reports of user login activity, which can be used for auditing, alerting, or investigation purposes.

## Key Features

- **Failed Login Detection**: Identify users with multiple failed login attempts in a given period.
- **Rolling Time Window Analysis**: Track login attempts over a rolling 24-hour period to detect abnormal behavior.
- **User Monitoring**: Monitor and report failed logins, which can be useful for detecting security incidents in real time.

## Use Cases

1. **Brute-Force Attack Detection**: 
   - Detect when a user has more than a certain number of failed login attempts within a short time frame. This can help prevent or respond to potential brute-force attacks.
  
2. **Compromised Account Alerts**: 
   - Monitor users who have consistently failed login attempts, especially when attempts originate from different locations or IP addresses.
  
3. **Audit Logs**: 
   - Provide detailed login reports that include both failed and successful attempts, making it easier for security teams to conduct audits or investigations.

4. **Real-Time Security Monitoring**: 
   - Generate alerts when users exceed predefined thresholds for failed login attempts, enabling faster response times.

## How to Use

1. Clone this repository.
2. Ensure the database structure includes the `login_attempts` table, or modify the queries to fit your existing database.
3. Execute the provided SQL queries in your SQL environment (e.g., PostgreSQL, MySQL, SQL Server).
4. Customize the queries based on your security needs (e.g., adjust the threshold for failed attempts or extend the time window).

## Contributing

We welcome contributions to this project! If you have any improvements, new ideas, or additional queries that could enhance security analysis, feel free to open a pull request or issue.

## License

This repository is licensed under the MIT License. See the `LICENSE` file for more details.

