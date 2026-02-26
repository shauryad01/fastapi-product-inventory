from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from routes import product_routes, auth_routes
from database.connection import engine
from database import product_model, user_model

app = FastAPI(title="Product API")
router = APIRouter()

user_model.Base.metadata.create_all(bind=engine)
product_model.Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product_routes.router)
app.include_router(auth_routes.router)

@router.get("/")
def root():
    return {"message": "API running"}