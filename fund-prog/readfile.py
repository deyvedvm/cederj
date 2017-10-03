dados = open("arquivo.txt", "r")

linha = dados.readline()

while linha != "":
    print(linha, end="")

    linha = dados.readline()

dados.close()

# Escrevendo no Arquivo

dados = open("arquivo.txt", "a")

dados.write("linha 3\n")

dados.close()

# Exemplo com o For

print("Usando o for...")

dados = open("arquivo.txt", "r")

for linha in dados:
    print(linha, end="")

dados.close()

print("Outro exemplo")

dados = open("arquivo.txt", "r")

print(dados.readlines())
