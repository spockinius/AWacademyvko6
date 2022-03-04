import requests

tiedosto = requests.get("https://api.github.com/search/repositories?q=language:python")

data = tiedosto.json()

# print(data['items'][0]['name'])
# käy läpi items-listassa olevat dictit, i=dict, [key]

for i in data['items']:
    print(f"{i['forks']}:{i['name']}:{i['description']}")

