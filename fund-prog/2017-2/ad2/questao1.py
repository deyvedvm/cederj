"""
Faça um programa que represente dois polinômios, p(x) e q(x), definidos pelo usuário.

Produza e escreva a soma dos dois polinômios lidos, onde soma(x) = p(x)+q(x), e a multiplicação dos dois polinômios
lidos, onde multiplica(x) = p(x)*q(x). Suponha que os polinômios tenham coeficientes que sejam números em ponto
flutuante e os graus sejam inteiros, o coeficiente de grau maior deve ser lido antes.

Entrada

Na primeira linha devem ser escritos todos os coeficientes do primeiro polinômio, separados por espaços em branco. Na
segunda linha devem ser escritos todos os coeficientes do segundo polinômio, separados por espaços em branco.

Saída

Na primeira linha deve ser escrita a string “Coeficientes do Polinômio Soma: ”, seguida dos coeficientes calculados;
Na segunda linha deve ser escrita a string “Coeficientes do Polinômio Multiplicação:”, seguida dos respectivos
coeficientes calculados.

Dica

Represente cada polinômio como um vetor, onde os coeficientes de maior grau estejam mais à esquerda.
"""


def ler_polinomio():
    coeficientes = input().split()

    for indice in range(len(coeficientes)):  # type: int
        coeficientes[indice] = float(coeficientes[indice])

    return coeficientes


def maior_polinomio(polinomio1, polinomio2):
    if len(polinomio1) > len(polinomio2):
        return polinomio1
    else:
        return polinomio2


def menor_polinomio(polinomio1, polinomio2):
    if len(polinomio1) < len(polinomio2):
        return polinomio1
    else:
        return polinomio2


def soma_polinomios(polinomio1, polinomio2):
    maior = maior_polinomio(polinomio1, polinomio2)
    menor = menor_polinomio(polinomio1, polinomio2)

    diferenca_de_grau = len(maior) - len(menor)

    polinomio_soma = [0.0] * len(maior)

    for coeficiente in range(len(maior)):

        if coeficiente < diferenca_de_grau:

            polinomio_soma[coeficiente] = maior[coeficiente]
        else:

            polinomio_soma[coeficiente] = maior[coeficiente] + menor[coeficiente - diferenca_de_grau]

    return polinomio_soma


def multiplica_polinominos(polinomio1, polinomio2):
    grau_polinomio_multiplicacao = len(polinomio1) + len(polinomio2) - 1

    polinomio_multiplicacao = [0.0] * grau_polinomio_multiplicacao

    for i in range(len(polinomio1)):
        for j in range(len(polinomio2)):
            polinomio_multiplicacao[i + j] += polinomio1[i] * polinomio2[j]

    return polinomio_multiplicacao


def imprimir_coeficientes(polinomio):
    for coeficiente in polinomio:
        print(coeficiente, end=" ")
    return None


polinomio_p = ler_polinomio()

polinomio_q = ler_polinomio()

polinomio_soma = soma_polinomios(polinomio_p, polinomio_q)

polinomio_multiplicacao = multiplica_polinominos(polinomio_p, polinomio_q)

print("Coeficientes do Polinômio Soma: ", end='')
imprimir_coeficientes(polinomio_soma)
print()
print("Coeficientes do Polinômio Multiplicação: ", end='')
imprimir_coeficientes(polinomio_multiplicacao)
