from functools import reduce


def calcula_saldo(lancamentos) -> float:
    get_value = lambda valor, tipo: valor if tipo == 'C' else -valor
    valores = map(lambda lancamento: get_value(*lancamento), lancamentos)
    saldo = reduce(lambda acc, valor: acc + valor, valores, 0)
    return saldo
