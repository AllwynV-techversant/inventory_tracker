from fastapi import FastAPI
from app.database import init_db
from app.routers import user, product

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await init_db()

app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(product.router, prefix="/products", tags=["Products"])

@app.get("/")
async def root():
    return {"message": "API is running"}
