from config import *

print(f"Lista de usuários: {topicos}")
topico = input("Digite o seu usuário: ").upper()
if topico not in topicos:
    print("[ERRO]: Usuário não encontrado")
    exit()

mensagem = input("Digite a mensagem: ")
mqttc.publish(topico, mensagem, qos=1)
mqttc.disconnect()