
import os
import time
import argparse

from threading import Thread

counter_another_status = 0

def inverter1_status(broker_address, port, user, password, device_addr, tag):
    ############## 5048 1 #############
    while True:
        print("PUSH 5048 1")
        os.system("mpp-solar -p {device_addr} -c QPIGS -q {broker_addr} --mqttport {port} --mqttuser {user} --mqttpass {password} --tag {tag} -o mqtt".format(device_addr=device_addr, broker_addr=broker_address, port=port, user=user, password=password, tag=tag))
        time.sleep(0.5)
        os.system("mpp-solar -p {device_addr} -c QMOD -q {broker_addr} --mqttport {port} --mqttuser {user} --mqttpass {password} --tag {tag} -o mqtt".format(device_addr=device_addr, broker_addr=broker_address, port=port, user=user, password=password, tag=tag))
        time.sleep(0.5)
        os.system("mpp-solar -p {device_addr} -c QPIGS -q {broker_addr} --mqttport {port} --mqttuser {user} --mqttpass {password} --tag {tag} -o mqtt".format(device_addr=device_addr, broker_addr=broker_address, port=port, user=user, password=password, tag=tag))
        time.sleep(0.5)
        os.system("mpp-solar -p {device_addr} -c QMOD -q {broker_addr} --mqttport {port} --mqttuser {user} --mqttpass {password} --tag {tag} -o mqtt".format(device_addr=device_addr, broker_addr=broker_address, port=port, user=user, password=password, tag=tag))
        time.sleep(0.5)
        print("PUSH 5048 1 Done")

        os.system("mpp-solar -p {device_addr} -c QPIWS -q {broker_addr} --mqttport {port} --mqttuser {user} --mqttpass {password} --tag {tag} -o mqtt".format(device_addr=device_addr, broker_addr=broker_address, port=port, user=user, password=password, tag=tag))
        time.sleep(0.5)
        os.system("mpp-solar -p {device_addr} -c QPIRI -q {broker_addr} --mqttport {port} --mqttuser {user} --mqttpass {password} --tag {tag}_conf -o mqtt".format(device_addr=device_addr, broker_addr=broker_address, port=port, user=user, password=password, tag=tag))
        time.sleep(0.5)
        os.system("mpp-solar -p {device_addr} -c QPIRI -q {broker_addr} --mqttport {port} --mqttuser {user} --mqttpass {password} --tag {tag}_conf -o mqtt".format(device_addr=device_addr, broker_addr=broker_address, port=port, user=user, password=password, tag=tag))
        time.sleep(0.5)

        print("PUSH 5048 1 conf Done")
    ############## 5048 1 #############

parser = argparse.ArgumentParser(description="MPP-5048 MQTT client script")
parser.add_argument("--broker", required=True, help="Broker address")
parser.add_argument("--port", default=1883, type=int, help="Broker port")
parser.add_argument("--user", required=True, help="Username")
parser.add_argument("--password", required=True, help="Password")
parser.add_argument("--device_addr", required=True, help="Device port addr")
parser.add_argument("--tag", required=True, help="Tag name")

args = parser.parse_args()
broker_address = args.broker
port = args.port
user = args.user
password = args.password
device_addr = args.device_addr
tag = args.tag

t1_status = Thread(target=inverter1_status, args=(broker_address, port, user, password, device_addr, tag))

# start the threads
t1_status.start()

# wait for the threads to complete
t1_status.join()
