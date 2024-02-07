caminho = r'estudantes.csv'


def ler_csv(arquivo):
    estudantes = []

    with open(arquivo, 'r') as arq:
        for linha in arq:
            linha = linha.strip().split(',')
            nome = linha[0]
            notas = list(map(int, linha[1:]))
            estudantes.append((nome, notas))

    return estudantes


dados = ler_csv(caminho)
dados_ordenados = sorted(dados, key=lambda x: x[0])


def calcular_media(lista):
    a = sorted(lista, reverse=True)[:3]
    media = sum(a) / len(a)
    return round(media, 2)


resposta = list(map(lambda x: f'Nome: {x[0]} Notas: {sorted(x[1], reverse=True)[:3]} Média: {calcular_media(x[1])}', dados_ordenados))

for c in resposta:
    print(c)
