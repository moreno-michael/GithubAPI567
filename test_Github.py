import unittest
import Github

class github_test(unittest.TestCase):
    def test_Valid_output(self):
        self.assertEqual(Github.get_git_repos_and_commits("mikemoreedu"), [('SSW567CircleCI', 9), ('Triangle567', 5)])

    def test_bad_input(self):
        self.assertEqual(Github.get_git_repos_and_commits(1), "User ID must be a string")
    
    def test_UserID(self):
        self.assertEqual(Github.get_git_repos_and_commits("notmikemoreedu"), "Invalid UserID")
if __name__ == '__main__':
    print('Performing unit tests...')
    unittest.main()
