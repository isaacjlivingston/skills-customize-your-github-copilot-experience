# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using the FastAPI framework and practice core backend development skills such as route creation, request validation, and structured JSON responses.

## 📝 Tasks

### 🛠️ Create Basic API Endpoints

#### Description
Set up a FastAPI application and implement core endpoints for checking service health and listing in-memory resources.

#### Requirements
Completed program should:

- Create a FastAPI app instance in `starter-code.py`.
- Add a `GET /` endpoint that returns a welcome message in JSON.
- Add a `GET /health` endpoint that returns a status response such as `{ "status": "ok" }`.
- Add a `GET /items` endpoint that returns a list of items from an in-memory data structure.


### 🛠️ Add CRUD Operations and Validation

#### Description
Expand the API to support creating, updating, and deleting items while validating request data with Pydantic models.

#### Requirements
Completed program should:

- Define an item model with FastAPI/Pydantic that includes at least `id`, `name`, and `price`.
- Add a `POST /items` endpoint to create a new item.
- Add a `PUT /items/{item_id}` endpoint to update an existing item.
- Add a `DELETE /items/{item_id}` endpoint to remove an item.
- Return appropriate HTTP status codes for successful and failed operations.


### 🛠️ Test API Behavior with Example Requests

#### Description
Run the application locally and verify endpoint behavior using interactive docs or HTTP requests.

#### Requirements
Completed program should:

- Start the API with Uvicorn.
- Use the auto-generated docs at `/docs` to test endpoints.
- Demonstrate at least one successful create request and one not-found response.
- Keep API responses in valid JSON format.

```text
Example request/response (abbreviated)

POST /items
{
  "id": 3,
  "name": "Notebook",
  "price": 4.99
}

201 Created
{
  "message": "Item created",
  "item": {
    "id": 3,
    "name": "Notebook",
    "price": 4.99
  }
}
```
