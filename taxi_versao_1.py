from datetime import datetime, timedelta
data_hora_inicio = 0
data_hora_termino = 0
duracao_corrida = 0
valor_corrida = 0

data_hora_inicio = datetime.now()
# somente para testar
delta_tempo_mock = timedelta(hours=0, minutes=15, seconds=59)
data_hora_termino = data_hora_inicio + delta_tempo_mock

duracao_corrida = data_hora_termino-data_hora_inicio
duracao_corrida = int(duracao_corrida.seconds/60)

def get_cliente():
    return 1, 'Cliente 1'

if ((data_hora_inicio.hour>22) and (data_hora_inicio.hour<6)):
    print('***********************')
    print('Extrato da Corrida')
    print('***********************')
    cod_cliente = get_cliente()[0]
    nome_cliente = get_cliente()[1]
    print('Cód. cliente: {}'.format(cod_cliente))
    print('Nome cliente: {}'.format(nome_cliente))
    print('***********************')
    valor_corrida = 5.50 + (0.50*1.10*duracao_corrida)
    print('Início da corrida: {}'.format(data_hora_inicio))
    print('Término da corrida: {}'.format(data_hora_termino))
    print('Duração da corrida: {}'.format(duracao_corrida))
    print('Valor da corrida: {}'.format(valor_corrida))
    print('***********************')
    data_hora_atual = datetime.now()
    print(data_hora_atual)
    print('***********************')

else:
    print('***********************')
    print('Extrato da Corrida')
    print('***********************')
    cod_cliente = get_cliente()[0]
    nome_cliente = get_cliente()[1]
    print('Cód. cliente: {}'.format(cod_cliente))
    print('Nome cliente: {}'.format(nome_cliente))
    print('***********************')
    valor_corrida = 5.50 + (0.50*duracao_corrida)
    print('Início da corrida: {}'.format(data_hora_inicio))
    print('Término da corrida: {}'.format(data_hora_termino))
    print('Duração da corrida: {}'.format(duracao_corrida))
    print('Valor da corrida: {}'.format(valor_corrida))
    print('***********************')
    data_hora_atual = datetime.now()
    print(data_hora_atual)
    print('***********************')