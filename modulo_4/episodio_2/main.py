# raise

x = input("Inserisci un numero")

if not type(x) is int:
    raise TypeError("Sono ammessi solo numeri interi")

    # Eccezioni: come gestile

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
finally:
    print("Execution ended")