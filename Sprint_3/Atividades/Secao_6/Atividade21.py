class Passaro:
    def voar(self):
        print("Voando...")

    def som(self):
        pass


class Pato(Passaro):
    def som(self):
        print("Quack Quack")


class Pardal(Passaro):
    def som(self):
        print("Piu Piu")


pato = Pato()
print("Pato")
pato.voar()
print("Pato emitindo som...")
pato.som()

pardal = Pardal()
print("Pardal")
pardal.voar()
print("Pardal emitindo som...")
pardal.som()
