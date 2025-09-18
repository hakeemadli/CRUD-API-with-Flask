import logging
import json
import datetime

log_file = "app_log.json"

class log_formatter(logging.Formatter):
    def format(self,record):
        log_record= {
            "time" : datetime.datetime.now().isoformat(),
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
    
def get_logger(name ="CRUD-API"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        # Write logs to file instead of console
        handler_for_stream = logging.StreamHandler()
        handler_with_file = logging.FileHandler(log_file, mode="a", encoding="utf-8")
        handler_with_file.setFormatter(log_formatter())
        handler_for_stream.setFormatter(log_formatter())
        logger.addHandler(handler_for_stream)
        logger.addHandler(handler_with_file)

    return logger



logger = get_logger()