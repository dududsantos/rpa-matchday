from client import get_matches
from filter import filter_matches
from formatter import format_matches
from settings import FAV_COMPETITIONS, FAV_TEAMS
from datetime import date
from settings import API_KEY

current_date = date.today().isoformat()


matches = get_matches(
    current_date,
)

filtered_matches = filter_matches(
    matches["matches"],
    FAV_TEAMS,
    FAV_COMPETITIONS
)

message = format_matches(filtered_matches)

print(message)