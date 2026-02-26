from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.connection import session
from database import product_model
from schemas.product_schema import ProductCreate, ProductResponse
import config

router = APIRouter(prefix="/products", tags=["Products"])

# DB dependency
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

# GET all products
@router.get("/", response_model=list[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return db.query(product_model.Product).all()

# GET single product
@router.get("/{id}", response_model=ProductResponse)
def get_product(id: int, db: Session = Depends(get_db)):
    product = db.query(product_model.Product).filter(product_model.Product.id == id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# CREATE product
@router.post("/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    new_product = product_model.Product(**product.dict(), added_by = config.current_u_id)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

# UPDATE product
@router.put("/{id}")
def update_product(id: int, product: ProductCreate, db: Session = Depends(get_db)):
    db_product = db.query(product_model.Product).filter(product_model.Product.id == id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    for key, value in product.model_dump().items():
        setattr(db_product, key, value)

    db.commit()
    return {"message": "Updated successfully"}

# DELETE product
@router.delete("/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(product_model.Product).filter(product_model.Product.id == id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(db_product)
    db.commit()
    return {"message": "Deleted"}