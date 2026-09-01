import requests
from settings import API_KEY, API_URL



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


jogos = buscar_jogos(
    "2026-09-01",
    API_KEY
)

print(jogos)