from config import *

# Fornece a lista de usuários cadastrados

print(f"Lista de usuários: {topicos}")

# Solicita ao usuário que digite o seu nome de usuário

topico = input("Digite o seu usuário: ").upper()

# Verifica se o nome fornecido está presente na lista de usuários cadastrados

if topico not in topicos:
    print("[ERRO]: Usuário não encontrado")
    exit()

# Solicita ao usuário que digite a mensagem a ser publicada

mensagem = input("Digite a mensagem: ")

# Publica a mensagem no tópico correspondente ao usuário usando o protocolo MQTT com qualidade de serviço 1

mqttc.publish(topico, mensagem, qos=1)

mqttc.disconnect()