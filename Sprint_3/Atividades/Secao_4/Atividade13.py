def my_map(lista, f):
    nova_lista = []
    for elemento in lista:
        resultado = f(elemento)
        nova_lista.append(resultado)
    return nova_lista


def potencia(x):
    return x ** 2


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = my_map(lista, potencia)
print(resultado)
