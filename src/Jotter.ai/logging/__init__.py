# Imports
import os
import sys
import logging

# %(asctime)s: Timestamp of the log event.
# %(levelname)s: Severity level of the log (e.g., INFO, ERROR).
# %(module)s: Module from which the log originated.
# %(message)s: Actual log message.
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

#Combines the directory path with a filename (running_logs.log) for the log file
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


#Logging Configuration
#Sets the logging level to INFO, capturing events of INFO level and above (INFO, WARNING, ERROR, etc.).
#Configures two handlers:
#FileHandler: Writes log messages to running_logs.log.
#StreamHandler: Outputs log messages to the console (via sys.stdout)
logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("textSummarizerLogger")