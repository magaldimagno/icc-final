import paho.mqtt.client as mqtt
import PIL.Image as Image

#Host Gratuito: ????
#Host Local: localhost
#Host Paho: mqtt.eclipseprojects.io

host = "localhost"

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.connect(host, 1883, 60)

topico = "ICC-USP"

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    client.subscribe("$SYS/#")

def on_message(client, userdata, msg):
    print(msg.topic +": " +msg.payload.decode())
