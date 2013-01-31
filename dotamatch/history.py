from dotamatch.api import Api, ApiError
from dotamatch.matches import MatchDetails, Match


class MatchHistory(Api):
    url = "https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?"

    def __init__(self, key):
        super(MatchHistory, self).__init__(key)
        self.match_api = MatchDetails(key)

    def matches(self, **kwargs):
        """ Fetch match information.
        The available options are:
        player_name=<name>      # Search matches with a player name, exact match only
        hero_id=<id>            # Search for matches with a specific hero being played (hero ID, not name)
        skill=<skill>           # 0 for any, 1 for normal, 2 for high, 3 for very high skill (default is 0)
        date_min=<date>         # date in UTC seconds since Jan 1, 1970 (unix time format)
        date_max=<date>         # date in UTC seconds since Jan 1, 1970 (unix time format)
        account_id=<id>         # A user's 32-bit steam ID
        league_id=<id>          # matches for a particular league
        start_at_match_id=<id>      # Start the search at the indicated match id, descending
        matches_requested=<n>       # Maximum is 25 matches (default is 25)
        """
        result = self._get(**kwargs)
        for match in result['result']['matches']:
            try:
                yield self.match_api.match(match['match_id'])
            except ApiError:
                yield Match(self.match_api, **match)


class MatchHistoryBySequenceNum(Api):
    url = "http://api.steampowered.com/IDOTA2Match_205790/GetMatchHistoryBySequenceNum/v0001/?"

    def __init__(self, key):
        super(MatchHistoryBySequenceNum, self).__init__(key)
        self.match_api = MatchDetails(key)

    def matches(self, **kwargs):

        """ Fetch complete match information with fewer calls. Useful if
        you're grabbing all matches - not useful for much else.
        Returns 100 matches at a time.
        start_at_match_seq_num=seq_num
        """
        result = self._get(**kwargs)
        for match in result['result']['matches']:
            yield Match(self.match_api, **match)
