from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import product_routes
from database.connection import engine
from database import models

app = FastAPI(title="Product API")

models.Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product_routes.router)

@app.get("/")
def root():
    return {"message": "API running"}