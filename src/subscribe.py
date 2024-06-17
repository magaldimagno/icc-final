from config import *
import datetime
import os

historico = os.path.join(os.path.dirname(__file__), "log/historico.txt")

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

for i in topicos:
    mqttc.subscribe(i, qos=1)
    mqttc.on_message = on_message
mqttc.loop_forever()