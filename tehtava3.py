
""" with open("harjoitus.txt", "w") as tiedosto:
    elaimet = ["Kissa", "Lehma", "Koiro", "Vuohi", "Kukko", "Lepakko", "Leopardi"]
    tiedosto.write('\n'.join(elaimet)) """

with open("harjoitus.txt", "r") as tiedosto:
    uusi_lista = []
    for rivi in tiedosto:
        rivi = rivi.replace("\n", "")
        uusi_lista.append(rivi)
    sortattu = sorted(uusi_lista)
    print(sortattu)
    string = ""
    for i in sortattu:
        string += i
        string += " "
    print(string)
        

with open("harjoitus.txt") as i:
    with open("uusiharjoitus.txt", "w") as o:
        o.write(string)

