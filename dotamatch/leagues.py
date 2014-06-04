from dotamatch.api import Api


class LeagueListing(Api):
    url = "https://api.steampowered.com/IDOTA2Match_570/GetLeagueListing/v0001/"

    def leagues(self, **kwargs):
        result = self._get(**kwargs)
        for league in result['result']['leagues']:
            yield League(**league)


class League(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)