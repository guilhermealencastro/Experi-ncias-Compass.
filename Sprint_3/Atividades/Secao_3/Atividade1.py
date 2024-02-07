import datetime
nome = input("nome ")
idade = int(input("idade: "))

ano_atual = datetime.date.today().year

print((100 - idade) + ano_atual)

