# Esempio di nuova classe

class Quadrato:  # definizione di una classe

    def __init__(self, lato):  # costruttore per l’inizializzazione di un oggetto
        self.lato = lato

    def __repr__(self):  # rappresentazione di un oggetto
        return "Quadrato(", self.lato, ")"


# Parametro self

class Quadrato:  # definizione di una classe

    def __init__(self, lato):  # costruttore per l’inizializzazione di un oggetto
        self.lato = lato

    def __repr__(self):  # rappresentazione di un oggetto
        return "Quadrato(", self.lato, ")"

    def perimetro(self):  # funzioni accessorie
        return self.lato * 4

    def area(self):
        return self.lato * self.lato


# Variabili di istanza vs variabili di classe

class Car:
    wheels = 4  # <- Class variable

    def __init__(self, name):
        self.name = name  # <- Instance variable
