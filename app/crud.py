from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from datetime import datetime
from typing import Any

from .model import Receipt, ReceiptData, User, UserData
from .utils import Calculator, IDGenerator

"""
Receipt object creation, read, update, and delete functions
TODO: delete and update function
"""
def get_receipt(db: Session, receipt_id: str) -> ReceiptData:
    return db.query(ReceiptData).filter(ReceiptData.receipt_id == receipt_id).first()

def create_receipt(db: Session, user_id: int, receipt: Receipt, receipt_id: str) -> None:
    # data preprocessing
    receipt_id = IDGenerator().create_receipt_id()
    points, message = Calculator.calculate(receipt)
    items = ''.join(str(item) for item in receipt.items)

    # prints point calculation breakdown to terminal
    print(message)

    to_db = ReceiptData(
        receipt_id=receipt_id, 
        user_id=user_id,
        receipt_entry_date=datetime.today(),
        receipt_retailer=receipt.retailer,
        receipt_purchase_date=receipt.purchase_date,
        receipt_purchase_time=receipt.purchase_time,
        receipt_total=receipt.total,
        receipt_items=items,
        points=points,
        points_breakdown=message,
        dwh_created_date=datetime.now(),
        dwh_update_date=datetime.now(),
        dwh_table_name='receipt_data',
        dwh_primary_key='receipt_id, user_id'
    )

    db.add(to_db)
    db.commit()
    db.refresh(to_db)


"""
User object creation, read, update, and delete functions
TODO: delete and update function
"""
def get_user(db: Session, user_id: int) -> UserData:
    return db.query(UserData).filter(User.user_id == user_id).first()

def create_user(db: Session, user: User, user_id: int) -> None:
    to_db = User(
        user_id=user_id,
        name=user.name,
        age=user.age,
        birthday=user.birthday,
        address_street=user.address_street,
        address_state=user.address_state,
        address_country=user.address_country,
        address_zip_code=user.address_zip_code,
        email=user.email,
        account_creation_datetime=datetime.now(),
        dwh_created_date=datetime.now(),
        dwh_update_date=datetime.now(),
        dwh_table_name='receipt_data',
        dwh_primary_key='user_id'
    )

    db.add(to_db)
    db.commit()
    db.refresh(to_db)

"""
General functions
"""
def delete(db: Session, data_item: Any) -> None:
    db.delete(data_item)
    db.commit()

def update(db: Session, data_item: Any) -> None:
    db.commit()
    db.refresh(data_item)