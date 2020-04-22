def insere_na_lista(lista, elemento):
    return lista.append(elemento)


def encontraRepeticoes(lista_elementos, quantidade_elementos):
    maior_repeticao = 0
    elementos_maior_repeticao = []

    for i in range(quantidade_elementos):
        elemento_atual = lista_elementos[i]
        quantidade_repeticoes = 0

        for j in range(i, quantidade_elementos):
            if elemento_atual == lista_elementos[j]:
                quantidade_repeticoes = quantidade_repeticoes + 1

        if quantidade_repeticoes > maior_repeticao:
            maior_repeticao = quantidade_repeticoes
            elementos_maior_repeticao = []
            elemento_atual = elemento_atual

        elif quantidade_repeticoes == maior_repeticao:
            insere_na_lista(elementos_maior_repeticao, elemento_atual)

    return elementos_maior_repeticao


# Main

lista_elementos = [7, 3, 6, 7, 1, 6, 5, 9, 6, 8, 8, 7]

print(encontraRepeticoes(lista_elementos, 12))
