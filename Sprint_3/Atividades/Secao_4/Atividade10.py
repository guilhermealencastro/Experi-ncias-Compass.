def remover_duplicatas(lista):
    return list(set(lista))

    
Original = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
lista_sem_duplicatas = remover_duplicatas(Original)

print(lista_sem_duplicatas)