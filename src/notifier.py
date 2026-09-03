import logging

import requests

from src.settings import CALLMEBOT_API_KEY, WHATSAPP_PHONE


API_URL = "https://api.callmebot.com/whatsapp.php"
logger = logging.getLogger(__name__)


def send_message(message):
    params = {
        "phone": WHATSAPP_PHONE,
        "apikey": CALLMEBOT_API_KEY,
        "text": message
    }

    try:
        response = requests.get(
            API_URL,
            params=params,
            timeout=30
        )
        response.raise_for_status()
    except requests.RequestException:
        logger.exception("Erro ao enviar mensagem pelo CallMeBot")
        raise

    return response.text