# Variabile

proverbio = "Rosso di sera, bel tempo si spera"

pigreco = 3.14

# Tipi di dato

quantita = 10
sito = 'https://theredcode.it'
prezzo = 1.99
flag = True
testo = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras ipsum nunc, tristique id risus a, tempor molestie nulla. Maecenas eget mauris ac nunc convallis aliquam. Aliquam lacinia blandit lectus, sit amet pulvinar nunc suscipit vulputate. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Nam convallis diam venenatis pharetra dictum.'

# Conversione implicita

x = 10

print("x is of type:", type(x))

y = 10.6
print("y is of type:", type(y))

x = x + y

print(x)
print("x is of type:", type(x))

# Conversione esplicita

n = "10010"
s = 'geeks'

c = tuple(s)
print(c)

e = float(n)
print(e)

c = str(s)
print(c)

# Tipizzazione dinamica

risultato = "Testo casuale"

risultato = 3  # OK

# Commenti

# Block comment

for i in range(0, 10):
    # Loop over i ten times and print out the value of i, followed by a
    # new line character
    print(i, '\n')

# Commento inline

x = 5  # This is an inline comment

# KO
x = 'John Smith'  # Student Name

# OK
std_dev = 'John Smith'  # Standard deviation


# Documentation string

def area(a, b):
    """Solve circle area via the formula.

    This calculation equation has the following form:
    a**2*3.14
    """
    ...