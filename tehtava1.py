
import statistics
import math

numerolista = input("Anna numerolista: ")

lista = numerolista.split(",")

uusi_lista = []

for luku in lista:
    uusi_lista.append(float(luku))


print(uusi_lista)

min = min(uusi_lista)
max = max(uusi_lista)
miini = statistics.mean(uusi_lista)
mediaani = statistics.median(uusi_lista)

print(min, max, miini, mediaani)

