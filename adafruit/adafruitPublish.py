import paho.mqtt.client as mqtt #import the client1
import time
broker_address="io.adafruit.com"
clientId="David Publish" #ganti sesuai nama kalian
username= "davidfauzi" #Ganti sesuai username kalian
password= "0f7873c4c7bf48bb95e79d4112889e8e" #ganti sesuai token API kalian
topic = "sensorsuhu" # ganti sesuai key sensor yang mau kalian masukin

#broker_address="iot.eclipse.org" #use external broker
client = mqtt.Client("hai") #create new instance
client.username_pw_set(username, password)
client.connect(broker_address) #connect to broker
i=0
while True:
    #publish
    client.publish(username+"/feeds/"+topic,i)
    i+=1
    time.sleep(5)