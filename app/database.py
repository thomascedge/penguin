from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine

from .env import MYSQL_USERNAME, MYSQL_PASSWORD

# get username and password from env

DATABASE_NAME = 'fetch'
DATABASE_URL = f"mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@localhost:3306/{DATABASE_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
