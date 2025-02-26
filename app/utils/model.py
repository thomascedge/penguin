from pydantic import BaseModel, Field, ConfigDict
from pydantic_extra_types.country import CountryAlpha2
from bson import ObjectId
from typing import Optional, Annotated
from enum import Enum


class Status(Enum):
    OKAY = 0
    CREATED = 1
    NOT_CREATED = 2
    INSUFFICIENT_INFORMATION = 3
    # Status.name, Status.value

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
    model_config = ConfigDict(arbitrary_types_allowed=True)
    receipt_id: Optional[ObjectId] = Field(default_factory=ObjectId, alias="_id")
    user_id: Optional[str] = None
    retailer: str
    purchase_date: str = Field(..., alias='purchaseDate')
    purchase_time: str = Field(..., alias='purchaseTime')
    items: list[Item]
    total: str
    points: Optional[int] = Field(default_factory=int)
    points_breakdown: Optional[str] = Field(default_factory=str)

class User(BaseModel):
    """
    Schema for a user.
    """
    model_config = ConfigDict(arbitrary_types_allowed=True)
    user_id: Optional[ObjectId] = Field(default_factory=ObjectId, alias="_id")
    name: str
    age: int
    birthday: str
    address_street: str
    address_state_code: str
    address_country_code: CountryAlpha2
    address_zip_code: str
    email: str
