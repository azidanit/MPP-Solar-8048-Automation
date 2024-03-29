import paho.mqtt.client as mqttClient
import time
# import subprocess
import os
  

  
def on_message(client, userdata, message):
    print("Message received: ", message.payload)
    print("Message Topic: ", message.topic)

    if message.topic == "homeassistant/sensor/inverter_3":
        print("EXEC inv3")
        command_str = message.payload.decode()
        full_str_cmd = "mpp-solar -p /dev/ttyUSB0 -P PI30 -c " + command_str
        os.system(full_str_cmd)
        time.sleep(0.1)
        os.system(full_str_cmd)

    if message.topic == "homeassistant/sensor/inverter_5":
        print("EXEC inv5")
        command_str = message.payload.decode()
        full_str_cmd = "mpp-solar -p /dev/ttyUSB1 -P PI30 -c " + command_str
        os.system(full_str_cmd)
        time.sleep(0.1)
        os.system(full_str_cmd)
    
    if message.topic == "homeassistant/sensor/inverter_1":
        print("EXEC inv1")

        command_str = message.payload.decode()
        full_str_cmd = "mpp-solar -p /dev/hidraw0 -P PI30 -c " + command_str
        os.system(full_str_cmd)
        time.sleep(0.1)
        os.system(full_str_cmd)
    

    if message.topic == "homeassistant/sensor/inverter_2":
        print("EXEC inv2")
        command_str = message.payload.decode()
        full_str_cmd = "mpp-solar -p /dev/hidraw1 -P PI30 -c " + command_str
        os.system(full_str_cmd)
        time.sleep(0.1)
        os.system(full_str_cmd)

  

def on_connect(client, userdata, flags, rc):
  
    if rc == 0:
  
        print("Connected to broker")
  
        global Connected                #Use global variable
        Connected = True                #Signal connection 

        client.on_message= on_message 
        client.subscribe("homeassistant/sensor/inverter_3")
        client.subscribe("homeassistant/sensor/inverter_1")
        client.subscribe("homeassistant/sensor/inverter_2")
        client.subscribe("homeassistant/sensor/inverter_5")
  
    else:
  
        print("Connection failed")

Connected = False   #global variable for the state of the connection
  
broker_address= "192.168.1.102"  #Broker address
# broker_address= "localhost"  #Broker address
port = 1883                       #Broker port
user = "sonoff"                    #Connection username
password = "sonoff"            #Connection password
  
client = mqttClient.Client("Python",clean_session=False)               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback
  

is_mqtt_connected = False

while not is_mqtt_connected:
    try:
        is_mqtt_connected = True
        client.connect(broker_address, port=port)          #connect to broker
    except:
        is_mqtt_connected = False
        print("cannot connect")
        time.sleep(1)
    


  
client.subscribe("homeassistant/sensor/inverter_3")
client.subscribe("homeassistant/sensor/inverter_1")
client.subscribe("homeassistant/sensor/inverter_2")
client.subscribe("homeassistant/sensor/inverter_5")
  

client.loop_forever()        #start the loop
  
while Connected != True:    #Wait for connection
    time.sleep(0.1)

try:
    while True:
        time.sleep(1)
  
except KeyboardInterrupt:
    print("exiting")
    client.disconnect()
    client.loop_stop()
