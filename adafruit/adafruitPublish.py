import paho.mqtt.client as mqtt #import the client1
import time
import random 

broker_address="io.adafruit.com"
clientId="Adelia Publish" #ganti sesuai nama kalian
username= "adelia_y" #Ganti sesuai username kalian
password= "aio_oCNL46vELAFdN0PD9hbjryNPusxH" #ganti sesuai token API kalian

#broker_address="iot.eclipse.org" #use external broker
client = mqtt.Client(clientId) #create new instance
client.username_pw_set(username, password)
client.connect(broker_address) #connect to broker

t = random.randint(0,100)
w = 11
p = 1
h = 70
cc = 50
pr = 80
aq = "Moderate"
st = "Cloudy Day"

while True:
    #publish
    client.publish(username+"/feeds/"+"temperature",t)
    client.publish(username+"/feeds/"+"wind",w)
    client.publish(username+"/feeds/"+"airquality",aq)
    client.publish(username+"/feeds/"+"pressure",p)
    client.publish(username+"/feeds/"+"humidity",h)
    client.publish(username+"/feeds/"+"cloudcover",cc)
    client.publish(username+"/feeds/"+"precipitation",pr)
    client.publish(username+"/feeds/"+"status",st)
    
    t = t + random.randint(-10,10) #deg C
    time.sleep(5)
    w = random.randint(5, 20) #km/h
    time.sleep(5)
    p = p + random.randint(-1,1) #bar
    time.sleep(5)
    h = h + random.randint(-2,2) #%
    time.sleep(5)
    cc = cc + random.randint(-5,5) #%
    time.sleep(5)
    pr = pr + random.randint(-10,10) #mm
    time.sleep(5)
    st = random.choice(["Heavy Rain", "Light Rain", "Thunderstorm", "Cloudy Day", "Sunny Day"])
    time.sleep(5)
    aq = random.choice(["Fair", "Moderate", "Unhealthy", "Hazardous"])
    time.sleep(5)
