import os.path


def get_key():
    key_path = os.path.expanduser("~/.steamapi")
    if os.path.exists(key_path):
        with open(key_path, 'r') as f:
            key = f.read().strip()
    else:
        try:
            key = raw_input("Enter Steam API key: ")
        except NameError:
            # Python 3
            key = input("Enter Steam API key: ")
    return key


class Dota(object):
    def __init__(self, key):
        self.key = key
        self.economy = Economy(key)
        self.heroes = Heroes(key)
        self.match_history = MatchHistory(key)
        self.match_history_by_sequence_num = MatchHistoryBySequenceNum(key)
        self.league_listing = LeagueListing(key)
        self.match_details = MatchDetails(key)
        self.player_summaries = PlayerSummaries(key)
        self.resolve_vanity_url = ResolveVanityUrl(key)
        self.teams = Teams(key)


from .economy import Economy
from .heroes import Heroes
from .history import MatchHistory, MatchHistoryBySequenceNum
from .leagues import LeagueListing
from .matches import MatchDetails
from .players import PlayerSummaries, ResolveVanityUrl
from .teams import Teams
