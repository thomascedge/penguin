from pydantic import BaseModel, Field

class Item(BaseModel):
    short_description: str = Field(..., alias='shortDescription')
    price: str

class Reciept(BaseModel):
    retailer: str
    purchase_date: str = Field(..., alias='purchaseDate')
    purchase_time: str = Field(..., alias='purchaseTime')
    items: list[Item]
    total: str
