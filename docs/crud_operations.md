# CRUD Operations Documentation

## Overview

This document details the CRUD (Create, Read, Update, Delete) operations implemented in the Flask API.

## API Endpoints

### 1. Create Operation

#### Create Item
- **Endpoint**: `/items/`
- **Method**: POST
- **Request Body**: JSON data
- **Response**: Newly created item with ID
- **Status Codes**: 201 (Created), 400 (Error)

Example Request:
```json
{
  "data": {
    "name": "John Doe",
    "age": 30
  }
}
```

### 2. Read Operations

#### Get All Items
- **Endpoint**: `/items/`
- **Method**: GET
- **Response**: List of all items
- **Status Codes**: 200 (Success), 400 (Error)

#### Get Single Item
- **Endpoint**: `/items/<id>`
- **Method**: GET
- **Response**: Single item by ID
- **Status Codes**: 200 (Success), 404 (Not Found), 400 (Error)

### 3. Update Operation

#### Update Item
- **Endpoint**: `/items/<id>`
- **Method**: PUT
- **Request Body**: Updated JSON data
- **Response**: Updated item
- **Status Codes**: 200 (Success), 404 (Not Found), 400 (Error)

Example Request:
```json
{
  "data": {
    "name": "John Doe Updated",
    "age": 31
  }
}
```

### 4. Delete Operation

#### Delete Item
- **Endpoint**: `/items/<id>`
- **Method**: DELETE
- **Response**: Success message
- **Status Codes**: 200 (Success), 404 (Not Found), 400 (Error)

## Data Structure

### Default Data Format
```json
{
  "id": number,
  "data": {
    "name": string,
    "age": number
  }
}
```

## Implementation Details

### Storage
- Uses local JSON file (`output.json`) for data persistence
- Automatic ID generation for new items
- Data validation before storage
- Error handling for file operations

## Notes

- The API uses a local JSON file for data persistence
- Default data structure includes name and age fields
- Implements standard HTTP status codes for responses
- Includes error handling for JSON operations
- RESTful architecture format