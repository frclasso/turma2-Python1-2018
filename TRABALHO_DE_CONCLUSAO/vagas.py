#!/usr/bin/env python3

import csv

print('Modulo vagas importado com sucesso!')

""""Separar as funcoes, definir uma para ler vagasDisponiveis e salvar em uma lista,
                        definir uma para ler vagasOcupadas e salvar em lista
                        fazer operacoes de diferenca - set
                        definir fucao para escrever dados vagasDisponiveis.csv
                        definir fucao para escrever dados vagasOcupadas.csv
                        """
vagasDisponiveis = []
vagasOcupadas = []

vagas = []
with open('vagas.csv','r') as f:
    csv_file = csv.reader(f)
    for x in csv_file:
        vagas.extend(x)


with open('vagasDisponiveis.csv', 'r') as f:
    csv_file = csv.reader(f)
    for v in csv_file:
        vagasDisponiveis.extend(v)

with open('vagasOcupadas.csv', 'r') as f:
    csv_file = csv.reader(f)
    for v in csv_file:
        vagasOcupadas.extend(v)


def zeraVagas():
    '''Zera vagas ocupdas para um novo dia de trabalho'''
    global vagasOcupadas
    global vagasDisponiveis
    vagasOcupadas = []
    vagasDisponiveis = vagas[:]
    print('Vagas liberadas com sucesso, ja podemos iniciar os trabalhos.')
    print('Vagas Ocupadas ==>', vagasOcupadas)
    print('Vagas a disposição:', vagasDisponiveis)
    salvaDados()


def entrada():
    """Insere uma entrada de vaga no arquivo vagasOcupadas.csv e retira de vagasDisponiveis.csv"""

    # inserindo vaga a ser utilizada

    vaga = input('Insira a vaga a ser utilizada:')
    if vaga in vagasOcupadas:
        print('Vaga Nao disponivel')
    else:
        vagasOcupadas.append(vaga)
        vagasDisponiveis.remove(vaga)


def saida():
    """Insere uma saida de vaga no arquivo vagasDisponiveis.csv e retira de vagasOcupadas.csv"""
    # inserindo vaga a ser utilizada
    #
    # global vagasOcupadas
    # global vagasDisponiveis
    vaga = input('Digite vaga a ser liberada:')
    for v in vagasOcupadas:
        if vaga == v:
            vagasOcupadas.remove(vaga)
        vagasDisponiveis.append(vaga)

    print('Carro saindo')


def salvaDados():
    global vagasOcupadas
    global vagasDisponiveis

    with open('vagasOcupadas.csv', mode='w') as f2:
        csv_file = csv.writer(f2)
        for v in sorted(vagasOcupadas):
            f2.write('{},'.format(v))

    with open('vagasDisponiveis.csv', mode='w') as f2:
        csv_file = csv.writer(f2)
        for v in sorted(vagasDisponiveis):
            f2.write('{},'.format(v))

#
# zeraVagas()
#
#
# entrada()
# print(vagasOcupadas)
# print(vagasDisponiveis)
#
# entrada()
# print(vagasOcupadas)
# print(vagasDisponiveis)
#
# entrada()
# print(vagasOcupadas)
# print(vagasDisponiveis)
#
#
# saida()
# print(vagasOcupadas)
# print(vagasDisponiveis)
#
# salvaDados()