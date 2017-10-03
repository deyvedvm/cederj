# Funções auxiliares

def car(lis):
    return lis[0]


def cdr(lis):
    return lis[1:]


def cons(x, lis):
    return [x] + lis


def ehLista(x):
    return isinstance(x, list)


def ehAtomo(x):
    return not ehLista(x)


# Questão 1a

def maiorElemento(x, lista):
    if not lista:
        return x
    else:
        if x >= car(lista):
            return maiorElemento(x, cdr(lista))
        else:
            return maiorElemento(car(lista), cdr(lista))


def maior(lista):
    if not lista:
        return 0
    else:
        return maiorElemento(car(lista), cdr(lista))


# Questão 1b

def maioresQueZero(lista):
    if not lista:
        return []
    else:
        if car(lista) <= 0:
            return maioresQueZero(cdr(lista))
        else:
            return cons(car(lista), maioresQueZero(cdr(lista)))


def comprimento(lista):
    if not lista:
        return 0
    else:
        return 1 + comprimento(cdr(lista))


def somaLista(lista):
    if lista == []:
        return 0
    else:
        return car(lista) + somaLista(cdr(lista))


def mediaPositivos(lista):
    if lista == [] or maioresQueZero(lista) == []:
        return 0
    else:
        return somaLista(maioresQueZero(lista)) + comprimento(maioresQueZero(lista))


# Questão 1c

def concatena(listaA, listaB):
    if not listaA:
        return listaB
    else:
        return cons(car(listaA), concatena(cdr(listaA), listaB))


def emagrece(lista):
    if not lista:
        return []
    else:
        if ehAtomo(car(lista)):
            return cons(car(lista), emagrece(cdr(lista)))
        else:
            return concatena(emagrece(car(lista)), emagrece(cdr(lista)))
    return []


# Programa Principal

print("Questão 1-a")
print("\t", maior([10, 2, 5, 13, 26, 4, 2, 9, 33, 18, 6, -99, 12, 17]))
print("\t", maior([]))
print("\t", maior([-10, -13, 12.99, 100, 888, 0, 83]))

print("Questão 1-b")
print("\t", mediaPositivos([-10, -2, -5, 13, -26, -4, 3, -9, 33, -18, -6, -99, -12, 17]))
print("\t", mediaPositivos([]))
print("\t", mediaPositivos([-10, -2, -5]))

print("Teste Q1.c:")
print("\t", emagrece([]))
print("\t", emagrece([[[]]]))
print("\t", emagrece(["ana", [["maria", "chico"]], [[["igor"]]], "juca"]))
print("\t", emagrece([10, 2, 5, 13, [[[26, [[4]], 2]]], 9, 33, [18, 6], 99, 12, 17]))
