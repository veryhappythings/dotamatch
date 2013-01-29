import datetime
from dotamatch.api import Api
from dotamatch.players import Player, PlayerSummaries


class MatchDetails(Api):
    url = "https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/?"

    def __init__(self, key):
        super(MatchDetails, self).__init__(key)
        self.player_summaries = PlayerSummaries(key)

    def match(self, match_id):
        return Match(self, **self._get(match_id=match_id)['result'])


class Match(object):
    def __init__(self, parent, **kwargs):
        self.parent = parent
        self.players = []

        for key, value in kwargs.items():
            setattr(self, key, value)


        for player in self.players:
            player['player'] = parent.player_summaries.player(
                player.get('account_id')
            )

        # TODO convert to date time
        self.start_time = kwargs.get('start_time', datetime.datetime.utcnow())

    def player(self, player_name):
        for player in self.players:
            if player['player'] and player['player'].personaname == player_name:
                return player
        return None


