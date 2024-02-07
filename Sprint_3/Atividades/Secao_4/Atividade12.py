import json

with open('person.json') as arquivo:
    arquivo = json.load(arquivo)
            
print(arquivo)    