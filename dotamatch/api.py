import urllib
import requests


class ApiError(Exception):
    pass


class Api(object):
    url = "You must override the URL in your API!"

    def __init__(self, key):
        self.key = key

    def _get(self, **kwargs):
        kwargs['key'] = self.key

        args = urllib.urlencode(kwargs)
        response = requests.get(type(self).url + args)
        print response.status_code
        if response.status_code == 200:
            return response.json()
        else:
            raise ApiError(str(response.status_code) + ': ' + type(self).url + args)


class CachedApi(Api):
    cache = {}
    def _get(self, **kwargs):
        key = hash(tuple(kwargs.items()))
        if key not in type(self).cache:
            type(self).cache[key] = super(CachedApi, self)._get(**kwargs)
        return type(self).cache[key]
