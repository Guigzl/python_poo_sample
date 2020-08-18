class Bancos:
    def __init__(self):
        self.agencias = [3241, 3248, 3336]
        self.contas = []
        self.clientes = []

    def add_cliente(self, cliente):
        self.clientes.append(cliente)

    def add_conta(self, conta):
        self.contas.append(conta)

    def autenticar(self, cliente):
        if cliente not in self.clientes:
            return False

        if cliente.conta not in self.contas:
            return False

        if cliente.conta.agencia not in self.agencias:
            return False
        return True
