"""
A prefeitura da sua cidade resolveu lhe contratar para ajudar aos habitantes a localizarem qual a farmácia mais próxima,
através de um programa que processe arquivos contendo o posicionamento de todas as farmácias da sua cidade. Seu programa
deve dizer qual o posicionamento da farmácia mais próxima de um cidadão que execute o seu programa. Caso haja empate,
ele deve dizer o posicionamento de uma delas. O arquivo texto de nome “farmacias.txt”, fornecido pela prefeitura,
contém o posicionamento de todas as farmácias, onde cada linha possui dois números inteiros.

Entrada

Seu programa deve ler o posicionamento, isto é, as coordenadas XCidadao, YCidadao, de um cidadão.

Saída

Seu programa deve escrever a mensagem "Arquivo de Farmácias está vazio!!!", caso o arquivo lido esteja vazio. Caso
contrário, deve escrever na primeira linha a string “Local da Farmácia Mais Próxima: ”, seguida do posicionamento
XFarmacia, YFamacia que seja a mais próxima do cidadão, e a que distância ela se encontra. Na segunda linha deve
escrever a string “Distância à Percorrer: ”, seguida da menor distância encontrada.

Dica

A distância entre dois pontos, (X1, Y1) e (X2, Y2), é dada por sqrt((X1 - X2) 2 + (Y1 - Y2) 2 ).
"""


def distancia_entre_pontos(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


xCidadao, yCidadao = input().split()
xCidadao, yCidadao = int(xCidadao), int(yCidadao)

lista_de_farmacias = open("farmacias.txt")

farmacia = lista_de_farmacias.readline()

if farmacia == "":

    print("Arquivo de Farmácias está vazio!!!")
else:

    xFarmaciaMaisProxima, yFarmaciaMaisProxima = farmacia.split()
    xFarmaciaMaisProxima, yFarmaciaMaisProxima = int(xFarmaciaMaisProxima), int(yFarmaciaMaisProxima)

    menor_distancia = distancia_entre_pontos(xFarmaciaMaisProxima, yFarmaciaMaisProxima, xCidadao, yCidadao)

    for posicao_farmacia in lista_de_farmacias:

        xFarmacia, yFarmacia = posicao_farmacia.split()
        xFarmacia, yFarmacia = int(xFarmacia), int(yFarmacia)

        distancia_atual = distancia_entre_pontos(xFarmacia, yFarmacia, xCidadao, yCidadao)

        if distancia_atual < menor_distancia:
            menor_distancia = distancia_atual

            xFarmaciaMaisProxima, yFarmaciaMaisProxima = xFarmacia, yFarmacia

    print("Local da Farmácia Mais Próxima:", xFarmaciaMaisProxima, yFarmaciaMaisProxima)

    print("Distância à Percorrer:", menor_distancia)

lista_de_farmacias.close()
