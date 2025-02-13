from pydantic import BaseModel, Field
from sqlmodel import Field, SQLModel

class Item(BaseModel):
    """
    Schema for reciept items. Items in a reciept are a collection, list, of two
    fields: a description and the price for each item. There should be at least
    one item per reciept.
    """
    short_description: str = Field(..., alias='shortDescription')
    price: str

class Receipt(BaseModel):
    """
    Schema for a receipt. A receipt should have the fields for a retailer,
    purchase date and time, a list of items, and a total. If a reciept does not
    contain all of these fields, it should be rejected.
    """
    retailer: str
    purchase_date: str = Field(..., alias='purchaseDate')
    purchase_time: str = Field(..., alias='purchaseTime')
    items: list[Item]
    total: str

class StoredData(SQLModel, table=True):
    """
    Relational database for data storage.
    """
    id: int = Field(default=None, primary_key=True)
    points: int