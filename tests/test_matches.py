import json
import os.path
import mock
import unittest
from dotamatch import matches

fixtures_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'fixtures')
)


class TestMatches(unittest.TestCase):
    @mock.patch('dotamatch.matches.MatchDetails._get')
    @mock.patch('dotamatch.players.PlayerSummaries._get')
    def test_match_details(self, player_summaries_get, match_details_get):
        with open(os.path.join(fixtures_path, 'match_details.json')) as f:
            match_details_get.return_value = json.load(f)
        with open(os.path.join(fixtures_path, 'player_summaries.json')) as f:
            player_summaries_get.return_value = json.load(f)


        api = matches.MatchDetails('testkey')
        match = api.match(111145518)

        self.assertEqual(111145518, match.match_id)
