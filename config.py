import os
from dotenv import load_dotenv

load_dotenv()

class Config: 
    SQLALCHEMY_DATABASE_URI = "sqlite:///wmginvent.db"
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False