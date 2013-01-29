import mock
import unittest
from dotamatch import api


class DotDict(dict):
    def __getattr__(self, attr):
        return self.get(attr, None)
    __setattr__= dict.__setitem__
    __delattr__= dict.__delitem__


class TestCachedApi(unittest.TestCase):
    @mock.patch('requests.get')
    def test_cache(self, get):
        response = get.return_value
        response.status_code = 200
        cached_api = api.CachedApi('testkey')

        cached_api._get()
        self.assertTrue(get.called)
        get.reset_mock()
        cached_api._get()
        self.assertFalse(get.called)
