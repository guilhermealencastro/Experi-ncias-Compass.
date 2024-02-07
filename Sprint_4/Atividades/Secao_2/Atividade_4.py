def calcular_valor_maximo(operadores, operandos) -> float:
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '%': lambda x, y: x % y
    }

    resultados = map(lambda tup: operations[tup[0]](*tup[1]), zip(operadores, operandos))

    return max(resultados)
