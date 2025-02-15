import os
from dotenv import load_dotenv

load_dotenv()

class Config: 
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    # Note the 4 slashes - sqlite:////absolute/path/to/database.db
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'database.db')}"
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev')
    SQLALCHEMY_TRACK_MODIFICATIONS = False