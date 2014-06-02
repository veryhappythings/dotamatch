"""
This example fetches the player IDs from all the matches that an individual
player has played in.
"""
from dotamatch import get_key
from dotamatch.history import MatchHistory

key = get_key()
history = MatchHistory(key)

players = set()
for match in history.matches(account_id=507891):
    for player in match.players:
        players.add(player['account_id'])

print(players)
