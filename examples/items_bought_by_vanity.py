"""
This example fetches the last 10 matches of the specified vanity URL player, and prints which items that player
bought.
"""

from dotamatch import get_key
from dotamatch.players import ResolveVanityUrl, id_to_32
from dotamatch.history import MatchHistory, MatchDetails
import pprint

key = get_key()
history = MatchHistory(key)
match_details = MatchDetails(key)
id = ResolveVanityUrl(key).id('wek')
id_32 = id_to_32(id)

items = {}
for match in history.matches(account_id=id, matches_requested=10):
    details = match_details.match(match.match_id)
    player = details.player(id_32)
    for i in range(6):
        item_slot = 'item_' + str(i)
        try:
            items[player[item_slot]] += 1
        except KeyError:
            items[player[item_slot]] = 1

pprint.pprint(items)