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

atores_faturamento = {}
atores_filmes = {}

for c in range(1, len(dados)):
    ator = dados[c][0].strip('"')
    faturamento_bruto = dados[c][1].replace(",", "").strip()
    numero_filmes = int(dados[c][2].replace(".", "").strip())

    try:
        faturamento_bruto = float(faturamento_bruto)
    except ValueError:
        faturamento_bruto = 0.0

    atores_faturamento[ator] = atores_faturamento.get(ator, 0.0) + faturamento_bruto
    atores_filmes[ator] = atores_filmes.get(ator, 0) + numero_filmes

media_faturamento_por_ator = {}
for ator in atores_faturamento:
    media_faturamento_por_ator[ator] = atores_faturamento[ator] / atores_filmes[ator]

ator_maior_media = max(media_faturamento_por_ator, key=media_faturamento_por_ator.get)
maior_media = media_faturamento_por_ator[ator_maior_media]

print(f"O ator/atriz com a maior média de faturamento por filme é {ator_maior_media} com uma média de {maior_media:.2f}.")

txt = r'C:\Users\Guilherme\Documents\Compass\Sprint_3\Atividades\Secao_7\etapa-3.txt'
with open(txt, 'w') as resp:
    resp.write(f"O ator/atriz com a maior média de faturamento por filme é {ator_maior_media} com uma média de {maior_media:.2f}.")