import unittest
import Github
from unittest.mock import MagicMock, patch

class github_test(unittest.TestCase):
    @patch('Github.requests')
    def test_valid_output(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"name": "SSW567CircleCI", "commits": 9},
            {"name": "Triangle567", "commits": 5}
        ]
        mock_requests.get.return_value = mock_response
        self.assertEqual(Github.get_git_repos_and_commits("mikemoreedu"), [('SSW567CircleCI', 9), ('Triangle567', 5)])

    #def test_bad_input(self):
     #   self.assertEqual(Github.get_git_repos_and_commits(1), "User ID must be a string")
    
    #def test_UserID(self):
     #   self.assertEqual(Github.get_git_repos_and_commits("notmikemoreedu"), "Invalid UserID")
if __name__ == '__main__':
    print('Performing unit tests...')
    unittest.main()
