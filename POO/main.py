from POO.cliente import Cliente
from POO.Contas import ContaCorrente, ContaPoupanca
from POO.Banco import Bancos

Inter = Bancos()

cliente402 = Cliente("Guilherminho", 28)
cliente302 = Cliente("Margaridinha", 54)

Conta402 = ContaPoupanca(7527, 3248, 50000)
Conta302 = ContaCorrente(5505, 3241, 0)

cliente302.inserir_conta(Conta302)
Inter.add_cliente(cliente302)
Inter.add_conta(Conta302)

if Inter.autenticar(cliente302):
    cliente302.conta.depositar(10000)

else:
    print("Cliente não autenticado")
