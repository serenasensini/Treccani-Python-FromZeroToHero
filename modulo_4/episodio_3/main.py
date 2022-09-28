# come importare i moduli

#import moduleName
# Importa tutto il modulo; un’alternativa è from moduleName import * (sconsigliata);

#from moduleName import function1, function2, …
# Dal modulo, importa le funzioni citate;

#import moduleName as m1
#Importa il modulo come oggetto m1;

# random

import random

numero_casuale = random.randint(0, 10)
# print(numero_casuale)

numero_random = random.random()
# print(numero_random)

# math
import math
x = 10
y = 3.2
print(math.factorial(x))
print(math.exp(x))
print(math.log(x))
print(math.pow(x,y))
print(math.sqrt(x))
print(math.pi)
print(math.inf)

# modulo interno
# file Cerchio.py

#file main.py
from Cerchio import Cerchio

c = Cerchio(3)
c.area_cerchio()