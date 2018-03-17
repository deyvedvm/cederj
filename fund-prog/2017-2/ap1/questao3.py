"""

Faça um programa, contendo subprogramas, que:

a) Leia da entrada padrão as dimensões, quantidade de linhas e quantidade de colunas de uma matriz bidimensional;
b) Gere uma matriz, onde cada célula é um número inteiro gerado aleatoriamente no intervalo 0 a 9;
c) Mostre a matriz, linha a linha na tela;
d) Calcule e escreva a média de todos os valores na matriz;
e) Escreva o conteúdo de todas as linhas que possuam todos os seus valores acima da média calculada em (d).

Dica

Utilize a função random.randint(a, b), disponível na API, que retorna um número
randômico inteiro entre a e b, inclusive.

Restrição
Não serão aceitos na correção programas que utilizam o módulo numpy.

Entrada

Dois números inteiros positivos são lidos, representando respectivamente: a quantidade linhas L e quantidade de colunas
C da matriz a ser gerada.

Saída

Seu programa deverá emitir:

L linhas, com C inteiros cada linha, contendo valores no intervalo 0 e 9;
Uma linha em branco;
Uma linha com um número de ponto flutuante, representando a média solicitada;
Uma linha em branco;
Zero ou mais linhas contendo C inteiros, de cada linha com a propriedade pedida

"""

from random import randint


def gera_matriz(linhas, colunas):
    matrix = []

    for linha in range(linhas):

        linha = []

        for coluna in range(colunas):
            linha.append(randint(0, 9))

        matrix.append(linha)
    return matrix


def imprime_matriz(matriz):
    for linha in matriz:
        for coluna in linha:
            print(coluna, end=" ")
        print()
    print()


def media_da_matriz(matriz):
    total = 0.0

    for linha in matriz:
        for coluna in linha:
            total += coluna
    return total / (len(matriz) * len(matriz[0]))


def imprive_valores_acima_da_media(matriz, media):
    for linha in matriz:
        for coluna in linha:
            if coluna > media:
                print(coluna, end=" ")


quantidade_linhas, quantidade_colunas = input().split()

matriz_gerada = gera_matriz(int(quantidade_linhas), int(quantidade_colunas))

imprime_matriz(matriz_gerada)

media_da_matriz = media_da_matriz(matriz_gerada)

print(media_da_matriz)

print()

imprive_valores_acima_da_media(matriz_gerada, media_da_matriz)
