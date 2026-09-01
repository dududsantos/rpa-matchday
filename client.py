import requests
from settings import API_KEY, API_URL
from datetime import date



def buscar_jogos(date, api_key=None):
    api_key = api_key or API_KEY

    if not api_key:
        raise ValueError(
            "API_KEY não está definida. Crie um arquivo .env com API_KEY=sua_chave."
        )

    headers = {
        "X-Auth-Token": api_key
    }

    params = {
        "date": date
    }

    response = requests.get(
        API_URL,
        headers=headers,
        params=params
    )

    return response.json()

current_date = date.today().isoformat()
jogos = buscar_jogos(
    current_date,
    API_KEY
)

#print(jogos)