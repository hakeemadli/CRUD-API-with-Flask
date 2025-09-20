import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    JWT_PRIVATE_KEY = os.getenv('JWT_PRIVATE_KEY')
    JWT_PUBLIC_KEY = os.getenv('JWT_PUBLIC_KEY')