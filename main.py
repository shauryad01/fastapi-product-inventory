from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from database import session, engine
import database_models
from sqlalchemy.orm import Session
import http

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"]
)

database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "Hello, World!"

products = [
    Product(id= 1, name = "Laptop", description = "A high-performance laptop", price = 999.99, quantity = 10)
    , Product(id= 2, name = "Smartphone", description = "A latest model smartphone", price = 499.99, quantity = 20)
    , Product(id= 3, name = "Headphones", description = "Noise-cancelling headphones", price = 199.99, quantity = 15)
    , Product(id= 4, name = "Smartwatch", description = "A smartwatch with various features", price = 299.99, quantity = 5)
]

def get_db():
    db = session()
    yield db
    db.close()

def init_db():
    db=session()
    count = db.query(database_models.Product).count
    if count == 0:
        for pr in products:
            db.add(database_models.Product(**pr.model_dump()))
        db.commit()

init_db()

@app.get("/products")
def get_products(db:Session = Depends(get_db)):
    db_products = db.query(database_models.Product).all()
    return db_products

@app.get("/products/{id}")
def find_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        return db_product
    return "Product not found"

@app.post("/products")
def add_product(product: Product, db: Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product

@app.put("/products/{id}")
def update_product(id:int,product:Product, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_product:
        db_product.name=product.name
        db_product.description=product.description
        db_product.price=product.price
        db_product.quantity=product.quantity
        db.commit()
        return "Product Added"
    else:
        return "Product Not Found"

@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(db_product)
    db.commit()
    return {"message": "Product deleted successfully"}