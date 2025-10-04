import logging, json, datetime

log_file = "log.json"

class log_formatter(logging.Formatter):
    def format(self,record):
        log_record= {
            "time" : datetime.datetime.now().strftime("%d/%b/%Y %H:%M:%S"),
            "level" : record.levelname,
            "logger": record.name,
            "message" :record.getMessage(),
       }
        
        # Add any extra fields from the record
        if hasattr(record, 'method'):
            log_record['method'] = record.method
        if hasattr(record, 'url'):
            log_record['url'] = record.url
        if hasattr(record, 'status_code'):
            log_record['status_code'] = record.status_code
        if hasattr(record, 'duration'):
            log_record['duration'] = record.duration
        if hasattr(record, 'client_ip'):
            log_record['client_ip'] = record.client_ip
        
        return json.dumps(log_record, indent= 4)
    
def get_logger(name):
    """
    Get a logger instance with the specified name.
    
    Args:
        name: Required. Name to identify the logger (e.g. user_id or component name)
    """
    if not name:
        raise ValueError("Logger name must be provided")

    # Check if logger already exists
    existing_logger = logging.getLogger(name)
    if existing_logger.handlers:
        return existing_logger

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # Remove any existing handlers
    logger.handlers = []
    
    # Create handlers
    handler_for_stream = logging.StreamHandler()
    handler_with_file = logging.FileHandler(log_file, mode="a", encoding="utf-8")
    
    # Set formatter for both handlers
    formatter = log_formatter()
    handler_with_file.setFormatter(formatter)
    handler_for_stream.setFormatter(formatter)
    
    # Set levels for handlers
    handler_for_stream.setLevel(logging.DEBUG)
    handler_with_file.setLevel(logging.DEBUG)
    
    # Add handlers to logger
    logger.addHandler(handler_for_stream)
    handler_with_file.setLevel(logging.DEBUG)
    logger.addHandler(handler_with_file)
    
    # Prevent propagation to root logger
    logger.propagate = False
    
    return logger

# Initialize with a system logger for internal use
logger = get_logger("system")





