def imprimir_parametros(*args, **kwargs):
    for i in args:
        print(i)
        
    for chave, valor in kwargs.items():
        print(valor)
        
imprimir_parametros(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
