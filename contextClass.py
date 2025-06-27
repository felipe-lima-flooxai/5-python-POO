class Arquivo:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def __enter__(self):
        self.file = open(self.path, self.mode, encoding="utf-8")
        return self.file

    #tirando self, os outros 3 valores são sobre o caso de haver erro. 
    #python preenche automaticamente
    def __exit__(self, type, value, traceback):
        self.file.close()

with Arquivo("exemplo.txt", "w") as f:
    f.write("Usando context manager com classe")