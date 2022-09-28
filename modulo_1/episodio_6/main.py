# Operazioni di base

nome = "Marco"
saluto = "Ciao"

risultato = nome + saluto

risultato = nome + " " + saluto

# oppure

print(nome, " ", saluto)

s = 'cra.'
print(s*4)

suffisso = "ino"

personaggio = "Paperino"

print(suffisso in personaggio)

# Caratteri speciali

#txt = "Esiste una città chiamata "Perugia" dove ogni anno si svolge il festival del cioccolato." #KO

txt = "Esiste una città chiamata \"Perugia\" dove ogni anno si svolge il festival del cioccolato." # OK

print(txt)

directory = "\\la\\mia\\cartella"

print(directory)

print("Sempre caro \nmi fu quest'ermo colle")

# Funzioni per le stringhe

len(suffisso)

personaggio = "Paperino"

nuovo_personaggio = personaggio.replace("ino", "one")

print(nuovo_personaggio)

personaggio_maiuscolo = personaggio.upper()

print(personaggio_maiuscolo)

print(personaggio.istitle())

print(personaggio.islower())

# Conversioni

pigreco = 3.14

pigreco_str = str(3.14)

print(pigreco_str)

print(type(pigreco))

print(type(pigreco_str))
