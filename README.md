# CRUD API with Flask

## Project Overview 💡

A RESTful CRUD (Create, Read, Update, Delete) API built with Flask, featuring comprehensive logging and authentication systems.

## Documentation 📚

Detailed documentation is available for each component of the system:

### Core Components

1. [Authentication System](./docs/authentication_overview.md)
   - JWT-based authentication
   - Token management
   - Security features

2. [CRUD Operations](./docs/crud_operations.md)
   - Create, Read, Update, Delete endpoints
   - Data structure
   - Implementation details

3. [Logging System](./docs/logging_system.md)
   - JSON-formatted logging
   - Request tracking
   - Performance monitoring

## Technologies Used 🛠️

- **Flask**: Web framework (v3.1.2)
- **Python**: Programming language
- **JSON**: Data storage format
- **JWT**: Authentication tokens

### Dependencies

- Flask 3.1.2
- Werkzeug 3.1.3
- Jinja2 3.1.6
- PyJWT for authentication
- Other supporting packages

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

## Key Features ✨

1. **Authentication**
   - JWT token-based authentication
   - Public/private key encryption
   - User management

2. **CRUD Operations**
   - RESTful API endpoints
   - JSON data storage
   - Automatic ID generation

3. **Logging**
   - JSON-formatted logs
   - Request tracking
   - Performance monitoring

4. **Security**
   - Token-based authentication
   - Error handling
   - Input validation

## Quick Start 🚀

1. Clone the repository:

```bash
git clone https://github.com/hakeemadli/CRUD-API-with-Flask.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Flask application:

   ```bash
   python app.py
   
   or
   
   flask run --host = <your-ip-addr> --port= <your-available-port>
   ```

4. API will be available at `http://localhost: port`

5. You can test the end-point response/request using Postman or Curl.

## Project Structure 📁

```
CRUD-API-with-Flask/
│
├── app.py              # Main application file
├── auth.py            # Authentication module
├── crud.py            # CRUD operations
├── logger.py          # Logging system
├── config.py          # Configuration
│
├── docs/              # Documentation
│   ├── authentication_overview.md
│   ├── crud_operations.md
│   └── logging_system.md
│
├── static/            # Static files
│   └── index.html     # Frontend interface
│
└── requirements.txt   # Project dependencies
```

## License 📝

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing 🤝

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

### Best Practices
1. Always include relevant context in logs
2. Use appropriate log levels
3. Include error details in exception logging
4. Monitor log file size
5. Regular log rotation (recommended)


