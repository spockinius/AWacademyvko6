import requests

tiedosto = requests.get("https://raw.githubusercontent.com/LearnWebCode/json-example/master/animals-1.json")

data = tiedosto.json()

for i in data:
    if i["name"] == "Purrpaws":
        print(i["name"], i["foods"]["likes"], i["foods"]["dislikes"])
