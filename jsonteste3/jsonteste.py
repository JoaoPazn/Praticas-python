import json

# Carregar o arquivo JSON
with open('jsonteste2.json', 'r') as f:
    data = json.load(f)

# Acessar a lista de nomes
nomes = data["Nomes"]

print(nomes)