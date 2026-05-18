# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a functional REST API using the FastAPI framework, learning how to define routes, handle HTTP methods, work with request/response models, and document your API automatically.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI Application

#### Description
Set up a FastAPI application with a root endpoint and at least one resource endpoint. Run the development server and verify your API responds correctly.

#### Requirements
Completed program should:

- Import and initialize a `FastAPI` app instance
- Define a `GET /` root endpoint that returns a welcome message
- Define a `GET /items` endpoint that returns a list of at least 3 sample items
- Run successfully with `uvicorn` and respond to requests


### 🛠️ Add Path and Query Parameters

#### Description
Extend your API to support dynamic routes and optional query parameters so callers can filter or retrieve specific resources.

#### Requirements
Completed program should:

- Define a `GET /items/{item_id}` endpoint that returns a single item by its ID
- Return a `404` HTTP error with a descriptive message when the item is not found
- Add an optional `q` query parameter to `GET /items` that filters results by name (case-insensitive)
- Example: `GET /items/1` returns the item with ID 1; `GET /items?q=book` returns only items whose name contains "book"


### 🛠️ Handle POST Requests with Pydantic Models

#### Description
Allow clients to create new items by accepting JSON request bodies validated with a Pydantic model.

#### Requirements
Completed program should:

- Define a `Pydantic` `BaseModel` called `Item` with fields: `name` (str), `price` (float), and `in_stock` (bool)
- Implement a `POST /items` endpoint that accepts an `Item` body and appends it to the items list
- Return the newly created item with a `201` status code
- Reject requests with missing or invalid fields automatically (FastAPI/Pydantic handles this)
- Example request body:
  ```json
  { "name": "Notebook", "price": 4.99, "in_stock": true }
  ```
