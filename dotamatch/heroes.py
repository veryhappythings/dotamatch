from dotamatch.api import CachedApi


class Heroes(CachedApi):
    url = "https://api.steampowered.com/IEconDOTA2_570/GetHeroes/v0001/?"

    def heroes(self):
        results = self._get()
        heroes = {}
        for result in results['result']['heroes']:
            heroes[result['id']] = Hero(result['id'], result['name'])
        return heroes


class Hero(object):
    def __init__(self, id_, name):
        self.id_ = id_
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
