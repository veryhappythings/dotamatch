from dotamatch import api

class Teams(api.CachedApi):
    url = "https://api.steampowered.com/IDOTA2Match_570/GetTeamInfoByTeamID/v001/?"

    def teams(self, **kwargs):
        """Return a list of teams.

        Available options are:
        start_at_team_id  # the ID of the team to start at
        teams_requested   # the number of teams to return (default is 100)
        """

        result = self._get(**kwargs)
        return [Team(**t) for t in result['result']['teams']]


class Team(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        return unicode(self.name).encode('utf-8')

    def __unicode__(self):
        return self.name
