import random

random_list = random.sample(range(500), 50)
random_list.sort()

tamanho = len(random_list)

if tamanho % 2 == 1:
    mediana = random_list[ (tamanho-1) //2 ]
else:
    mediana =(random_list[tamanho // 2-1] + random_list[tamanho // 2]) /2
    
media = sum (random_list)/len(random_list)

valor_minimo = min(random_list)

valor_maximo = max(random_list)

print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}')