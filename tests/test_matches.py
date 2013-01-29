import json
import os.path
import mock
import unittest
from dotamatch import matches

fixtures_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'fixtures')
)


class TestMatches(unittest.TestCase):
    @mock.patch('requests.get')
    def test_match_details(self, get):
        response = get.return_value
        response.status_code = 200
        with open(os.path.join(fixtures_path, 'match_details.json')) as f:
            response.json.return_value = json.load(f)

        api = matches.MatchDetails('testkey')
        match = api.match(111145518)

        self.assertEqual(111145518, match.match_id)
