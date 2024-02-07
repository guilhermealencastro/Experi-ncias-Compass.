def ler_csv(arquivo):
    linhas = []
    with open(arquivo, 'r') as arq:
        for linha in arq:
            linha = linha.strip()
            campos = linha.strip(',')
            linhas.append(campos)
    return linhas


caminho = r'C:\Desafio_Python\Actors.csv'
dados = ler_csv(caminho)
substring = [string.split(',') for string in dados]

atores_faturamento = {}
atores_filmes = {}

for c in range(1, len(substring)):
    if substring[c][0] == '"Robert Downey':
        ator = (substring[c][0].strip() + substring[c][1].strip()).replace('"', '')
        faturamento = float(substring[c][2].strip())
        numero = int(substring[c][3].strip())
    else:
        ator = substring[c][0].strip()
        faturamento = float(substring[c][1].strip())
        numero = int(substring[c][2].strip())

    if ator not in atores_faturamento:
        atores_faturamento[ator] = {'faturamento_bruto': 0, 'atores_filmes': 0}

    atores_faturamento[ator]['faturamento_bruto'] += faturamento
    atores_faturamento[ator]['atores_filmes'] = numero

print("Média de faturamento por ator: ")

txt = r'C:\Users\Guilherme\Documents\Compass\Sprint_3\Atividades\Secao_7\etapa-2.txt'
with open(txt, 'w') as resp:
    for k, v in atores_faturamento.items():
        media = v['faturamento_bruto'] / v['atores_filmes']
        print(f'{k}: {media:.2f}')
        resp.write(f'{k}: {media:.2f}\n')
