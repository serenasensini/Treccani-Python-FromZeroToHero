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


class Studente:

    def __init__(self, nome, cognome, matricola, esami, cfu=0):
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola
        self.cfu = cfu
        self.esami = esami

    def __repr__(self):
        print("Dati anagrafici", self.nome, self.cognome)
        print("Matricola", self.matricola)
        print("Crediti attuali", self.cfu)
        print("Esami sostenuti", self.esami)

    def get_nome(self):
        return self.nome

    def set_nome(self, nuovo_nome):
        self.nome = nuovo_nome

    def get_cognome(self):
        return self.cognome

    def set_cognome(self, nuovo_cognome):
        self.cognome = nuovo_cognome

    def get_anagrafica(self):
        return self.nome, self.cognome

    def get_cfu(self):
        return self.cfu

    def set_cfu(self, crediti_esame):
        self.cfu += crediti_esame

    def sostieni_esame(self, nuovo_esame):
        self.esami.append(nuovo_esame)

mario_rossi = Studente("Mario", "Rossi", 1003123, [], 0)

# mario_rossi.__repr__()

mario_rossi.sostieni_esame("Analisi I")
mario_rossi.set_cfu(12)

cognome = mario_rossi.get_cognome()
print(cognome)
# mario_rossi.__repr__()