import requests
import json
from datetime import datetime

#https://github.com/Zmalski/NHL-API-Reference?tab=readme-ov-file#get-standings
BASE_URL = "https://api-web.nhle.com/v1/"

def get_nhl_standings():
    url = f"{BASE_URL}standings/now"
    response = requests.get(url)
    
    if response.status_code != 200:
        return f"Error: {response.status_code}"

    data = response.json()

    # Initialize an empty JSON array
    json_array = []

    # Process the standings data
    for team_info in data['standings']:
        team_name = team_info['teamName']['default']
        games_played = team_info['gamesPlayed']
        goals_for = team_info['goalFor']
        goals_against = team_info['goalAgainst']
        
        home_games_played = team_info['homeGamesPlayed']
        home_goals_for = team_info['homeGoalsFor']
        home_goals_against = team_info['homeGoalsAgainst']
        
        road_games_played = team_info['roadGamesPlayed']
        road_goals_for = team_info['roadGoalsFor']
        road_goals_against = team_info['roadGoalsAgainst']
        
        # Check if games played is greater than zero to avoid division by zero
        all_goals_avg = round(goals_for / games_played, 2) if games_played > 0 else 0
        all_losses_avg = round(goals_against / games_played, 2) if games_played > 0 else 0
        
        home_goals_avg = round(home_goals_for / home_games_played, 2) if home_games_played > 0 else 0
        home_losses_avg = round(home_goals_against / home_games_played, 2) if home_games_played > 0 else 0
        
        road_goals_avg = round(road_goals_for / road_games_played, 2) if road_games_played > 0 else 0
        road_losses_avg = round(road_goals_against / road_games_played, 2) if road_games_played > 0 else 0

        # Create a JSON object for the team
        team_json = {
            "teamName": team_name,
            "gamesPlayed": games_played,
            "goalsFor": goals_for,
            "goalsAgainst": goals_against,
            "all": {
                "goalsAverage": all_goals_avg,
                "lossesAverage": all_losses_avg
            },
            "home": {
                "goalsAverage": home_goals_avg,
                "lossesAverage": home_losses_avg
            },
            "guest": {
                "goalsAverage": road_goals_avg,
                "lossesAverage": road_losses_avg
            }
        }

        # Add the JSON object to the array
        json_array.append(team_json)

    return json_array

# Call the function and print the result
# standings = get_nhl_standings()
# print(json.dumps(standings, indent=4))

def get_previous_nhl_standings():
    previous_date = get_previous_season_date()
    url = f"{BASE_URL}standings/{previous_date}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return f"Error: {response.status_code}"

    data = response.json()

    # Initialize an empty JSON array
    json_array = []

    # Process the standings data
    for team_info in data['standings']:
        team_name = team_info['teamName']['default']
        games_played = team_info['gamesPlayed']
        goals_for = team_info['goalFor']
        goals_against = team_info['goalAgainst']
        
        home_games_played = team_info['homeGamesPlayed']
        home_goals_for = team_info['homeGoalsFor']
        home_goals_against = team_info['homeGoalsAgainst']
        
        road_games_played = team_info['roadGamesPlayed']
        road_goals_for = team_info['roadGoalsFor']
        road_goals_against = team_info['roadGoalsAgainst']
        
        # Check if games played is greater than zero to avoid division by zero
        all_goals_avg = round(goals_for / games_played, 2) if games_played > 0 else 0
        all_losses_avg = round(goals_against / games_played, 2) if games_played > 0 else 0
        
        home_goals_avg = round(home_goals_for / home_games_played, 2) if home_games_played > 0 else 0
        home_losses_avg = round(home_goals_against / home_games_played, 2) if home_games_played > 0 else 0
        
        road_goals_avg = round(road_goals_for / road_games_played, 2) if road_games_played > 0 else 0
        road_losses_avg = round(road_goals_against / road_games_played, 2) if road_games_played > 0 else 0

        # Create a JSON object for the team
        team_json = {
            "teamName": team_name,
            "gamesPlayed": games_played,
            "goalsFor": goals_for,
            "goalsAgainst": goals_against,
            "all": {
                "goalsAverage": all_goals_avg,
                "lossesAverage": all_losses_avg
            },
            "home": {
                "goalsAverage": home_goals_avg,
                "lossesAverage": home_losses_avg
            },
            "guest": {
                "goalsAverage": road_goals_avg,
                "lossesAverage": road_losses_avg
            }
        }

        # Add the JSON object to the array
        json_array.append(team_json)

    return json_array

def get_previous_season_date():
    current_year = datetime.now().year
    # Если текущий месяц до октября, значит мы в межсезонье, берем предыдущий сезон
    if datetime.now().month < 10:
        previous_season_year = current_year - 1
    else:
        previous_season_year = current_year
    
    # Формируем дату конца предыдущего сезона
    previous_season_end_date = f"{previous_season_year}-04-18"
    print(f'last year standing {previous_season_end_date}')
    return previous_season_end_date

