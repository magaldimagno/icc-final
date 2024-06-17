from config import *

print(f'Estes são os usuários disponíveis: {topicos}')
topico = input("Digite o seu usuário: ").upper()
mensagem = input("Digite a mensagem: ")

mqttc.publish(topico, mensagem, qos=1)
mqttc.disconnect()