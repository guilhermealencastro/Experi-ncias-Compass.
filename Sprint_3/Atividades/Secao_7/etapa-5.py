def ler_csv(arquivo):
    linhas = []
    with open(arquivo, 'r') as arq:
        for linha in arq:
            linha = linha.strip()
            campos = linha.split(',')
            linhas.append(campos)
    return linhas


caminho = r'C:\Desafio_Python\Actors.csv'
dados = ler_csv(caminho)
substring = [linha for linha in dados[1:]]

atores_faturamento = {}
for c in range(0, len(substring)):
    if substring[c][0] == '"Robert Downey':
        ator = (substring[c][0].strip() + substring[c][1].strip()).replace('"', '')
        faturamento = float(substring[c][2].strip())
    else:
        ator = substring[c][0].strip()
        faturamento = float(substring[c][1].strip())

    try:
        faturamento_bruto = float(faturamento)
    except ValueError:
        faturamento_bruto = 0.0

    atores_faturamento[ator] = atores_faturamento.get(ator, 0.0) + faturamento

atores_ordenados = sorted(atores_faturamento.items(), key=lambda x: x[1], reverse=True)

print("Lista dos atores ordenada pelo faturamento bruto total, em ordem decrescente:")

for ator, faturamento_total in atores_ordenados:
    print(f"{ator}: {faturamento_total:.2f}")

txt = r'C:\Users\Guilherme\Documents\Compass\Sprint_3\Atividades\Secao_7\etapa-5.txt'
with open(txt, 'w') as resp:
    resp.write("Lista dos atores ordenada pelo faturamento bruto total, em ordem decrescente:\n")
    for ator, faturamento_total in atores_ordenados:
        resp.write(f"{ator}: {faturamento_total:.2f}\n")
