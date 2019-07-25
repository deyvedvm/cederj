# coding=utf-8
"""

A função fatorial duplo é definida como o produto de todos os números naturais ímpares de 1 até algum número natural
ímpar N. Por exemplo, se N é igual a 5 então o fatorial duplo de N é calculado como:

5!! = 1 × 3 × 5 = 15

Implemente um programa que recebe uma sequência de números naturais via entrada padrão e, para cada número ímpar N
informado, calcule seu fatorial duplo R e imprima a mensagem “O fatorial duplo de N é R”, onde N deve ser substituído
pelo número lido e R deve ser substituído pelo fatorial duplo calculado, conforme mostram os exemplos abaixo. Caso o
número natural N informado seja par, seu programa deverá imprimir a mensagem “O número N é par”, conforme mostram os
exemplos abaixo.

Um número N é dito natural se ele é inteiro positivo, incluindo o zero.

Restrição: Serão aceitos na correção apenas programas que calculam o fatorial duplo de N por meio de uma função
recursiva que atenda ao seguinte protótipo (sem variações):

def fatorial_duplo(n):
# Implemente essa função

"""


def fatorial_duplo(n):
    if n == 1:
        return 1
    else:
        return fatorial_duplo(n - 2) * n


while True:
    N = int(input())

    if N == -1:
        break

    if N % 2 == 0:
        print("O número {} é par".format(N))
        continue

    print("O fatorial duplo de {} é {}".format(N, fatorial_duplo(N)))
