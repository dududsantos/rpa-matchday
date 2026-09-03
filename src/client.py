import logging
import requests
from src.settings import API_KEY, API_URL

logger = logging.getLogger(__name__)


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

    try:
        response = requests.get(
            API_URL,
            headers=headers,
            params=params,
            timeout=30
        )
        response.raise_for_status()
        return response.json()

    except requests.HTTPError as error:
        logger.exception(
            "Erro HTTP %s ao buscar jogos para %s na API %s. Resposta: %s",
            error.response.status_code,
            date,
            API_URL,
            error.response.text,
        )
        raise
    except (requests.RequestException, ValueError):
        logger.exception("Erro ao buscar jogos para %s na API %s", date, API_URL)
        raise


