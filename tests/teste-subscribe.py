from settings import *

mqttc.subscribe(topico, qos=1)
mqttc.subscribe(topico1, qos=1)
mqttc.subscribe(topico2, qos=1)

mqttc.on_message = on_message
#mqttc.on_connect = on_connect
mqttc.loop_forever()
