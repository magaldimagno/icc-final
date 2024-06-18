from config import *

print(f"Lista de tópicos: {topicos}")
topico = input("Digite o seu tópico: ").upper()
if topico not in topicos:
    print("[ERRO]: Tópico não encontrado")
    exit()

arquivo = os.path.join(os.path.dirname(__file__), input("Digite o nome/caminho do arquivo a partir da pasta tests: "))

with open(arquivo, "rb") as file:
    codificado = b64encode(file.read()).decode()

