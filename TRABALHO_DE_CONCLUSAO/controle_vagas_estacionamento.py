#!/usr/bin/env python3

"""Desenvolver uma aplicacao de controle de vagas de estacionamento"""

print('Modulo controle_vagas_estacionamento importado com sucesso')

from datetime import datetime
import vagas as v


now = datetime.now()

# O que precisamos?
# quantidade de vagas totais, vagas em uso, vagas disponiveis
# cadastro de clientes mensalistas, cadastro de veiculos
# metodos de pagamento
# controle de entrada e saida, data e hora
# relatorio com faturamento, salvar em .csv modo 'a', append


#criando lista de usuarios

clientesMensalistas = []
clientesDiaristas = []
clientesAvulsos = []


def entradaCliente():
    global clientesMensalistas
    global clientesDiaristas
    global clientesAvulsos

    cliente = input('Digite nome do cadastro:')

    clienteTipo = input('Digite o tipo do cliente, Mensalista/Diarista/Horista:')
    if clienteTipo == 'm':
        clientesMensalistas.append(cliente)
    elif clienteTipo == 'd':
        clientesDiaristas.append(cliente)
    else:clientesAvulsos.append(cliente)

    tipoDeVeiculo = input('Digite o tipo de veículo, passeio/moto/utilitário:')
    modelo = input('Digite o modelo do veículo, ex: Fusca:')
    veiculoPlaca = input('Digite a placa do veiculo:')
    horarioEntrada = now.strftime("%H:%M:%S %p")

    global v
    v.entrada()

    return f'Nome: {cliente}, veiculo: {modelo}, Placa: {veiculoPlaca}, horario de entrada: {horarioEntrada}'


def saidaCliente():
    modelo = input('Digite o modelo do veículo, ex: Fusca:')
    veiculoPlaca = input('Digite a placa do veiculo:')
    horarioSaida = now.strftime("%H:%M:%S %p")
    global v
    v.saida()
    return f'Modelo: {modelo}, Placa: {veiculoPlaca}, Horario de saída: {horarioSaida}'


# valorHora = 10.00
# quantidadeHoras = 0
# totalDia = valorHora * quantidadeHoras
# totalSemana = totalDia * 7
# totalMes = totalDia * 22
