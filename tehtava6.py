# tee vm, ota yhteys public ip osoitteeseen
# juokse: #!/bin/bash
# sudo apt update && sudo apt -y install apache2
# echo '<!doctype html><html><body><h1>Hello World!</h1></body></html>' | sudo tee /var/www/html/index.html
# echo '<!doctype html><html><body><h1>Healthy</h1></body></html>' | sudo tee /var/www/html/health.html

import requests

r = requests.get("http://52.157.11.89")

if r.status_code == 200:
    with open("health.txt", "a") as file:
        file.write("Kone on kunnossa" + "\n")
else:
    with open("health.txt", "a") as file:
        file.write("Kone on kaatunut" + "\n")


