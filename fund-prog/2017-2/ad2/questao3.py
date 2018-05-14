"""
O Campeonato de Futebol de Botão do Cederj é um evento bastante popular e você é uma peça fundamental na divulgação do
andamento dos times. Dados os resultados dos jogos, sua tarefa é montar a tabela de classificação correspondente.

A tabela de classificação mostra a colocação de cada time em ordem decrescente de pontos, seguido pelo saldo de gols e
o número de gols marcados. Quando existe empate no número de pontos, no saldo de gols e no número de gols marcados,
você deve considerar que esses times ocupam a mesma posição na tabela de classificação e mostra-los em ordem alfabética.

O número de pontos de um time é dado pela soma de pontos obtidos em cada partida disputada por esse time, onde uma
vitória lhe garante 3 (três) pontos, o empate resulta em 1 (um) ponto e a derrota em 0 (zero) pontos.

O saldo de gols de um time é dado pela quantidade de gols marcados menos a quantidade de
gols sofridos em todas as partidas disputadas por esse time.

Entrada

A entrada é o arquivo texto de nome “partidas.txt”, fornecido pelo dirigente do Campeonato de Futebol de Botão do
Cederj ao término de cada rodada da competição.

A primeira linha do arquivo contém dois valores inteiros T (1 ≤ T ≤ 99) e J (1 ≤ J ≤ 10), onde T é o número de times e
J é o número de jogos disputados.

Cada uma das T linhas seguintes contem o nome de um time. É garantido que os nomes dos times sejam todos diferentes e
compostos por uma única palavra cada. Nenhum nome de time tem mais que 20 caracteres.

Por fim, as J linhas seguintes contém o resultado de cada jogo. Os jogos são mostrados no seguinte formato: nome do
primeiro time, espaço em branco, número de gols marcados pelo primeiro time, um espaço em branco, a letra “x”, um
espaço em branco, número de gols marcados pelo segundo time, um espaço em branco e o nome do segundo time.
É garantido que T e J atenderão os limites indicados. Logo, não é preciso fazer a verificação.

Saída

Seu programa deve emitir o arquivo “tabela.txt”, contendo a tabela de classificação conforme o formato e alinhamento
apresentado no exemplo. Nessa tabela, os times aparecem em ordem de classificação, um por linha. Cada linha é composta
pela posição do time no campeonato (dois caracteres), nome do time (20 caracteres), número de pontos (dois caracteres),
número de jogos disputados (dois caracteres), número de gols marcados (dois caracteres), número de gols sofridos (dois
caracteres) e saldo de gols (três caracteres). Note que se vários times estão empatados, todos recebem a mesma posição
e são apresentados em ordem alfabética. Deve ser colocado um espaço em branco entre cada duas colunas vizinhas da
tabela.
"""


def atualizar_pontuacao(time, nome__do_time, gols_marcados, gols_sofridos):
    dados_time = time[nome__do_time]
    if gols_marcados > gols_sofridos:
        dados_time[1] = 3  # três pontos por vitória
    elif gols_marcados == gols_sofridos:
        dados_time[1] = 1  # pontos (empate)
    dados_time[2] += 1  # jogos_disputados
    dados_time[3] += gols_marcados  # gols_marcados
    dados_time[4] += gols_sofridos  # gols_sofridos
    dados_time[5] += gols_marcados - gols_sofridos  # saldo


def ordenar_times(times_list):
    for i in range(1, len(times_list)):
        time_atual = times_list[i]
        k = i
        while k > 0 and time1_antecede_time2(time_atual, times_list[k - 1]):
            times_list[k] = times_list[k - 1]
            k -= 1
        times_list[k] = time_atual


def time1_antecede_time2(dados_time1, dados_time2):
    if dados_time1[1] > dados_time2[1]:  # pontos
        return True
    elif dados_time1[1] == dados_time2[1]:
        if dados_time1[5] > dados_time2[5]:  # saldo
            return True
        elif dados_time1[5] == dados_time2[5]:
            if dados_time1[3] > dados_time2[3]:  # gols_marcados
                return True
            elif dados_time1[3] == dados_time2[3]:
                return dados_time1[0] < dados_time2[0]  # nome
    return False


def empatou(dados_time1, dados_time2):
    return dados_time1[1] == dados_time2[1] and dados_time1[3] == dados_time2[3] and dados_time1[5] == dados_time2[5]


def imprimir_linha(posicao_time, dados_time):
    arquivo_saida.write("%2d %20s %2d %2d %2d %2d %3d\n" % (
        posicao_time,  # posicao_time
        dados_time[0],  # nome
        dados_time[1],  # pontos
        dados_time[2],  # jogos_disputados
        dados_time[3],  # gols_marcados
        dados_time[4],  # gols_sofridos
        dados_time[5]))  # saldo


# Principal


with open("partidas.txt", "r") as arquivo_de_entrada:
    times, jogos = map(int, arquivo_de_entrada.readline().split())

    dados_do_time = dict()
    for indice_do_time in range(times):
        nome_do_time = arquivo_de_entrada.readline().strip()
        dados_do_time[nome_do_time] = [nome_do_time, 0, 0, 0, 0, 0]  # [nome, pontos, jogos_disputados, gols_marcados, gols_sofridos, saldo]

    for indice_dos_jogos in range(jogos):
        nome_time1, gols_time1, x, gols_time2, nome_time2 = arquivo_de_entrada.readline().split()
        atualizar_pontuacao(dados_do_time, nome_time1, int(gols_time1), int(gols_time2))
        atualizar_pontuacao(dados_do_time, nome_time2, int(gols_time2), int(gols_time1))

dados_do_time_list = list(dados_do_time.values())

ordenar_times(dados_do_time_list)

with open("tabela.txt", "w") as arquivo_saida:
    posicao = 1
    imprimir_linha(posicao, dados_do_time_list[0])
    for indice in range(1, times):
        if not empatou(dados_do_time_list[indice], dados_do_time_list[indice - 1]):
            posicao += 1
        imprimir_linha(posicao, dados_do_time_list[indice])
