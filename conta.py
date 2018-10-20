class Conta:
    def __init__(self,saldo,numero,agencia):
        saldo.self = 0
        numero.self = numero
        agencia.self = agencia

    def getSaldo(self):
        return self.saldo

    def getNumero(self):
        return self.numero

    def getAgencia(self):
        return self.agencia

    class Fisica:
        def __init__(self,cpf):
            Conta.__init__(self,saldo,numero,agencia)
            cpf.self = cpf
    class Juridica:
        def __init__(self,cnpj,empresa,idade):
            Conta.__init__(self,saldo,numero,agencia)
            cnpj.self = cnpj
            empresa.self = empresa
            idade.self = idade
a = Conta()
Conta.__init__(a,"5000","123456",019)

b = Fisica("05823917171","Vinicius",18)
banco = Juridica("123456789","Fiat",198)

print (a.numero)


