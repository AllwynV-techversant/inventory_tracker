from beanie import Document
from pydantic import Field
from typing import Optional
from uuid import UUID, uuid4

class Product(Document):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: Optional[str] = None
    price: float
    quantity: int

    class Settings:
        name = "products"
