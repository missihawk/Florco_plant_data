from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    TCP_PORT = int(os.getenv("TCP_PORT", 4000))
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = int(os.getenv("DB_PORT", 5432))