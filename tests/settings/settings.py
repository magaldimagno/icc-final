import paho.mqtt.client as mqtt

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.connect("localhost", 1883, 60)

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    client.subscribe("$SYS/#")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
