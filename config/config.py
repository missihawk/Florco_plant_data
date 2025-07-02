from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    # Connection configuration
    TCP_HOST = os.getenv("TCP_HOST", "192.168.174.251")
    TCP_PORT = int(os.getenv("TCP_PORT", 4000))

    # Database configuration
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = int(os.getenv("DB_PORT", 5432))