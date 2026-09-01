import os
from dotenv import load_dotenv


load_dotenv()

API_URL = os.getenv("API_URL", "https://api.football-data.org/v4/matches")
API_KEY = os.getenv("API_KEY", "")

__all__ = ["API_URL", "API_KEY"]
