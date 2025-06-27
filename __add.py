class Vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, outro):
        return Vetor(self.x + outro.x, self.y + outro.y)

    def __repr__(self):
        return f"Vetor({self.x}, {self.y})"

v1 = Vetor(2, 3)
v2 = Vetor(4, 1)
v3 = v1 + v2

print(v3)