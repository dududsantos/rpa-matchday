def filter_matches(matches, fav_teams, fav_competitions):
    filtered_matches = []

    for match in matches:
        competition_id = match["competition"]["id"]

        home_team_id = match["homeTeam"]["id"]
        away_team_id = match["awayTeam"]["id"]

        is_favorite_competition = (
            competition_id in fav_competitions
        )

        is_favorite_team = (
            home_team_id in fav_teams
            or away_team_id in fav_teams
        )

        if is_favorite_competition or is_favorite_team:
            filtered_matches.append(match)

    return filtered_matches