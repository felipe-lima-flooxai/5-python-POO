class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"{self.nome}, {self.idade} anos"

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso

    def apresentar(self):
        base = super().apresentar()
        return f"{base} - Curso: {self.curso}"

p = Pessoa("João", 40)
a = Aluno("Maria", 22, "Engenharia")

print(p.apresentar())
print(a.apresentar())