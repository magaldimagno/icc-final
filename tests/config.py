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

topicos = ["MAGNO", "ELEONORA", "GBR", "PERIGOSO", "TESTE", "LEQUE", "ICC-USP", "JOÃO PAULO"]

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    client.subscribe("$SYS/#")

historico = os.path.join(os.path.dirname(__file__), "historico.txt")
#log = os.path.join(os.path.dirname(__file__), "log.txt")

def on_message(client, userdata, msg):
    message = msg.payload.decode()
    topic = msg.topic
    date = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    text = f"{topic} [{date}]: {message}"
    id_msg = get_id(msg)
    print(text)
    with open(historico, "a") as file:
        print(f"{id_msg} = {text}", file=file)

def get_id(msg):
    id_topico = topicos.index(msg.topic)
    num_msg = 1
    with open(historico, "r") as file:
        for line in file:
            if msg.topic in line:
                num_msg += 1
    id = f"{id_topico}.{num_msg}"
    return id