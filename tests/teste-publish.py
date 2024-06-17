from config import *

"""
CAMINHO TERMINAL:
cd Projetos/USP/ICC/icc-final/tests
python3 teste-publish.py

with open("arquivo.txt", "r") as file:
    arquivo = file.read()
    mqttc.publish("teste", arquivo, qos=1)

topico = topicos[0]

print(f'Estes são os usuários disponíveis: {topicos}')
topico = input("Digite o seu usuário: ").upper()
if topico in topicos:
    mensagem = input("Digite a mensagem: ")
else:
    print("Usuário não cadastrado")
    resposta = input("Deseja cadastrar um novo usuário? (s/n) ").lower()
    if resposta == "s" or resposta == "sim":
        topicos.append(topico.upper)
        with open(cadastros, "a") as file:
            print(topico, file=file)
        print(f'Usuário {topico} cadastrado com sucesso!')
        mensagem = input("Digite a mensagem: ")
    else:
        exit()

"""

print(f"Lista de tópicos: {topicos}")
topico = input("Digite o seu tópico: ").upper()
if topico not in topicos:
    print("[ERRO]: Tópico não encontrado")
    exit()

mensagem = input("Digite a mensagem: ")

mqttc.publish(topico, mensagem, qos=1)

mqttc.disconnect()