# IMPORT LIBRARY 
import paho.mqtt.client as mqtt #import the client1
import time
import random 

# SET BROKER (SERVER)
broker_address="io.adafruit.com"
clientId="Adelia Publish" #ganti sesuai nama kalian
username= "adelia_y" #Ganti sesuai username kalian
password= "aio_oCNL46vELAFdN0PD9hbjryNPusxH" #ganti sesuai token API kalian

client = mqtt.Client(clientId) #create new instance
client.username_pw_set(username, password)
client.connect(broker_address) #connect to broker

# VARABLE DECLARATIONS AND INITIALIZE DEFAULT VALUES
t = 25 # temperature
w = 11 # wind speed
p = 1 # pressure
h = 70 # humidity
cc = 50 # cloud cover
pr = 80 # precipitation
aq = "Moderate" # air quality
st = "Cloudy Day" # status 

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
    
    t = abs(t + random.randint(-5,5)) #deg C
    time.sleep(5)
    w = abs(w + random.randint(-3, 3)) #km/h
    time.sleep(5)
    p = abs(p + random.randint(-3,3)) #bar
    time.sleep(5)
    h = abs(h + random.randint(-3,3)) #%
    time.sleep(5)
    cc = abs(cc + random.randint(-5,5)) #%
    time.sleep(5)
    pr = abs(pr + random.randint(-10,10)) #mm
    time.sleep(5)
    st = random.choice(["Heavy Rain", "Light Rain", "Thunderstorm", "Cloudy Day", "Sunny Day"])
    time.sleep(5)
    aq = random.choice(["Fair", "Moderate", "Unhealthy", "Hazardous"])
    time.sleep(5)