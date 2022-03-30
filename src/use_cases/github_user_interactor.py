"""example usecase class implementation"""
import requests

class GitHubUserInteractor:
    """This is just example"""

    def __init__(self):
        pass

    def get_user_information(self):
        r = requests.get("https://api.github.com/users/defunkt")
        print(r.json())
