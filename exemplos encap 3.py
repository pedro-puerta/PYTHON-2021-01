class ContaBancaria:
    def __init__(self, numero, titular, senha):
        # atributos publicos
        self.numero = numero
        self.titular = titular
        # atributo privados
        self.__senha = senha
        self.__saldo = 0

    def get_saldo(self, senha):
        if senha == self.__senha:
            return self.__saldo
        else:
            print('Senha invalida')

    def depositar(self, valor, senha):
        if senha == self.__senha:
            self.__saldo += valor
        else:
            print('Senha invalida')

    def sacar(self, valor, senha):
        if senha == self.__senha:
            self.__saldo -= valor
        else:
            print('Senha invalida')


# cria objeto conta
conta = ContaBancaria(123, 'Francisco', 123456)

print('Numero da conta: ', conta.numero)
print('Titular da Conta: ', conta.titular)
# print('Senha da Conta:', conta.__senha)

valor = float(input('Valor do deposito:'))
senha = int(input('Informe a senha para fazer o depósito: '))
conta.depositar(valor, senha)

senha = int(input('Informe a senha para verificar o saldo: '))
print('Saldo da Conta:', conta.get_saldo(senha))
