"""
Source for most info: http://dev.dota2.com/showthread.php?t=58317
"""
from dotamatch import get_key
from dotamatch.history import MatchHistory
from dotamatch.matches import MatchDetails

key = get_key()
history = MatchHistory(key)
for match in history.matches(player_name='Maccy'):
    print match
    print match.player('Maccy').hero
