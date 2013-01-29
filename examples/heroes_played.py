"""
This example shows how you could count up the heroes used by a player.
It also highlights the problem with using player name instead of account
ID.
"""
import pprint
from dotamatch import get_key
from dotamatch.history import MatchHistory
from dotamatch.players import PlayerSummaries
from dotamatch.heroes import Heroes

key = get_key()
history = MatchHistory(key)
player_summaries = PlayerSummaries(key)
heroes = Heroes(key)

heroes_played = {}
for match in history.matches(player_name='Maccy'):
    player = match.player('Maccy')
    if player:
        hero = heroes.heroes()[player['hero_id']].name
        heroes_played[hero] = heroes_played.get(hero, 0) + 1

pprint.pprint(heroes_played)

print
print '------------'
print

heroes_played = {}
for match in history.matches(account_id='507891'):
    player = match.player('Maccy')
    if player:
        hero = heroes.heroes()[player['hero_id']].name
        heroes_played[hero] = heroes_played.get(hero, 0) + 1

pprint.pprint(heroes_played)
