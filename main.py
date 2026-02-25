from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def greet():
    return "Hello, World!"

products = [
    Product(id= 1, name = "Laptop", description = "A high-performance laptop", price = 999.99, quantity = 10)
    , Product(id= 2, name = "Smartphone", description = "A latest model smartphone", price = 499.99, quantity = 20)
    , Product(id= 3, name = "Headphones", description = "Noise-cancelling headphones", price = 199.99, quantity = 15)
    , Product(id= 4, name = "Smartwatch", description = "A smartwatch with various features", price = 299.99, quantity = 5)
]

@app.get("/products")
def get_products():
    return products

@app.get("/product")
def find_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    return None

@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product

@app.put("/product")
def update_product(id:int,product:Product):
    for pr in products:
        if pr.id == id:
            pr = product
            return "Product Added"
    return "Product Not Found"
