class Conta:

    def __init__(self, conta='', agencia='',saldo=''):
        self.conta = conta
        self.agencia = agencia
        self.saldo = saldo

    def getConta(self):
        return self.conta

    def getAgencia(self):
        return self.agencia

    def getSaldo(self):
        return self.saldo

class PessoaFisica(Conta):

    def __init__(self, CPF, nome='', idade=''):
        Pessoa.__init__(self, nome, idade)
        self.CPF = CPF



class PessoaJuridica(Conta):

    def __init__(self, CNPJ, nome='', idade=0):
        Pessoa.__init__(self, nome, idade)
        self.CNPJ = CNPJ


a = Conta()
Conta.__init__(a, 'Leonardo', 22)

b = PessoaFisica('122.333.332-1', nome= '')
banco = PessoaJuridica('00.000.000/0001-11', nome='Banco do Brasil', idade=435)

print (a.conta)
print (a.agencia) # imprime 22
print (b.CPF)  # imprime 122.333.332-1
print (banco.CNPJ)  # imprime 00.000.000/0001-11