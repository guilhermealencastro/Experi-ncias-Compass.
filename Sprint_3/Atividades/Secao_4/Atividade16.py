def somar(string_numeros):
    numeros = string_numeros.split(',')
    soma = 0
    for numero in numeros:
        soma += int(numero)
    return soma
    
string_numeros = "1,3,4,6,10,76"
resultado = somar(string_numeros)
print(resultado)