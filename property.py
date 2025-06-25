class Carro:
    def __init__(self, name, brand, age):
        self._name = name
        self._brand = brand
        self._age = age

    @property
    def name(self):
        return self._name
    
    @property
    def brand(self):
        return self._brand
    
    @property
    def age(self):
        return self._age
    
    @name.setter
    def name(self, name):
        if(isinstance(name, str)):
            self._name = name
        else:
            print("Dado enviado não é uma string")
        
    @brand.setter
    def name(self, brand):
        if(isinstance(brand, str)):
            self._brand = brand
        else:
            print("Dado enviado não é uma string")

    @age.setter
    def age(self, age):
        if(isinstance(age, int)):
            self._age = age
        else:
            print("Dado enviado não é um inteiro")
    
corola = Carro("Corola", "Toyota", 2020)

print(corola.name)
print(corola.brand)
print(corola.age)

corola.name = 123
corola.name = True
corola.name = "SW4"
print(corola.name)