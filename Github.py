import requests
import json

def get_git_repos_and_commits(UserID):
    #checks to see if user ID is a string
    if not isinstance(UserID, str):
        return "User ID must be a string"
    
    API_repos_URL = "https://api.github.com/users/" + UserID + "/repos"
    API_commits_URL = "https://api.github.com/repos/" + UserID + "/"
    result = []
    response = requests.get(API_repos_URL)
    #checks with GitHub if user ID is valid
    if response.status_code != 200:
        return "Invalid UserID"
    #appends results to array
    for repo in response.json():
        response = requests.get(API_commits_URL + repo["name"] + "/commits").json()
        result.append((repo["name"], len(response)))
    return result

print(get_git_repos_and_commits("mikemoreedu"))
