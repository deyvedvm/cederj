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

# Main

quantidade_de_numeros = int(input())

numeros_lidos = []

for indice in range(quantidade_de_numeros):
    numeros_lidos.append(int(input()))

for indice in range(len(quantidade_de_numeros) - 1):
