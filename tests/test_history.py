import json
import os.path
import mock
import unittest
from dotamatch import history

fixtures_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'fixtures')
)


class TestMatchHistoryBySequenceNum(unittest.TestCase):
    @mock.patch('dotamatch.history.MatchHistoryBySequenceNum._get')
    @mock.patch('dotamatch.players.PlayerSummaries._get')
    def test_match_details(self, player_summaries_get, match_details_get):
        with open(os.path.join(fixtures_path, 'match_history_by_sequence_num.json')) as f:
            match_details_get.return_value = json.load(f)
        with open(os.path.join(fixtures_path, 'player_summaries.json')) as f:
            player_summaries_get.return_value = json.load(f)


        api = history.MatchHistoryBySequenceNum('testkey')
        matches = api.matches()

        self.assertEqual(7, matches.next().match_id)
