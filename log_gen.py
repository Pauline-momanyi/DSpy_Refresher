import random
import time

# Example log levels
log_levels = ["INFO", "WARNING", "ERROR", "CRITICAL", "DEBUG"]

# Example log messages
messages = [
    "User login successful",
    "Database connection failed",
    "CPU usage exceeded threshold",
    "File not found error",
    "Service restarted successfully",
]

def generate_logs(file_name="sample_logs.log", num_lines=100):
    with open(file_name, "w") as file:
        for _ in range(num_lines):
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            level = random.choice(log_levels)
            message = random.choice(messages)
            file.write(f"{timestamp} [{level}] - {message}\n")

    print(f"Generated {num_lines} log entries in {file_name}")

# Generate a sample log file
generate_logs()
