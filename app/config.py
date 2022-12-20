import os

from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv('DB_NAME')
HOST = os.getenv('HOST')
USER = os.getenv('USER')
PORT = os.getenv('PORT')
PASSWORD = os.getenv('PASSWORD')

SECRET_KEY = os.getenv('SECRET_KEY')
