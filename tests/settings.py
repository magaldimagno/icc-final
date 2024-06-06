import paho.mqtt.client as mqtt
import PIL.Image as Image
import datetime
import os

#Host Gratuito: ????
#Host Local: localhost
#Host Paho: mqtt.eclipseprojects.io

host = "mqtt.eclipseprojects.io"

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.connect(host, 1883, 60)

topicos = ["MAGNO", "ELEONORA", "GBR", "PERIGOSO", "TESTE", "LEQUE", "ICC-USP"]

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    client.subscribe("$SYS/#")

arquivo = os.path.join(os.path.dirname(__file__), "arquivo.txt")

def on_message(client, userdata, msg):
    message = msg.payload.decode()
    topic = msg.topic
    date = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    retain = msg.retain
    texto = f"{topic} [{date}]: {message}"
    print(texto)
    with open(arquivo, "a") as file:
        print(texto, file=file)