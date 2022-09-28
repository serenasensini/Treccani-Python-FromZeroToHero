# Funzioni

def hello():
    print("Hello world!")

hello()

# Funzioni built-in

#  integer number
integer = -20

absolute = abs(integer)

print('Absolute value of -40 is:', str(absolute))

# Parametri

def somma(a,b):
    return a + b

# Argomenti

risultato = somma(3, 2)
print(risultato)

# Argomenti di default
def greet(name, msg="Good morning!"):
    print("Hello", name + ', ' + msg)


greet("Kate")
greet("Bruce", "How do you do?")