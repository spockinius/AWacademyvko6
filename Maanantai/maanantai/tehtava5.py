# tee linux kone, kirjaudu ssh-yhteydellä sisään, kirjoita crontab -e, valitse /bin/nano
# tee tekstitiedosto.txt ja pythontiedosto.py ( echo > tiedostonnimi.py)
# avaa nano pythontiedosto.py, kirjoita sinne alla oleva koodi, muokkaa tiedostonimet
# avaa crontab, kirjoita loppuun esim. * * * * * python3 /home/kata/pythontiedosto.py ja tallenna
# watch cat /home/kata/testtimes.txt
# nanon kautta voi pythontiedostoon laittaa myös esim. funktioita, esim health check


import datetime

now = datetime.datetime.now()
with open("testtimes.txt", "a") as file:
    file.write(str(now))
