
import argparse
import os
import random
import time

from threading import Thread

counter_another_status = 0

def inverter8048_status(device_addr, broker_addr, port, user, password, tag, sleep_time=5):
    while True:
        ############## 8048 #############
        print("\t\t\t\tPUSH 8048")
        os.system("mpp-solar -p {device_addr} -c QPIGS -q {broker_addr} --mqttport {port} --mqttuser {user} --mqttpass {password} --tag {tag} -P PI30MAX -o mqtt".format(device_addr=device_addr, broker_addr=broker_addr, port=port, user=user, password=password, tag=tag))
        time.sleep(3.5)
        os.system("mpp-solar -p {device_addr} -c QPIGS2 -q {broker_addr} --mqttport {port} --mqttuser {user} --mqttpass {password} --tag {tag} -P PI30MAX -o mqtt".format(device_addr=device_addr, broker_addr=broker_addr, port=port, user=user, password=password, tag=tag))
        time.sleep(3.5)
        os.system("mpp-solar -p {device_addr} -c QMOD -q {broker_addr} --mqttport {port} --mqttuser {user} --mqttpass {password} --tag {tag} -P PI30MAX -o mqtt".format(device_addr=device_addr, broker_addr=broker_addr, port=port, user=user, password=password, tag=tag))
        time.sleep(3.5)
        os.system("mpp-solar -p {device_addr} -c Q1 -q {broker_addr} --mqttport {port} --mqttuser {user} --mqttpass {password} --tag {tag} -P PI30 -o mqtt".format(device_addr=device_addr, broker_addr=broker_addr, port=port, user=user, password=password, tag=tag))
        time.sleep(3.5)
        print("\t\t\t\tPUSH 8048 done")
        ############## 8048 #############
        os.system("mpp-solar -p {device_addr} -c QPIWS -q {broker_addr} --mqttport {port} --mqttuser {user} --mqttpass {password} --tag {tag} -P PI30MAX -o mqtt".format(device_addr=device_addr, broker_addr=broker_addr, port=port, user=user, password=password, tag=tag))
        time.sleep(3.5)
        os.system("mpp-solar -p {device_addr} -c QPIRI -q {broker_addr} --mqttport {port} --mqttuser {user} --mqttpass {password} --tag {tag}_conf -P PI30 -o mqtt".format(device_addr=device_addr, broker_addr=broker_addr, port=port, user=user, password=password, tag=tag))
        time.sleep(3.5)
        print("\t\t\t\tPUSH 8048 conf done")

        # random int between 1 and 10, eachtime value is different
        random_int = random.randint(5, 20)
        time.sleep(random_int)

parser = argparse.ArgumentParser(description="MPP-5048 MQTT client script")
parser.add_argument("--broker", required=True, help="Broker address")
parser.add_argument("--port", default=1883, type=int, help="Broker port")
parser.add_argument("--user", required=True, help="Username")
parser.add_argument("--password", required=True, help="Password")
parser.add_argument("--device_addr", required=True, help="Device port addr")
parser.add_argument("--tag", required=True, help="Tag name")
parser.add_argument("--sleep", default=15, type=int, help="Sleep time")

args = parser.parse_args()
broker_address = args.broker
port = args.port
user = args.user
password = args.password
device_addr = args.device_addr
tag = args.tag
sleep_time = args.sleep

t1_status = Thread(target=inverter8048_status, args=(device_addr, broker_address, port, user, password, tag, sleep_time))

# start the threads
t1_status.start()

# wait for the threads to complete
t1_status.join()
