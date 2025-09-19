# CRUD API with Flask - Project Overview 💡🧑‍💻

## Project Description

This is a RESTful CRUD (Create, Read, Update, Delete) API built with Flask, implementing basic data operations with JSON file storage. The API provides endpoints for managing items with unique IDs and associated data, featuring advanced logging capabilities.

## Technologies Used
- **Flask**: Web framework (v3.1.2)
- **Python**: Programming language
- **JSON**: Data storage format
- **Dependencies**:
  - Flask 3.1.2
  - Werkzeug 3.1.3
  - Jinja2 3.1.6
  - Other supporting packages (blinker, click, etc.)

## Architecture
- **Storage**: Local JSON file (`output.json`)
- **Data Structure**: List of objects with `id` and `data` fields
- **Default Data Format**: 
```json
{
  "id": number,
  "data": {
    "name": string,
    "age": number
  }
}
```

## API Endpoints

### 1. Welcome Route
- **Endpoint**: `/`
- **Method**: GET
- **Description**: Welcome page and initializes JSON file if not exists

### 2. Get All Items
- **Endpoint**: `/items/`
- **Method**: GET
- **Response**: List of all items
- **Status Codes**: 200 (Success), 400 (Error)

### 3. Get Single Item
- **Endpoint**: `/items/<id>`
- **Method**: GET
- **Response**: Single item by ID
- **Status Codes**: 200 (Success), 404 (Not Found), 400 (Error)

### 4. Create Item
- **Endpoint**: `/items/`
- **Method**: POST
- **Request Body**: JSON data
- **Response**: Newly created item with ID
- **Status Codes**: 201 (Created), 400 (Error)

### 5. Update Item
- **Endpoint**: `/items/<id>`
- **Method**: PUT
- **Request Body**: Updated JSON data
- **Response**: Updated item
- **Status Codes**: 200 (Success), 404 (Not Found), 400 (Error)

## Features
1. Persistent storage using JSON file
2. Automatic ID generation for new items
3. Error handling for file operations
4. JSON validation
5. RESTful architecture

## Logging System Implementation
Our Flask CRUD API implements a sophisticated logging system with JSON formatting and comprehensive request tracking.

### Core Components

#### 1. Logger Configuration
**File**: `logger.py`
**Main Components**:
- `log_formatter` class: Custom formatter for JSON output
- `get_logger` function: Logger initialization and configuration
- Global `logger` instance

#### 2. Logging Features

##### Timestamp Format
- Format: `DD/MMM/YYYY HH:MM:SS`
- Example: `19/Sep/2025 20:17:07`
- Implementation: 
```python
datetime.datetime.now().strftime("%d/%b/%Y %H:%M:%S")
```

##### Log Structure
**Core Fields**:
- `time`: Formatted timestamp
- `level`: Log level (INFO, DEBUG, ERROR, etc.)
- `logger`: Logger name (default: "CRUD-API")
- `message`: Log message content

**Dynamic Fields**:
- `method`: HTTP request method
- `url`: Request endpoint
- `status_code`: Response status
- `duration`: Request processing time
- `client_ip`: Client's IP address

##### Output Handlers
1. **Stream Handler**
   - Outputs to console
   - Uses JSON formatting
   - Real-time monitoring

2. **File Handler**
   - File: `log.json`
   - Append mode
   - UTF-8 encoding
   - Persistent storage

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

### Best Practices
1. Always include relevant context in logs
2. Use appropriate log levels
3. Include error details in exception logging
4. Monitor log file size
5. Regular log rotation (recommended)

## Project Structure
```
CRUD-API-with-Flask/
├── app.py              # Main application file
├── logging.py          # Logging configuration
├── output.json         # Data storage
├── requirements.txt    # Project dependencies
└── README.md          # Project documentation
```

## Getting Started
1. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the Flask application:
     ```bash
   python app.py
   
   or
   
   flask run --host = <your-ip-addr> --port= <your-available-port>
   ```
3. API will be available at `http://localhost:port`

## Notes
- The API uses a local JSON file for data persistence
- Default data structure includes name and age fields
- Implements standard HTTP status codes for responses
- Includes error handling for JSON operations