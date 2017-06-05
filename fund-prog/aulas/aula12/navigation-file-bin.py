# Exemplos de Navegação em Arquivo Binário

# Verificando o tamanho do arquivo

try:
    with open("file.bin", "rb") as file:
        file.seek(0, 2)
        size = file.tell()
        print("O arquivo possui {} bytes".format(size))
except IOError:
    print("Error while open file")
