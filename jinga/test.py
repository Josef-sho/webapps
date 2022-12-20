import requests

data = requests.get(f"https://api.agify.io?name=michael")
print(data.json()['age'])