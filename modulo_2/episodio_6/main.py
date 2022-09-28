# Ripasso

def divisibiliPerCinque(lista):
    for element in lista:
        if element % 5 == 0:
            print(element)

print(divisibiliPerCinque([10,12,15,20]))
