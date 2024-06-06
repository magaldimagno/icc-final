from config import *

"""
CAMINHO TERMINAL:
cd Projetos/USP/ICC/icc-final/tests
python3 teste-publish.py

with open("arquivo.txt", "r") as file:
    arquivo = file.read()
    mqttc.publish("teste", arquivo, qos=1)


print(f"Lista de tópicos: {topicos}")
topico = input("Digite o tópico: ").upper()
if topico not in topicos:
    print("[ERRO]: Tópico não encontrado")
    exit()
"""

topico = topicos[0]

mensagem = input("Digite a mensagem: ")

mqttc.publish(topico, mensagem, qos=1)

mqttc.disconnect()