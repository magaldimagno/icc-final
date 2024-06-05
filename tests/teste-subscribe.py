from settings.settings import *

mqttc.subscribe("teste")

mqttc.on_message = on_message
#mqttc.on_connect = on_connect
mqttc.loop_forever()
