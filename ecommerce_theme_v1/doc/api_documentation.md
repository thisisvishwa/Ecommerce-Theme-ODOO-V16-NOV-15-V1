# API Documentation

## Overview

This document provides the API documentation for the ecommerce_theme_v1 developed in Odoo v16 Community Edition.

## Endpoints

### Product

- **GET /api/products**: Fetches all products.
- **GET /api/products/{id}**: Fetches a specific product by its ID.
- **POST /api/products**: Creates a new product. Requires admin privileges.

### User

- **GET /api/users/{id}**: Fetches a specific user by their ID.
- **POST /api/users**: Creates a new user.
- **PUT /api/users/{id}**: Updates a specific user. Requires the user's credentials or admin privileges.
- **DELETE /api/users/{id}**: Deletes a specific user. Requires admin privileges.

### Review

- **GET /api/reviews**: Fetches all reviews.
- **GET /api/reviews/{id}**: Fetches a specific review by its ID.
- **POST /api/reviews**: Creates a new review. Requires the user's credentials.
- **PUT /api/reviews/{id}**: Updates a specific review. Requires the user's credentials or admin privileges.
- **DELETE /api/reviews/{id}**: Deletes a specific review. Requires admin privileges.

### Cart

- **GET /api/cart/{id}**: Fetches a specific cart by its ID.
- **POST /api/cart**: Creates a new cart. Requires the user's credentials.
- **PUT /api/cart/{id}**: Updates a specific cart. Requires the user's credentials.
- **DELETE /api/cart/{id}**: Deletes a specific cart. Requires the user's credentials.

## Error Handling

All API endpoints return standard HTTP status codes. In case of an error, a JSON response will be returned with the following format:

```json
{
    "error": "Error message"
}
```

## Authentication

Some endpoints require authentication. This is done by sending the user's credentials in the headers of the HTTP request.

## Rate Limiting

To prevent abuse, rate limiting is implemented on all API endpoints. Each user can make up to 1000 requests per day.

## Pagination

Endpoints that return multiple items will be paginated to 50 items by default. You can specify further pages with the `?page` parameter.