class ErroPersonalizado(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)  

def dividir(a, b):
    if b == 0:
        raise ErroPersonalizado("Divisão por zero não permitida")
    return a / b

try:
    resultado = dividir(10, 0)
    print(resultado)
except ErroPersonalizado as e:
    print(f"Erro: {e}")

#okay, essa classe de erro é inutil, porém é a base pra criar erros proprios.