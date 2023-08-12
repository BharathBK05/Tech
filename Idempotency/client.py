import requests

params = {'uid': 1}
response = requests.get('https://localhost:8085/movies',
            params=params)
print(response.url)