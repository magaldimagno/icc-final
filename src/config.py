# Importa a biblioteca paho.mqtt.client para utilizar o MQTT

import paho.mqtt.client as mqtt

# Define o endereço do servidor MQTT

host = "mqtt.eclipseprojects.io"

# Cria uma instância do cliente MQTT e conecta ao servidor MQTT

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.connect(host, 1883, 60)

# Define a lista dos tópicos MQTT

topicos = ["MAGNO", "LEQUE", "PERIGOSO", "GBR", "ANDRE"]