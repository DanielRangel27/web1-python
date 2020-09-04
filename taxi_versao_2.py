from datetime import datetime, timedelta

def inicia_corrida():
    global data_hora_inicio
    data_hora_inicio = datetime.now()

    # teste:
    # horário bandeira 1
    # horário bandeira 2

def finaliza_corrida():
    global data_hora_termino
    
    # data_hora_termino = datetime.now()
    # somente para testar
    delta_tempo_mock = timedelta(hours=0, minutes=15, seconds=0)
    data_hora_termino = data_hora_inicio + delta_tempo_mock

def is_bandeira_01():
    if ((data_hora_inicio.hour>22) and (data_hora_inicio.hour<6)):
        return False
    else:
        return True

def calcula_corrida():
    global duracao_corrida
    global valor_corrida
    duracao_corrida = data_hora_termino-data_hora_inicio
    duracao_corrida = int(duracao_corrida.seconds/60)
    if is_bandeira_01:
        valor_corrida = 5.50 + (0.50*duracao_corrida)
    else:
        valor_corrida = 5.50 + (0.50*1.10*duracao_corrida)

def imprimir_cabecalho():
    print('***********************')
    print('Extrato da Corrida')
    print('***********************')
    print('Cód. cliente: {}'.format(cod_cliente))
    print('Nome cliente: {}'.format(nome_cliente))
    print('***********************')

def imprimir_rodape():
    print('***********************')
    data_hora_atual = datetime.now()
    print(data_hora_atual)
    print('***********************')

def imprimir_dados_corrida(data_hora_inicio, data_hora_termino, duracao_corrida, valor_corrida):
    print('Início da corrida: {}'.format(data_hora_inicio))
    print('Término da corrida: {}'.format(data_hora_termino))
    print('Duração da corrida: {}'.format(duracao_corrida))
    print('Valor da corrida: {}'.format(valor_corrida))

def imprimir_relatorio_corrida():
    imprimir_cabecalho()
    imprimir_dados_corrida(data_hora_inicio, data_hora_termino, duracao_corrida, valor_corrida)
    imprimir_rodape()

def get_cliente():
    return 1, 'Cliente 1'

if __name__ == "__main__":
    global cod_cliente
    global nome_cliente
    # variáveis globais
    global data_hora_inicio
    global data_hora_termino
    global duracao_corrida
    global valor_corrida


    cod_cliente = get_cliente()[0]
    nome_cliente = get_cliente()[1]
    data_hora_inicio = 0
    data_hora_termino = 0
    duracao_corrida = 0
    valor_corrida = 0

    inicia_corrida()
    finaliza_corrida()
    calcula_corrida()
    imprimir_relatorio_corrida()