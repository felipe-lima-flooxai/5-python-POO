import ex_heranca as contas
import ex_heranca2 as pessoas

class Banco:
    def __init__(self, agencias: list[int] | None=None, 
                 clientes: list[pessoas.Pessoa] | None =None, 
                 contas: list[contas.Conta] | None =None):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            return True
        return False

    def _checa_conta(self, conta):
        if conta.conta in self.contas:
            return True
        return False
    
    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            return True
        return False

    def autenticar(self, cliente: pessoas.Pessoa, conta: contas.Conta):
        return self._checha_agencia(conta) and self._checa_cliente(cliente) and self._checa_conta(conta)
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f"({self.agencias!r}, {self.clientes!r}, {self.contas!r})"
        return f"{class_name}{attrs}"
    

if __name__ == "__main__":
    c1 = pessoas.Cliente("Luiz", 30)
    cc1 = contas.ContaCorrente(111, 222, 0 ,0)
    c1.conta = cc1
    c2 = pessoas.Cliente("Maria", 18)
    cp1 = contas.ContaPoupanca(112, 223, 100)
    c2.conta = cp1
    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1, cp1])
    banco.agencias.extend([111, 222])
    print(banco.autenticar(c1, cp1))
    print(banco)