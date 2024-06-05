from settings.settings import *

"""
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

mqttc.on_connect = on_connect
mqttc.on_message = on_message

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
mqttc.loop_forever()

CAMINHO TERMINAL:
cd Projetos/USP/ICC/icc-final/tests
python3 teste-subscribe.py
"""

with open("arquivo.txt", "r") as file:
    arquivo = file.read()
    #mqttc.publish("teste", "Hello World!")

mqttc.publish("teste", arquivo, qos=1)

mqttc.disconnect()