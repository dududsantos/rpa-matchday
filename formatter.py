from datetime import datetime
from zoneinfo import ZoneInfo


def format_matches(matches):
    message = "Oi Dudu, esses são os Jogos de hoje ⚽:\n\n"

    for match in matches:
        home_team = match["homeTeam"]["shortName"]
        away_team = match["awayTeam"]["shortName"]
        competition = match["competition"]["name"]

        utc_date = datetime.fromisoformat(
            match["utcDate"].replace("Z", "+00:00")
        )

        brazil_date = utc_date.astimezone(
            ZoneInfo("America/Sao_Paulo")
        )

        time = brazil_date.strftime("%H:%M")

        message += f"🕐 {time} - {home_team} x {away_team}\n"
        message += f"🏆 {competition}\n\n"

    return message