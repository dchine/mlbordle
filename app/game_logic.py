import csv
import random
from collections import OrderedDict

players = []
with open('./app/players/all-players.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    players = list(reader)[1:]
    player_names = [x['Name'] for x in players]

def get_player(name):
    player = [x for x in players if x['Name'].lower() == name.lower()]
    
    if player:
        player = player[0]
        return player
    else:
        return False

def get_new_answer():
    return random.choice(players)