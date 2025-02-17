# src/exec.py

import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from funcs import get_server_count

if __name__ == "__main__":
    game_id = input("enter script (gameid)")
    server_count = get_server_count(game_id)
    
    if server_count is not None:
        print(f"Number of servers for game ID {game_id}: {server_count}")
    else:
        print("Failed to retrieve server count.")
