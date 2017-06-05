# Exemplo de Escrita e Leitura de Registros
import struct

SIZE = 43


def write(file, matricula, nome, cr):
    file.write(matricula.encode("utf-8"))
    file.write(nome[:30].ljust(30, chr(0)).encode("utf-8"))
    file.write(struct.pack("f", cr))


def read(file):
    matricula = file.read(9).decode("utf-8")
    nome = file.read(30).decode("utf-8").rstrip(chr(0))
    cr = struct.unpack("f", file.read(4))[0]

    return matricula, nome, cr


with open("file.bin", "w+b") as file:
    write(file, '213031001', 'Gustavo', 8.5)
    write(file, '114031012', 'Dayana', 8.3)
    write(file, '214031173', 'Deyve', 10.0)

    file.seek(2 * SIZE)

    matricula, nome, cr = read(file)

    print("Matricula: {}, nome: {}, CR: {}".format(matricula, nome, cr))
