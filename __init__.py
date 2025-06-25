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
    

pedro = Pessoa("Pedro", 21, 1.75)

print(pedro)
print("Nome do pedro: ", pedro.getName())
print("Idade do pedro: ", pedro.getAge())
print("Tamanho do pedro: ", pedro.getSize())