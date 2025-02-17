# luac.py

import requests

def get_server_count(game_id):
    url = f"https://games.roblox.com/v1/games/{game_id}/servers/Public?sortOrder=Asc&limit=100"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        
        data = response.json()
        server_count = len(data.get('data', []))
        
        return server_count
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
