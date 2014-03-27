try:
    from urllib import urlencode
except ImportError:
    # Python 3
    from urllib.parse import urlencode
import time
import datetime
import requests


class ApiError(Exception):
    pass


class Api(object):
    time_between_requests = datetime.timedelta(seconds=1)
    time_of_last_request = datetime.datetime.min

    url = "You must override the URL in your API!"

    def __init__(self, key):
        self.key = key

    def _get(self, **kwargs):
        if datetime.datetime.utcnow() - Api.time_of_last_request < Api.time_between_requests:
            time.sleep((datetime.datetime.utcnow() - Api.time_of_last_request).total_seconds())
        Api.time_of_last_request = datetime.datetime.utcnow()

        kwargs['key'] = self.key

        args = urlencode(kwargs)
        response = requests.get(type(self).url + args)
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
