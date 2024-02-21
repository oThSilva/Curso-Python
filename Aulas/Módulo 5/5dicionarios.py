# Dicionario {Chave:valor}
dicionario_pessoa = {"Nome: ": "Th", "Idade: ": "18", "Altura: ": "1.70"}
print(dicionario_pessoa)
# outra maneira de criar dicionario

dicionario_2 = dict(nome="Th", Idade="24", altura="1.70")
print(dicionario_2)

# para acessar o valor de uma chave especifica
print(dicionario_pessoa["Altura: "])

# para ver todas as chaves de um dicionario
print(dicionario_pessoa.keys())

# para ver todos os valores de um dicionario
print(dicionario_pessoa.values())

# Para retornar em uma tupla dentro de uma lista as chaves e os valores de um dicionario
print(dicionario_pessoa.items())

# Iterar sobre um dicionarios

for item in dicionario_pessoa.values():
    print(item)
