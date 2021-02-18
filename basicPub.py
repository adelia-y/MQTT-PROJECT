# Kode dasar buat publish msg 
import paho.mqtt.client as mqtt #import the client1
import time
broker_address="wpcmqtt.cloud.shiftr.io"
clientId="David Publish" #ganti sesuai nama kalian
username= "wpcmqtt"
password= "GW5bGhof1lmPNScl"


client = mqtt.Client(clientId) #create new instance
client.username_pw_set(username,password )
client.connect(broker_address,1883) #connect to broker
i=0
while True:
    client.publish("JawaBarat/Bandung","Data ke-"+str(i))#publish
    i+=1
    time.sleep(2)