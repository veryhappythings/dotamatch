import json
import os.path
import mock
import unittest
from dotamatch import teams

fixtures_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'fixtures')
)


class TestTeams(unittest.TestCase):
    @mock.patch('dotamatch.teams.Teams._get')
    def test_match_details(self, teams_get):
        with open(os.path.join(fixtures_path, 'teams.json')) as f:
            teams_get.return_value = json.load(f)

        api = teams.Teams('testkey')
        team_list = api.teams()
        self.assertEqual(team_list[0].name, 'Zenith')
