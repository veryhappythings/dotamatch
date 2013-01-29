"""
Source for most info: http://dev.dota2.com/showthread.php?t=58317
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
    for player in match.players:
        details = player_summaries.player(player['account_id'])
        if details and details.personaname == 'Maccy':
            hero = heroes.heroes()[player['hero_id']].name
            heroes_played[hero] = heroes_played.get(hero, 0) + 1

pprint.pprint(heroes_played)
