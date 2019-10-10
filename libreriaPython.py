#questo programma ci fornisce 10 numeri casuali tra 1 e 50

import random
from math import sqrt

for numero in range(10):
    valore=random.randint(1,50)
    print(valore)

print("\nValore: " + str(valore))
k=sqrt(valore)
print("\nValore SQRT: " + str(k))
