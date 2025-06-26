
#eu poderia ter feito com classe abstrata também, mas assim é mais simples
class Funcionario:
    def trabalho(self):
        return "Trabalha em tarefas genéricas"

class Programador(Funcionario):
    def trabalho(self):
        return "Escreve código"

class Designer(Funcionario):
    def trabalho(self):
        return "Cria interfaces"

def mostrar_trabalho(funcionario):
    print(funcionario.trabalho())

f1 = Programador()
f2 = Designer()

mostrar_trabalho(f1)
mostrar_trabalho(f2)