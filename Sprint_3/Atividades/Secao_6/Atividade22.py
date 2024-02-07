class Pessoa:
    def __init__(self, identificador):
        self.id = identificador
        self.__nome = ""

    def nome(self):
        return self.__nome

    def nome1(self, valor):
        self.__nome = valor


pessoa = Pessoa(0)
pessoa.nome = 'Alguém'
print(pessoa.nome)
