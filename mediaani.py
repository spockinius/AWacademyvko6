import statistics
import math

luku = input("Anna luku: ")

uusi_luku = luku.split(",")
lista = []
for i in uusi_luku:
    lista.append(float(i))
print(lista)

mediaani = statistics.mode(lista)

print(mediaani)