#seguiiiiiinte
#pedi pra IA preencher o código com docstrings pra mim
#não sei se gostei tanto de docstring pra documentar o código não.
#Por mais que eu goste de comentar códigos, desse jeito ficou MUITO grande desnecessariamente;

class Conta:
    """
    Representa uma conta bancária genérica.

    Atributos:
        titular (str): Nome do dono da conta.
        saldo (float): Saldo atual da conta.
    """

    def __init__(self, titular, saldo=0):
        """
        Inicializa a conta com um titular e saldo opcional.

        Args:
            titular (str): Nome do titular.
            saldo (float): Saldo inicial da conta (padrão: 0).
        """
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        """
        Adiciona dinheiro à conta.

        Args:
            valor (float): Valor a ser depositado.
        """
        self.saldo += valor

    def sacar(self, valor):
        """
        Remove dinheiro da conta se houver saldo suficiente.

        Args:
            valor (float): Valor a ser sacado.

        Returns:
            bool: True se o saque foi realizado, False caso contrário.
        """
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        return False

    def obter_saldo(self):
        """Retorna o saldo atual da conta."""
        return self.saldo


class ContaCorrente(Conta):
    """
    Representa uma conta corrente com limite de cheque especial.

    Atributos adicionais:
        limite (float): Valor do limite extra disponível.
    """

    def __init__(self, titular, saldo=0, limite=500):
        """
        Inicializa uma conta corrente.

        Args:
            titular (str): Nome do titular.
            saldo (float): Saldo inicial.
            limite (float): Limite do cheque especial.
        """
        super().__init__(titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        """
        Realiza saque utilizando saldo e limite, se necessário.

        Args:
            valor (float): Valor a ser sacado.

        Returns:
            bool: True se o saque foi realizado, False caso contrário.
        """
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            return True
        return False


# Exemplo de uso
conta = ContaCorrente("Felipe", saldo=1000, limite=300)
print(f"Saldo: {conta.obter_saldo()}")

conta.sacar(1200)
print(f"Saldo após saque: {conta.obter_saldo()}")

conta.depositar(500)
print(f"Saldo após depósito: {conta.obter_saldo()}")
