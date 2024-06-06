from tests.settings import *

"""
CAMINHO TERMINAL:
cd Projetos/USP/ICC/icc-final/tests
python3 teste-publish.py

with open("arquivo.txt", "r") as file:
    arquivo = file.read()
    mqttc.publish("teste", arquivo, qos=1)
"""

topico = topicos[0]

mensagem = "Hello World!"

mqttc.publish(topico, mensagem, qos=1)

mqttc.disconnect()