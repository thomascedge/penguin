from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, Date, Time, DateTime, BigInteger

from .database import Base

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

class User(BaseModel):
    """
    Schema for a user.
    """
    user_id: int
    name: str
    age: int
    birthday: str
    address_street: str
    address_state: str
    address_country: str
    address_zip_code: str
    email: str


class ReceiptData(Base):
    """
    Relational database for points and receipt data storage.
    """
    __tablename__='receipt_data'
    receipt_id: str = Column(String(255), primary_key=True, index=True)
    user_id: int = Column(BigInteger, primary_key=True, index=True)
    receipt_entry_date: Date = Column(Date, index=True)
    receipt_retailer: str = Column(String(255), index=True)
    receipt_purchase_date: Date = Column(Date, index=True)
    receipt_purchase_time: Time = Column(Time, index=True)
    receipt_total: int = Column(Integer)
    receipt_items: str = Column(String(255))
    points: int = Column(Integer)
    points_breakdown: str = Column(String(255))
    # standard data warehouse metadata → best practices for data governance
    dwh_created_date: Date = Column(DateTime, index=True)
    dwh_update_date: DateTime = Column(DateTime, index=True)
    dwh_table_name: str = Column(String(255))
    dwh_primary_key: str = Column(String(255))

class UserData(Base):
    """
    Relational database for customer information storage.
    """
    __tablename__='user'
    user_id: int = Column(BigInteger, primary_key=True, index=True)
    name: str = Column(String(255))
    age: int = Column(Integer)
    birthday: Date =  Column(Date)
    address_street: str = Column(String(255))
    address_state: str = Column(String(255))
    address_country: str = Column(String(255))
    address_zip_code: str = Column(Integer)
    email: str = Column(String(255))
    account_creation_datetime: DateTime = Column(DateTime)
    # standard data warehouse metadata → best practices for data governance
    dwh_created_date: Date = Column(DateTime, index=True)
    dwh_update_date: DateTime = Column(DateTime, index=True)
    dwh_table_name: str = Column(String(255))
    dwh_primary_key: str = Column(String(255))
