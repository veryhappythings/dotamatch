from dotamatch import get_key
from dotamatch.history import MatchHistory
from dotamatch.matches import MatchDetails
from dotamatch.players import PlayerSummaries
from dotamatch.heroes import Heroes

key = get_key()
history = MatchHistory(key)
player_summaries = PlayerSummaries(key)
details = MatchDetails(key)
heroes = Heroes(key)

tidehunter_id = 29

for match in history.matches(skill=3, hero_id=tidehunter_id):
    match = details.match(match.match_id)
    for player in [p for p in match.players if p['hero_id'] == tidehunter_id]:
        for i in range(6):
            print 'item_{0}'.format(i), player['item_{0}'.format(i)]

