import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM", "HS256")

    DATABASE_URL = os.getenv("DATABASE_URL")
    if not DATABASE_URL:
        raise ValueError("❌ DATABASE_URL is not set! Please export it or add it to .env")

    MODEL_URL = os.getenv("MODEL_URL")
    if not MODEL_URL:
        raise ValueError("❌ MODEL_URL is not set! Please export it or add it to .env")

    MODEL_FILENAME = os.getenv("MODEL_FILENAME", "granite-3.1-2b-instruct-IQ4_XS.gguf")


config = Config()
