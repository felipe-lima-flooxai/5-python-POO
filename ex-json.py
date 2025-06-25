import json

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

with open("pessoa.json", "w", encoding="utf-8") as f:
    json.dump(pedro.__dict__, f, indent=4)