# terminaaliin: PS C:\Users\katariina\Desktop\vko6\maanantai> #alkuu: python #tämä on tiedoston sijainti: .\tehtava4.1.py #nämä arvot annan: 2 6

import sys
  
  
print("This is the name of the program:",
       sys.argv[0])
print("First number:",
       sys.argv[1])
print("Second number:",
       sys.argv[2])

summalista = []
summalista.append(int(sys.argv[1]))
summalista.append(int(sys.argv[2]))

print(summalista)

print("Sum on numbers:",
       f"{sys.argv[1]} + {sys.argv[2]} = {sum(summalista)}")