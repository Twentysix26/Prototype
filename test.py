import requests

URL = "https://api.github.com/orgs/Cog-Creators/repos"
data = requests.get(URL)

print(data.json())
