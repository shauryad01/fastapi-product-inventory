# FastAPI Product Inventory

A full-stack product inventory application with:

- **Backend:** FastAPI + SQLAlchemy + PostgreSQL
- **Frontend:** React + Axios
- **Auth:** Basic email/password signup & login endpoints

## Project Structure

```text
.
├── main.py
├── config.py
├── database/
│   ├── connection.py
│   ├── product_model.py
│   └── user_model.py
├── routes/
│   ├── auth_routes.py
│   └── product_routes.py
├── schemas/
│   ├── product_schema.py
│   └── user_schema.py
├── utils/
│   └── auth.py
├── requirements.txt
└── frontend/
    ├── package.json
    └── src/
```

## Features

- User signup and login (`/auth/signup`, `/auth/login`)
- Product CRUD API (`/products`)
- React dashboard for:
  - creating, editing, deleting products
  - listing products
  - client-side search and sorting

## Prerequisites

- Python 3.10+
- Node.js 18+
- PostgreSQL

## Environment Variables

Create a `.env` file in the repository root:

```env
DB_URL=postgresql://<username>:<password>@localhost:5432/<database_name>
```

`database/connection.py` reads `DB_URL` to create the SQLAlchemy engine.

## Backend Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend runs at: `http://localhost:8000`

Interactive docs:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Frontend Setup

```bash
cd frontend
npm install
npm start
```

Frontend runs at: `http://localhost:3000`

## API Overview

### Auth

- `POST /auth/signup`
- `POST /auth/login`
- `GET /auth/test`

### Products

- `GET /products/` — list all products
- `GET /products/{id}` — get one product
- `POST /products/` — create a product
- `PUT /products/{id}` — update a product
- `DELETE /products/{id}` — delete a product

## Sample Product Payload

```json
{
  "name": "Keyboard",
  "description": "Mechanical keyboard",
  "price": 79.99,
  "quantity": 15
}
```

## Notes

- Product `added_by` is linked to the most recently logged-in user through `config.current_u_id`.
- `utils/auth.py` currently returns a placeholder access token (`123`).
- CORS is configured in `main.py` for `http://localhost:3000`.

## Troubleshooting

- **Database connection errors:** verify `DB_URL`, PostgreSQL service status, and database credentials.
- **Frontend cannot reach API:** make sure backend is running on port `8000` and frontend on `3000`.
- **Dependency issues:** delete lockfiles/node_modules and reinstall (`npm install`, `pip install -r requirements.txt`).
