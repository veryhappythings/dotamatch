from dotamatch import api

class PlayerSummaries(api.CachedApi):
    url = "https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?"

    def player(self, account_id):
        # This is the placeholder ID for private players
        if account_id == 4294967295:
            return None
        # Convert the 32-bit ID into 64-bit
        result = self._get(steamids=int(account_id) + 76561197960265728)
        return Player(**result['response']['players'][0])


class Player(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        return unicode(self.personaname).encode('utf-8')

    def __unicode__(self):
        return self.personaname
