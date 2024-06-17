import paho.mqtt.client as mqtt

host = "mqtt.eclipseprojects.io"

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.connect(host, 1883, 60)

topicos = ["MAGNO", "LEQUE", "PERIGOSO", "GBR", "ANDRE"]