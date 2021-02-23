
 
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

alertstrings = []
 
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("notificationAlert")
    client.subscribe("iOSupdate")
    client.subscribe("newAlert")
    client.subscribe("statusUpdate")
    client.subscribe("descriptionUpdate")
    
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #alertstring = ("\n" + str(msg.payload.decode("utf-8")))
    alertstrings.append(str(msg.payload.decode("utf-8")))    
    f = open("alertslog.txt", 'w')
    data = '\n'.join(alertstrings)
    f.write(data)
    f.close()
    """print(msg.topic+" "+str(msg.payload))
    
    if msg.payload.decode(encoding='UTF-8') == "Critical":
        print("Paint Department has critical issue")"""


#Set MQTT server adress
thepipster = "192.168.1.17"


# Create an MQTT client and attach our routines to it.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(thepipster)

 
# Process network traffic and dispatch callbacks. This will also handle
# reconnecting. Check the documentation at
# https://github.com/eclipse/paho.mqtt.python
# for information on how to use other loop*() functions
client.loop_forever()
