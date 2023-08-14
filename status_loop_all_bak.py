
import os
import time

from threading import Thread

counter_another_status = 0

def inverter1_status():
    ############## 5048 1 #############
    while True:
        print("PUSH 5048 1")
        os.system("mpp-solar -p /dev/hidraw0 -c QPIGS -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver1 -o mqtt")
        time.sleep(0.5)
        os.system("mpp-solar -p /dev/hidraw0 -c QMOD -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver1 -o mqtt")
        time.sleep(0.5)
        os.system("mpp-solar -p /dev/hidraw0 -c QPIGS -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver1 -o mqtt")
        time.sleep(0.5)
        os.system("mpp-solar -p /dev/hidraw0 -c QMOD -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver1 -o mqtt")
        time.sleep(0.5)
        print("PUSH 5048 1 Done")

        os.system("mpp-solar -p /dev/hidraw0 -c QPIWS -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver1 -o mqtt")
        time.sleep(0.5)
        os.system("mpp-solar -p /dev/hidraw0 -c QPIRI -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver1_conf -o mqtt")
        time.sleep(0.5)
        os.system("mpp-solar -p /dev/hidraw0 -c QPIRI -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver1_conf -o mqtt")
        time.sleep(0.5)

        print("PUSH 5048 1 conf Done")


    ############## 5048 1 #############

def inverter2_status():
    ############## 5048 2 #############
    while True:
        print("\t\tPUSH 5048 2")
        os.system("mpp-solar -p /dev/hidraw1 -c QPIGS -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver2 -o mqtt")
        time.sleep(0.5)
        os.system("mpp-solar -p /dev/hidraw1 -c QMOD -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver2 -o mqtt")
        time.sleep(0.5)
        os.system("mpp-solar -p /dev/hidraw1 -c QPIGS -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver2 -o mqtt")
        time.sleep(0.5)
        os.system("mpp-solar -p /dev/hidraw1 -c QMOD -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver2 -o mqtt")
        time.sleep(0.5)
        print("\t\tPUSH 5048 2 Done")
        ############## 5048 2 #############

        os.system("mpp-solar -p /dev/hidraw1 -c QPIWS -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver2 -o mqtt")
        time.sleep(0.5)
        os.system("mpp-solar -p /dev/hidraw1 -c QPIRI -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver2_conf -o mqtt")
        time.sleep(0.5)
        os.system("mpp-solar -p /dev/hidraw1 -c QPIRI -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver2_conf -o mqtt")
        time.sleep(0.5)
        print("\t\tPUSH 5048 2 conf Done")



def inverter3_status():
    while True:
        ############## 8048 #############
        print("\t\t\t\tPUSH 8048")
        os.system("mpp-solar -p /dev/ttyUSB0 -c QPIGS -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver3 -P PI30MAX -o mqtt")
        time.sleep(0.5)
        os.system("mpp-solar -p /dev/ttyUSB0 -c QPIGS2 -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver3 -P PI30MAX -o mqtt")
        time.sleep(0.5)
        os.system("mpp-solar -p /dev/ttyUSB0 -c QMOD -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver3 -P PI30MAX -o mqtt")
        time.sleep(0.5)
        os.system("mpp-solar -p /dev/ttyUSB0 -c Q1 -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver3 -P PI30 -o mqtt")
        time.sleep(0.5)
        print("\t\t\t\tPUSH 8048 done")
        ############## 8048 #############
        os.system("mpp-solar -p /dev/ttyUSB0 -c QPIWS -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver3 -P PI30MAX -o mqtt")
        time.sleep(0.5)
        os.system("mpp-solar -p /dev/ttyUSB0 -c QPIRI -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver3_conf -P PI30 -o mqtt")
        time.sleep(0.5)
        print("\t\t\t\tPUSH 8048 conf done")

def inverter5_status():
    while True:
        ############## 8048 #############
        print("\t\t\t\tPUSH 8048")
        os.system("mpp-solar -p /dev/ttyUSB0 -c QPIGS -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver4 -P PI30MAX -o mqtt")
        time.sleep(0.5)
        os.system("mpp-solar -p /dev/ttyUSB0 -c QPIGS2 -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver4 -P PI30MAX -o mqtt")
        time.sleep(0.5)
        os.system("mpp-solar -p /dev/ttyUSB0 -c QMOD -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver4 -P PI30MAX -o mqtt")
        time.sleep(0.5)
        os.system("mpp-solar -p /dev/ttyUSB0 -c Q1 -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver4 -P PI30 -o mqtt")
        time.sleep(0.5)
        print("\t\t\t\tPUSH 8048 done")
        ############## 8048 #############
        os.system("mpp-solar -p /dev/ttyUSB0 -c QPIWS -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver4 -P PI30MAX -o mqtt")
        time.sleep(0.5)
        os.system("mpp-solar -p /dev/ttyUSB0 -c QPIRI -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver4_conf -P PI30 -o mqtt")
        time.sleep(0.5)
        print("\t\t\t\tPUSH 8048 conf done")


t1_status = Thread(target=inverter1_status)
t2_status = Thread(target=inverter2_status)
t3_status = Thread(target=inverter3_status)
t5_status = Thread(target=inverter5_status)

# start the threads
t1_status.start()
t2_status.start()
t3_status.start()
t5_status.start()

# wait for the threads to complete
t1_status.join()
t2_status.join()
t3_status.join()
t5_status.join()

# while True:

#     if counter_another_status >= 1:
#         print("PUSH Another")

        

    


#         print("PUSH Another Done")

#         counter_another_status = 0
#     else:
#         counter_another_status += 1

#     # print("SLEEP 20s")
#     # time.sleep(20)

