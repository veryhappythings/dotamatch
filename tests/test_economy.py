import json
import os.path
import mock
import unittest
from dotamatch import economy

fixtures_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'fixtures')
)


class TestEconomy(unittest.TestCase):
    @mock.patch('dotamatch.economy.Economy._get')
    def test_match_details(self, match_details_get):
        with open(os.path.join(fixtures_path, 'economy_en.json')) as f:
            match_details_get.return_value = json.load(f)


        api = economy.Economy('testkey')
        result = api.items(language='en')

        self.assertEqual(0, result['result']['qualities']['normal'])
