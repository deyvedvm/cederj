# Exemplo de escrita em arquivo binário

# Escrita de um valor inteiro e um ponto flutuante com precisão dupla

import struct

try:
    with open("file.bin", "wb") as file:

        package = struct.pack("i", 10)
        file.write(package)

        package = struct.pack("d", 99.5)
        file.write(package)
except IOError:
    print("Error while open file")
