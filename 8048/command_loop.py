import argparse
import paho.mqtt.client as mqttClient
import time
# import subprocess
import os
  
parser = argparse.ArgumentParser(description="MPP-5048 MQTT client script")
parser.add_argument("--broker", required=True, help="Broker address")
parser.add_argument("--port", default=1883, type=int, help="Broker port")
parser.add_argument("--user", help="Username")
parser.add_argument("--password", help="Password")
parser.add_argument("--device_addr", required=True, help="Device port addr")
parser.add_argument("--topic", required=True, help="Tag name")

args = parser.parse_args()
broker_address = args.broker
port = args.port
user = args.user
password = args.password
device_addr = args.device_addr
topic = args.topic
  
def on_message(client, userdata, message):
    global device_addr, topic
    
    print("Message received: ", message.payload)
    print("Message Topic: ", message.topic)

    if message.topic == topic:
        print("EXEC inv3")
        command_str = message.payload.decode()
        full_str_cmd = "mpp-solar -p {device_addr} -P PI30 -c {cmd}".format(device_addr=device_addr, cmd=command_str)
        os.system(full_str_cmd)
        time.sleep(1)
        os.system(full_str_cmd)
 

def on_connect(client, userdata, flags, rc):
  
    if rc == 0:
  
        print("Connected to broker")
  
        global Connected                #Use global variable
        Connected = True                #Signal connection 

        client.on_message= on_message 
        client.subscribe(topic)
  
    else:
  
        print("Connection failed")

Connected = False   #global variable for the state of the connection
  
client = mqttClient.Client("Python",clean_session=False)               #create new instance
client.username_pw_set(username=user, password=password)    #set username and password
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
    
  
client.subscribe(topic)
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
