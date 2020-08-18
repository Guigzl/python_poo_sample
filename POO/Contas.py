from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, conta, agencia, saldo):
        self.conta = conta
        self.agencia = agencia
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        self.extrato()

    def extrato(self):
        print(
            f"Agencia: {self.agencia} "
            f"Conta: {self.conta} "
            f"Seu saldo é de R${self.saldo} ")

    @abstractmethod
    def saque(self, valor):
        pass


class ContaCorrente(Conta):
    def __init__(self, conta, agencia, saldo, limite=500):
        super().__init__(conta, agencia, saldo)
        self.limite = limite

    def saque(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo insuficiente')
            return
        self.saldo -= valor
        self.extrato()


class ContaPoupanca(Conta):
    def saque(self, valor):
        if self.saldo <= 0 or self.saldo < valor:
            print("saldo insuficiente")
            return
        self.saldo -= valor
        self.extrato()
