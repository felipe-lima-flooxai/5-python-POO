class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        return "Som de animal"

class Cachorro(Animal):
    def falar(self):
        return "Latido"

class Gato(Animal):
    def falar(self):
        return "Miado"

a = Animal("Bicho")
c = Cachorro("Totó")
g = Gato("Gatinho")

print(a.falar())
print(c.falar())
print(g.falar())