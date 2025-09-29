import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    
    # DB config
    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_PORT = os.getenv("MYSQL_PORT")
    MYSQL_DB = 'crud_api_db'


    SQLALCHEMY_DB_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
    SQLALCHEMY_TRACK_MODIFIED = False