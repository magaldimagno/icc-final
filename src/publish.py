from config import *

print(f"Lista de tópicos: {topicos}")
topico = input("Digite o seu tópico: ").upper()
if topico not in topicos:
    print("[ERRO]: Tópico não encontrado")
    exit()

mensagem = input("Digite a mensagem: ")
mqttc.publish(topico, mensagem, qos=1)
mqttc.disconnect()