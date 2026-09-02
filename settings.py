import os
from dotenv import load_dotenv


load_dotenv()

API_URL = os.getenv("API_URL", "https://api.football-data.org/v4/matches")
API_KEY = os.getenv("API_KEY", "")

__all__ = ["API_URL", "API_KEY"]

FAV_COMPETITIONS = [
    2013, #Brasileirao
    2021, #Premier League
    2001, #Champions League
]

#Só coloquei times que não estão inseridos nas competições favoritas, pois por enqunato não tem um uso específico p/ times favoritos. 
FAV_TEAMS = [
    98, #Milan
    108, #Inter
    113, #Napoli
    5, #Bayern
    86, #Real Madrid
]