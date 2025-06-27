from enum import Enum

class Cor(Enum):
    VERMELHO = 1
    VERDE = 2
    AZUL = 3
    AMARELO = 4

print(Cor.VERMELHO)
print(Cor.VERMELHO.name)
print(Cor.VERMELHO.value)

for cor in Cor:
    print(f"{cor.name} = {cor.value}")