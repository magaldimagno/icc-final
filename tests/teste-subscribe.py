from settings import *

for i in topicos:
    mqttc.subscribe(i, qos=1)
    mqttc.on_message = on_message
mqttc.loop_forever()
