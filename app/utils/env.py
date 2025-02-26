import os
from dotenv import load_dotenv


"""
Get environment variables from system. If variables are not present, you can
create a .env file at the root of this project with your env variables listed
as <NAME>="<CONTENT>".
"""
load_dotenv()

OPEN_API_KEY = os.getenv('OPENAI_API_KEY')
MONGO_DB_USERNAME = os.getenv('MONGO_DB_USERNAME')
MONGO_DB_PASSWORD = os.getenv('MONGO_DB_PASSWORD')
