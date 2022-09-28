import sys
import random

# estrae un numero intero casuale tra 1 e 100
num_random = random.randint(1, 100)

user_input = int(input("Inserisci un numero tra 1 e 100: "))

flag = False

# Tentativo n.1 azzeccato...
if num_random == user_input:
    print("Hai indovinato!")
    flag = True
    sys.exit()

# ... altrimenti continua a giocare
while flag == False:
    user_input = int(input("Inserisci un numero tra 1 e 100: "))

    if user_input > num_random:
        print("Il numero è troppo alto! Ritenta")
    elif user_input < num_random:
        print("Il numero è troppo basso! Ritenta")
    else:
        print("Hai indovinato!")
        flag = True

