from config import *

topico = topicos[0]
mensagem = input("Digite a mensagem: ")

mqttc.publish(topico, mensagem, qos=1)
mqttc.disconnect()