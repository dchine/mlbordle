import csv
import random

players = []
with open('./players/all-players.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    players = list(reader)[1:]

def get_player(name):
    player = [x for x in players if x['Name'].lower() == name.lower()]
    if player:
        return player[0]
    else:
        return False

def get_new_answer():
    return random.choice(players)