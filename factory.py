class Pessoa:
    def __init__(self, name, age, size):
        self.name = name
        self.age = age
        self.size = size

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getSize(self):
        return self.size
    
    @classmethod
    def newborn(cls, name, size):
        return cls(name, 0, size)
    

pedro = Pessoa("Pedro", 21, 1.75)
guilherme = Pessoa.newborn("Guilherme", 0.3)
gabriel = pedro.newborn("Gabriel", 0.4)

print(pedro)
print("Nome do pedro: ", pedro.getName())
print("Idade do pedro: ", pedro.getAge())
print("Tamanho do pedro: ", pedro.getSize())
print(guilherme)
print(guilherme.name)
print(guilherme.age)
print(guilherme.size)
print(gabriel)
print(gabriel.name)
print(gabriel.age)
print(gabriel.size)