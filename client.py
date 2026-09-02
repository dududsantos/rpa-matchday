import requests
from settings import API_KEY, API_URL

def get_matches(date, api_key=None):
    api_key = api_key or API_KEY

    if not api_key:
        raise ValueError(
            "API_KEY não está definida."
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


