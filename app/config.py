import os
from dotenv import load_dotenv

load_dotenv(encoding="utf-8-sig")

CORS_ORIGINS = [
    origin.strip()
    for origin in os.getenv("CORS_ORIGINS", "").split(",")
    if origin.strip()
]
