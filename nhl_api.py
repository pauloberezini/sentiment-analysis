from nhlpy import NHLClient
import json

client = NHLClient()

def get_nhl_standings():
    response = client.standings.get_standings()

    # Initialize an empty JSON array
    json_array = []

    # Process the standings data
    for team in response['standings']:
        team_name = team['teamName']['default']
        games_played = team['gamesPlayed']
        goals_for = team['goalFor']
        goals_against = team['goalAgainst']
        
        homeGamesPlayed = team['homeGamesPlayed']
        homeGoalsFor = team['homeGoalsFor']
        homeGoalsAgainst = team['homeGoalsAgainst']
        
        roadGamesPlayed = team['roadGamesPlayed']
        roadGoalsFor = team['roadGoalsFor']
        roadGoalsAgainst = team['roadGoalsAgainst']
        
        # Calculate and round the averages
        #All games
        a_goals_average = round(goals_for / games_played, 2)
        a_losses_average = round(goals_against / games_played, 2)
        
        #Home games
        h_goals_average = round(homeGoalsFor / homeGamesPlayed, 2)
        h_losses_average = round(homeGoalsAgainst / homeGamesPlayed, 2)
        
        #Guest games
        g_goals_average = round(roadGoalsFor / roadGamesPlayed, 2)
        g_losses_average = round(roadGoalsAgainst / roadGamesPlayed, 2)

        # Create a JSON object for the team
        team_json = {
            "teamName": team_name,
            "gamesPlayed": games_played,
            "goalsFor": goals_for,
            "goalsAgainst": goals_against,
            "all" : {
                "goalsAverage": a_goals_average,
                "lossesAverage": a_losses_average
            },
            "home" : {
                "goalsAverage": h_goals_average,
                "lossesAverage": h_losses_average
            },
            "guest" : {
                "goalsAverage": g_goals_average,
                "lossesAverage": g_losses_average
            },
            
        }

        # Add the JSON object to the array
        json_array.append(team_json)
    return json_array