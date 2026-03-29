import requests

API_KEY = 'W4rtREUctjtHVswA08U0hStPDHhQEQs+rSE/7y4cTWZzsP1viJYypF/zdr9TK9wU'
BASE_URL = "https://api.collegebasketballdata.com"
headers = {'Authorization': f'Bearer {API_KEY}', 'accept': 'application/json'}

def get_games(season, week=None):
    """Get games for a season"""
    params = {'season': season}
    if week:
        params['week'] = week
    response = requests.get(f"{BASE_URL}/games", headers=headers, params=params)
    return response.json() if response.status_code == 200 else []

def get_game_players(game_id):
    """Get player stats for a specific game"""
    response = requests.get(f"{BASE_URL}/games/players", headers=headers, params={'gameId': game_id})
    return response.json() if response.status_code == 200 else []

# Get all games from a recent date
games = get_games(season=2025)

for game in games[:3]:  # First 3 games
    print(f"\n{game.get('homeTeam')} vs {game.get('awayTeam')}")
    print(f"Game ID: {game.get('id')}")
    print(f"Date: {game.get('date')}")
    
    # Get player stats for this game
    players = get_game_players(game.get('id'))
    
    if players:
        print("\nTop scorers:")
        # Sort by points (assuming the data structure includes points)
        sorted_players = sorted(players, key=lambda x: x.get('points', 0), reverse=True)
        for player in sorted_players[:5]:
            print(f"  {player.get('player', {}).get('name')}: {player.get('points', 0)} pts, {player.get('rebounds', 0)} reb, {player.get('assists', 0)} ast")
        
