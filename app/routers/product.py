from fastapi import APIRouter, HTTPException
from app.models.product import Product
from app.schemas.product import ProductCreate
from uuid import UUID

router = APIRouter()

@router.post("/")
async def create_product(product: ProductCreate):
    new_product = Product(**product.dict())
    await new_product.insert()
    return new_product

@router.get("/")
async def list_products():
    return await Product.find_all().to_list()

@router.get("/{product_id}")
async def get_product(product_id: UUID):
    product = await Product.find_one(Product.id == product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/{product_id}")
async def update_product(product_id: UUID, updated_data: ProductCreate):
    product = await Product.find_one(Product.id == product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    product.name = updated_data.name
    product.description = updated_data.description
    product.price = updated_data.price
    product.quantity = updated_data.quantity
    await product.save()
    return product

@router.delete("/{product_id}")
async def delete_product(product_id: UUID):
    product = await Product.find_one(Product.id == product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    await product.delete()
    return {"message": "Product deleted"}
