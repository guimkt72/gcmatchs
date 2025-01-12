import pandas as pd
import requests 
import json 

url = 'https://gamersclub.com.br/lobby/match/22697838/1'
request = requests.get(url)
request_response = request.text
data = json.loads(request_response)

# Extract players data from both teams
team_a = data['jogos']['players']['team_a']
team_b = data['jogos']['players']['team_b']

# Combine both teams' data
all_players = team_a + team_b

# Define the columns we want to extract
columns = [
    'updated_at',     # Game date
    'player_room',    # Team identifier (a or b)
    'nb_kill',        # Kills
    'assist',         # Assists
    'death',          # Deaths
    'hs',             # Headshots
    'damage',         # Total damage
    'adr',            # Average damage per round
    'kdr',            # Kill/Death ratio
    'phs',            # Headshot percentage
    'firstkill',      # First kills
    'pkast',          # KAST percentage
    'nb1kill',        # 1 kill rounds
    'nb2kill',        # 2 kill rounds
    'nb3kill',        # 3 kill rounds
    'nb4kill',        # 4 kill rounds
    'nb5kill',        # 5 kill rounds
    'defuse',         # Bomb defuses
    'bombe',          # Bomb plants
    'hits',           # Total hits
    'level',          # Player level
    'rating',         # Player rating
    'flash_assist',   # Flash assists
    'multikills'      # Multi-kill rounds
]

# Create a list to store player data
players_data = []

# Extract data for each player
for player in all_players:
    player_dict = {
        'nick': player['player']['nick'],  # Player nickname
        'team': 'Team A' if player['player_room'] == 'a' else 'Team B'
    }
    
    # Add stats from the columns list
    for col in columns:
        player_dict[col] = player[col]
    
    players_data.append(player_dict)

# Create DataFrame
df = pd.DataFrame(players_data)

# Convert numeric columns
numeric_columns = [
    'nb_kill', 'assist', 'death', 'hs', 'damage', 'firstkill',
    'nb1kill', 'nb2kill', 'nb3kill', 'nb4kill', 'nb5kill',
    'defuse', 'bombe', 'hits', 'level', 'rating', 
    'flash_assist', 'multikills'
]
df[numeric_columns] = df[numeric_columns].astype(int)

# Convert percentage columns
percentage_columns = ['adr', 'kdr', 'phs', 'pkast']
df[percentage_columns] = df[percentage_columns].astype(float)

print(df['updated_at'])

# Convert date column
df['updated_at'] = pd.to_datetime(df['updated_at'])

# Display the DataFrame
print(df)


#df.to_excel('data1.xlsx')

