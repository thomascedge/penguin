from typing import Annotated
from fastapi import FastAPI, HTTPException, Depends, Query
from sqlalchemy.orm import Session

from .utils import Calculator, IDGenerator
from .model import Receipt, ReceiptData, User, UserData
from .database import SessionLocal, engine, Base

from .crud import *

app = FastAPI()
calculator = Calculator()

# create tables for database
Base.metadata.create_all(bind=engine)

# dependnecy to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()


# endpoints and api calls
@app.post('/user')
async def create_user(user: User, db: Session = Depends(get_db)) -> dict:
    user_id = IDGenerator().create_user_id()
    create_user(db, user, user_id)

    return {'user_id': user_id, 'message': f'Welcome {user.name}!'}

@app.get('/user/{user_id}')
async def get_user(user_id: int, db: Session = Depends(get_db)) -> dict:
    """
    A simple Getter endpoint that looks up a user by the ID and returns an object 
    specifying the points awarded.
    """
    data = get_user(db, user_id)

    if not data:
        raise HTTPException(status_code=404, detail=f'No user for id, {user_id}')
    return {'user': data}

@app.put('/user/{user_id}')
async def update_user(user_id: int, db: Session = Depends(get_db), **kwargs: dict):
    """
    Function that finds a user's id and updates any field specified in the 
    new_data parameter.

    May need to use __getattribute__ 
    Make user params optional, use **kwargs to access them

    TODO: implement
    """
    data = db.query(UserData).filter(UserData.user_id == user_id).first()
    
    if data is None:
        raise HTTPException(status_code=404, detail=f"No user for id, {user_id}")
    
    for field, updated_value in kwargs.items():
        data.__dict__.update({field: updated_value})
        # user = data.copy(update={field: updated_value}) if above line does not work
        
    update(db, data)
    
    return {'user_id': user_id, 'message': 'User information successfully updated.'}

@app.get('user/{user_id}/receipts/{receipt_id}')
async def process_receipts(user_id: int, receipt_id: str, db: Session = Depends(get_db)) -> dict:
    """
    
    """
    data = get_receipt(db, user_id)

    # raises 404 error when a receipt id cannot be found
    if not data:
        raise HTTPException(status_code=404, detail=f'No receipt for id, {receipt_id}, for that user.')

    return {'receipt': data}

@app.post('/user/{user_id}/receipts/process')
async def get_points(user_id: int, receipt: Receipt, db: Session = Depends(get_db)) -> dict:
    """
    A simple Getter endpoint that looks up the receipt by the ID and returns an object 
    specifying the points awarded.

    NOTE: automatically raises a 422 error if any Receipt field is missing or wrong type

    { "points": 32 }
    """    
    # error handeling in case no items in reciept
    if len(receipt.items) == 0:
        raise HTTPException(status_code=400, detail=f'Items list empty. Please ensure items are populated.')

    # create ID for receipt
    receipt_id = IDGenerator().create_id()
    
    # calculate points and add to database
    create_receipt(db, user_id, receipt, receipt_id)

    return {'id': receipt_id}

@app.delete('/user/{user_id}/receipts/{receipt_id}')
def delete_receipt(user_id: int, receipt_id: str, db: Session = Depends(get_db)):
    """
    Deletes a record for a given receipt id.
    """
    data = db.query(ReceiptData).filter(ReceiptData.receipt_id == receipt_id).first()

    if not data:
        raise HTTPException(status_code=404, detail=f"No receipt found for id, {id}.")
    
    delete(db, data)
    return {'message': 'Receipt successfully deleted.'}
    

@app.get('/user/{user_id}/receipts')
def read_receipts(user_id: int, db: Session = Depends(get_db), limit: int = 100) -> dict:
    """
    Getter function to get all receipts for a given user.

    TODO: implement
    """
    pass


"""
Could add other endpoints for new user creation, taking input from a frontend
like name, age, birthday, address, email, and create a unique id (numbers only)
that corresponds to a receipt and points

Use int(uuid.uuid4()) for interger 


Points could later be aggregated and totaled for analytics

SQL queries: https://www.atlassian.com/data/notebook/how-to-execute-raw-sql-in-sqlalchemy

FastAPI with SQLAlchemy: Building Scalable APIs with a Database Backend: https://medium.com/@suganthi2496/fastapi-with-sqlalchemy-building-scalable-apis-with-a-database-backend-7ccc9aa659a1
Dockerizing FastAPI and PostgreSQL Effortless Containerization: A Step-by-Step Guide: https://medium.com/@kevinkoech265/dockerizing-fastapi-and-postgresql-effortless-containerization-a-step-by-step-guide-68b962c3e7eb
"""