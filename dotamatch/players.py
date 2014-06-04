from dotamatch import api

# Constant for converting 32-bit IDs into 64-bit and vice-versa
DIFF_64 = 76561197960265728


def id_to_64(account_id):
    """Safely converts id to 64-bit. If the id is already 64-bit, it will not be converted."""
    return account_id if account_id >= DIFF_64 else account_id + DIFF_64


def id_to_32(account_id):
    """Safely converts id to 32-bit. If the id is already 32-bit, it will not be converted."""
    return account_id if account_id < DIFF_64 else account_id - DIFF_64


class PlayerSummaries(api.CachedApi):
    url = "https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?"

    def players(self, *account_ids):
        ids = []
        for account_id in account_ids:
            # 4294967295 is the placeholder ID for private players
            if account_id is not None and account_id != 4294967295:
                # Converts ID to 64-bit if it is not already
                ids.append(id_to_64(account_id))
        result = self._get(steamids=','.join(ids))
        for player in result['response']['players']:
            yield Player(player)


class ResolveVanityUrl(api.CachedApi):
    url = "https://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?"

    def id(self, vanity_name):
        result = self._get(vanityurl=vanity_name)
        if result['response']['success'] == 1:
            return int(result['response']['steamid'])
        return None


class Player(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        try:
            return unicode(self.personaname).encode('utf-8')
        except NameError:
            # Python 3
            return self.personaname

    def __unicode__(self):
        return self.personaname
