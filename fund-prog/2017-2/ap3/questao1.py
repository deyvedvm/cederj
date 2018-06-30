# coding=utf-8
"""
Considerando a entrada de valores inteiros não negativos, ordene estes valores segundo o seguinte critério:

▪ Primeiro os múltiplos de 10
▪ Depois os demais números

Sendo que deverão ser apresentados os múltiplos de 10 em ordem crescente e depois os demais números em ordem
decrescente.

Entrada

A entrada é dada via entrada padrão. A primeira linha da entrada contém o número N > 0, que indica quantos números
compõe o conjunto de valores a serem ordenados. As N linhas seguintes contém os valores inteiros não negativos da
coleção, um por linha.

Saída

O resultado da ordenação deve ser escrito na saída padrão, colocando-se um valor por linha.

Restrição

Não é permitido utilizar rotinas prontas de ordenação disponíveis na API do Python. Logo, você deverá implementar
explicitamente um dos algoritmos de ordenação vistos em aula. Será atribuído 0 (zero) para soluções que fazem uso de
rotinas prontas de ordenação
"""


def ordena_numeros(numeros, ordem):
    ascendente = ordem

    for i in range(len(numeros)):
        pivo = i
        for j in range(i + 1, len(numeros)):
            if numeros[j] < numeros[pivo]:
                pivo = j
        numeros[i], numeros[pivo] = numeros[pivo], numeros[i]

    if ascendente:
        return numeros
    else:
        return numeros.reverse()


def imprime_numeros(numeros):
    for indice_local in range(len(numeros)):
        print(numeros[indice_local])


# Main

quantidade_de_numeros = int(input())

numero = 0

numeros_multiplos_10 = []

outros_numeros = []

for indice in range(quantidade_de_numeros):
    numero = int(input())

    if numero % 10 == 0:
        numeros_multiplos_10.append(numero)
    else:
        outros_numeros.append(numero)

ordena_numeros(numeros_multiplos_10, True)

ordena_numeros(outros_numeros, False)

imprime_numeros(numeros_multiplos_10)

imprime_numeros(outros_numeros)
