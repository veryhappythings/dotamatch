import datetime
from dotamatch.api import Api
from dotamatch.players import Player


class MatchDetails(Api):
    url = "https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/?"

    def match(self, match_id):
        return Match(**self._get(match_id=match_id)['result'])


class Match(object):
    def __init__(self, **kwargs):
        self.players = []

        for key, value in kwargs.items():
            setattr(self, key, value)

        #players = []
        #for player in self.players:
        #    players.append(Player(**player))
        #self.players = players

        # TODO convert to date time
        self.start_time = kwargs.get('start_time', datetime.datetime.utcnow())

    def player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player
        return None


