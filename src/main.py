from src.client import get_matches
from src.filter import filter_matches
from src.formatter import format_matches
from src.settings import FAV_COMPETITIONS, FAV_TEAMS
from datetime import date
from src.settings import API_KEY
from src.notifier import send_message

current_date = date.today().isoformat()


matches = get_matches(
    current_date,
)

filtered_matches = filter_matches(
    matches["matches"],
    FAV_TEAMS,
    FAV_COMPETITIONS
)


if not filtered_matches:
    #print("Nenhum jogo encontrado.")
    exit()

message = format_matches(filtered_matches)

send_message(message)

print(message)