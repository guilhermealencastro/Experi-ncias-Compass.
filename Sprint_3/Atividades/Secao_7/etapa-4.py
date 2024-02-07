def ler_csv(arquivo):
    linhas = []
    with open(arquivo, 'r') as arq:
        for linha in arq:
            linha = linha.strip()
            campos = [campo.strip() for campo in linha.split(',')]
            linhas.append(campos)
    return linhas


caminho = r'C:\Desafio_Python\Actors.csv'
dados = ler_csv(caminho)
substring = [linha for linha in dados[1:]]

filmes_frequencia = {}
for c in range(len(substring)):
    if substring[c][0] == '"Robert Downey':
        filme = substring[c][5].strip()
    else:
        filme = substring[c][4].strip()
    if filme not in filmes_frequencia:
        filmes_frequencia[filme] = 0
    filmes_frequencia[filme] += 1

maior_frequencia = max(filmes_frequencia.values())

filmes_mais_frequentes = []
for filme, frequencia in filmes_frequencia.items():
    if frequencia == maior_frequencia:
        filmes_mais_frequentes.append(filme)


print("O(s) filme(s) mais frequente(s) e sua respectiva frequência:")
for filme in filmes_mais_frequentes:
    print(f"{filme}: {maior_frequencia}")

    txt = r'C:\Users\Guilherme\Documents\Compass\Sprint_3\Atividades\Secao_7\etapa-4.txt'
with open(txt, 'w') as resp:
    resp.write(f"{filme}: {maior_frequencia}")
