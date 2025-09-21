# Logging System Documentation

## Overview

This document details the logging system implemented in the Flask API, featuring JSON formatting and comprehensive request tracking.

## Core Components

### Logger Configuration

#### File Structure
- **Main File**: `logger.py`
- **Classes**: 
  - `log_formatter`: Custom formatter for JSON output
- **Functions**:
  - `get_logger`: Logger initialization and configuration

### Logging Features

#### Timestamp Format
- Format: `DD/MMM/YYYY HH:MM:SS`
- Example: `19/Sep/2025 20:17:07`
- Implementation: Uses `datetime.datetime.now().strftime("%d/%b/%Y %H:%M:%S")`

#### Log Structure

##### Core Fields
- `time`: Formatted timestamp
- `level`: Log level (INFO, DEBUG, ERROR, etc.)
- `logger`: Logger name (default: "CRUD-API")
- `message`: Log message content

##### Extended Fields
- `endpoint`: API endpoint accessed
- `method`: HTTP method used
- `status`: Response status code
- `response_time`: Request processing duration
- `ip_address`: Client IP address
- `user_agent`: Client browser/application info

### Log Storage

#### File Output
- **Location**: `log.json`
- **Format**: JSON
- **Structure**: Array of log entries

Example Log Entry:
```json
{
  "time": "19/Sep/2025 20:17:07",
  "level": "INFO",
  "logger": "CRUD-API",
  "message": "Request processed successfully",
  "endpoint": "/items/1",
  "method": "GET",
  "status": 200,
  "response_time": "0.023s",
  "ip_address": "127.0.0.1",
  "user_agent": "Mozilla/5.0..."
}
```

## Features

### 1. Request Tracking
- Complete request lifecycle logging
- Request duration measurement
- Client information capture

### 2. Error Handling
- Exception logging with stack traces
- Error context preservation
- Custom error messages

### 3. Performance Monitoring
- Response time tracking
- Resource usage logging
- API endpoint performance metrics

### 4. Security Logging
- Authentication attempts
- Access control decisions
- Security-related events

### Implementation Details

#### Log Formatter
```python
class log_formatter(logging.Formatter):
    def format(self,record):
        log_record = {
            "time": datetime.datetime.now().strftime("%d/%b/%Y %H:%M:%S"),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage()
        }
        # Dynamic fields added if present
        return json.dumps(log_record, indent=4)
```

#### Logger Setup
```python
def get_logger(name="CRUD-API"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    # Configure handlers
    # ... handler setup ...
    return logger
```

### Usage Examples

#### Basic Logging
```python
from logger import logger

# Info level logging
logger.info("Application started")

# Error logging
logger.error("Database connection failed")
```

#### Request Logging
```python
logger.info("Processing request", extra={
    'method': 'POST',
    'url': '/items',
    'client_ip': request.remote_addr
})
```

#### Performance Monitoring
```python
logger.info("Request completed", extra={
    'duration': process_time,
    'status_code': 200
})
```

## Notes

1. Always include relevant context in logs
2. Use appropriate log levels
3. Include error details in exception logging
4. Monitor log file size
5. Regular log rotation (recommended)