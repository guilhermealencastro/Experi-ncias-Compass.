import hashlib

while True:
    input_string = input("Digite uma string para gerar o hash (ou 'sair' para encerrar): ")

    if input_string.lower() == "sair":
        break

    sha1_hash = hashlib.sha1(input_string.encode()).hexdigest()
    print("Hash SHA-1 da string:", sha1_hash)
