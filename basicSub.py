import paho.mqtt.client as mqtt
broker_address="wpcmqtt.cloud.shiftr.io"
clientId="David Subscribe" #ganti sesuai nama kalian
username= "wpcmqtt"
password= "GW5bGhof1lmPNScl"
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("JawaBarat/Bandung")
    client.subscribe("JawaBarat/Cirebon")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("Topic: " +msg.topic+" Msg: "+str(msg.payload.decode("utf-8")))

client = mqtt.Client(clientId)
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username,password )
client.connect(broker_address,1883) #connect to broker

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()