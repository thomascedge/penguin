from dotenv import load_dotenv

import os

# get OpenAi API key from environment variable
load_dotenv()

OPEN_API_KEY = os.getenv('OPENAI_API_KEY')
MYSQL_USERNAME = os.getenv('MYSQL_USERNAME')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')