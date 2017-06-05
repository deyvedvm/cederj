# Exemplo de Escrita e Leitura de Registros
import struct

Aluno = struct.Struct("9s 30s f")  # Criar Struct com o formato do registro


def write(file, matricula, nome, cr):
    block = Aluno.pack(matricula.encode("utf-8"), nome.encode("utf-8"), cr)
    file.write(block)


def read(file):

    block = file.read(Aluno.size)
    fields = Aluno.unpack(block)

    return fields[0], fields[1].decode("utf-8").rstrip(chr(0)), fields[2]


with open("file.bin", "w+b") as file:
    write(file, '213031001', 'Gustavo', 8.5)
    write(file, '114031012', 'Dayana', 8.3)
    write(file, '214031173', 'Deyve', 10.0)

    file.seek(2 * Aluno.size)

    matricula, nome, cr = read(file)

    print("Matricula: {}, nome: {}, CR: {}".format(matricula, nome, cr))
