cupcake = open("data/cupcake.txt", "r")
# contenuto = cupcake.read()
# print(contenuto)
contenuto = cupcake.readlines()
print(contenuto)

dolci = []
# per ogni riga del file...
for linea in contenuto:
    # separo le singole parole della riga...
    parole = linea.split()
    # .. e le aggiungo alla lista usando il metodo extend()
    dolci.extend(parole)
print(dolci)
