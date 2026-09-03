import unittest
from unittest.mock import Mock, patch

from src.client import get_matches


class GetMatchesTests(unittest.TestCase):
    @patch("src.client.requests.get")
    def test_get_matches_uses_date_range_params_for_single_day(self, mock_get):
        response = Mock()
        response.raise_for_status.return_value = None
        response.json.return_value = {"matches": []}
        mock_get.return_value = response

        result = get_matches("2026-09-03", api_key="token")

        self.assertEqual(result, {"matches": []})
        mock_get.assert_called_once_with(
            "https://api.football-data.org/v4/matches",
            headers={"X-Auth-Token": "token"},
            params={"dateFrom": "2026-09-03", "dateTo": "2026-09-03"},
            timeout=30,
        )


if __name__ == "__main__":
    unittest.main()
