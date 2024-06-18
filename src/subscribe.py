from config import *
import datetime  
import os  

# Define o caminho dos arquivos externos utilizados

historico = os.path.join(os.path.dirname(__file__), "log/historico.txt")
notificacao = os.path.join(os.path.dirname(__file__), "sounds/olha_a_mensagem.mp3")

# Função chamada quando uma mensagem é recebida

def on_message(client, userdata, msg):
    try:
        from playsound import playsound # Importa a função playsound da biblioteca playsound
        playsound(notificacao)  # Toca o som de notificação
    except:
        pass
    mensagem = msg.payload.decode()  # Decodifica a mensagem recebida
    topico = msg.topic  # Obtém o tópico da mensagem
    datahora = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')  # Obtém a data e hora atual
    texto = f"{topico} [{datahora}]: {mensagem}"  # Formata a mensagem com o tópico, data e hora, e conteúdo
    id_msg = get_id(msg)  # Obtém o ID da mensagem
    print(texto)  # Imprime a mensagem no console do usuário
    with open(historico, "a") as file:
        print(f"{id_msg} = {texto}", file=file)  # Escreve a mensagem com ID no arquivo de histórico

# Função para obter o ID da mensagem

def get_id(msg):
    id_topico = topicos.index(msg.topic)  # Obtém o índice do tópico na lista de tópicos
    num_msg = 1  # Inicializa o contador de mensagens
    with open(historico, "r") as file:
        for line in file:
            if msg.topic in line:
                num_msg += 1  # Incrementa o contador de mensagens se encontrar uma mensagem com o mesmo tópico
    id = f"{id_topico}.{num_msg}"  # Cria o ID da mensagem no formato "índice_do_tópico.número_da_mensagem"
    return id

# Subscreve aos tópicos e define a função on_message como callback

for i in topicos:
    mqttc.subscribe(i, qos=1)
    mqttc.on_message = on_message

# Inicia o loop infinito para receber mensagens

mqttc.loop_forever()  