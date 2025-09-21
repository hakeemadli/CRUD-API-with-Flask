# CRUD API Authentication System Overview

## Authentication Flow

### 1. Key Infrastructure

- Uses asymmetric encryption with public/private key pair
  - `private.pem`: Used for signing JWT tokens
  - `public.pem`: Used for verifying JWT tokens
  - Algorithm: RS256 (RSA Signature with SHA-256)

### 2. User Management

- User data stored in `users.json`
- User schema:

```json
{
  "id": number,
  "user_id": string (email),
  "password": string
}
```

- Includes default admin user for initial setup

### 3. Authentication Endpoints

#### Register (`/register` POST)

1. Accepts JSON payload with `user_id` and `password`
2. Validates if user doesn't already exist
3. Assigns new unique ID
4. Stores user in `users.json`
5. Returns success message with user ID

#### Login (`/login` POST)

1. Accepts JSON payload with `user_id` and `password`
2. Validates credentials against stored users
3. Generates JWT token if valid
4. Returns token in response

### 4. Token System

#### Token Generation

- Generated upon successful login
- Contains:
  - `user_id`: User identifier
  - `exp`: Expiration time (24 hours from creation)
- Signed using private key (RS256)

#### Token Verification (`@token_required` decorator)

1. Extracts token from Authorization header
2. Validates token format ('Bearer' scheme)
3. Verifies token signature using public key
4. Checks token expiration
5. Makes user data available in request context (Flask's `g` object)

### 5. Security Features

- JWT expiration (24 hours)
- Bearer token authentication
- Asymmetric encryption for token signing/verification
- Email uniqueness validation
- Error handling for:
  - Missing authorization header
  - Invalid token format
  - Expired tokens
  - Invalid signatures
  - General token errors

## Permission Access

### Current Implementation

- Basic authentication (valid/invalid token)
- No role-based access control implemented
- All authenticated users have same access level

### Potential Enhancements

1. Role-based access
2. Permission levels
3. Token refresh mechanism
4. Password hashing
5. Rate limiting

## Technical Implementation Notes

### Dependencies

- Flask: Web framework
- PyJWT: JWT token handling
- JSON: Data storage
- Blueprint: Route modularization

### Security Considerations

1. Password storage is currently plaintext (should be hashed)
2. No password complexity requirements
3. No rate limiting on login attempts
4. Token revocation not implemented
5. Session management not implemented

### Notes

- Uses Blueprint for route organization
- Decorator pattern for token verification
- Error handling with appropriate HTTP status codes
- JSON response format standardization
- Modular code structure