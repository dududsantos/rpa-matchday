import requests

from src.settings import CALLMEBOT_API_KEY, WHATSAPP_PHONE


API_URL = "https://api.callmebot.com/whatsapp.php"


def send_message(message):
    params = {
        "phone": WHATSAPP_PHONE,
        "apikey": CALLMEBOT_API_KEY,
        "text": message
    }

    response = requests.get(
        API_URL,
        params=params
    )

    return response.text