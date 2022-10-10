# Ciclo for

for i in [1, 3, 5, 7]:
    print(i)

# Ciclo while

countdown = 10
while countdown <= 0:
    print(countdown)
    countdown = countdown + 1

# Funzione range

for i in range(1, 10):
    print(i)

for i in range(1, 10, 2):
    print(i)

# Esempio con due argomenti
for i in range(-1, 5):
    print(i, end=", ")  # restituiti: -1, 0, 1, 2, 3, 4,
