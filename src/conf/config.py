import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_URL = os.environ.get('SQLALCHEMY_DB') #"postgresql+asyncpg://postgres:postgres@10.185.110.242:5432/contacts_db"

config = Config