class Calculo:
    def somar(self, x, y):
        resultado = x + y
        return resultado

    def subtrair(self, x, y):
        resultado = x - y
        return resultado


calculo = Calculo()
x = 4
y = 5

soma = calculo.somar(x, y)
print("Somando: {}+{} = {}".format(x, y, soma))

subtracao = calculo.subtrair(x, y)
print("Subtraindo: {}-{} = {}".format(x, y, subtracao))
