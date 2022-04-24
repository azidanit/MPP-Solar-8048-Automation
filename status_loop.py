from itertools import count
import os
import time

counter_another_status = 0

while True:
    ############## 8048 #############
    print("PUSH 8048")
    os.system("mpp-solar -p /dev/ttyUSB0 -c QPIGS -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver4 -P PI30MAX -o mqtt")
    time.sleep(0.5)
    os.system("mpp-solar -p /dev/ttyUSB0 -c QPIGS2 -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver4 -P PI30MAX -o mqtt")
    time.sleep(0.5)
    os.system("mpp-solar -p /dev/ttyUSB0 -c QMOD -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver4 -P PI30MAX -o mqtt")
    time.sleep(0.5)
    os.system("mpp-solar -p /dev/ttyUSB0 -c Q1 -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver4 -P PI30 -o mqtt")
    time.sleep(0.5)
    print("PUSH 8048 done")
    ############## 8048 #############

    ############## 5048 1 #############
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

    ############## 5048 1 #############

    ############## 5048 2 #############
    print("PUSH 5048 1")
    os.system("mpp-solar -p /dev/hidraw1 -c QPIGS -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver2 -o mqtt")
    time.sleep(0.5)
    os.system("mpp-solar -p /dev/hidraw1 -c QMOD -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver2 -o mqtt")
    time.sleep(0.5)
    os.system("mpp-solar -p /dev/hidraw1 -c QPIGS -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver2 -o mqtt")
    time.sleep(0.5)
    os.system("mpp-solar -p /dev/hidraw1 -c QMOD -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver2 -o mqtt")
    time.sleep(0.5)
    print("PUSH 5048 2 Done")


    ############## 5048 2 #############

    if counter_another_status >= 1:
        print("PUSH Another")

        os.system("mpp-solar -p /dev/ttyUSB0 -c QPIWS -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver4 -P PI30MAX -o mqtt")
        time.sleep(0.5)
        os.system("mpp-solar -p /dev/ttyUSB0 -c QPIRI -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver4_conf -P PI30 -o mqtt")
        time.sleep(0.5)

    
        os.system("mpp-solar -p /dev/hidraw0 -c QPIWS -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver1 -o mqtt")
        time.sleep(0.5)
        os.system("mpp-solar -p /dev/hidraw0 -c QPIRI -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver1_conf -o mqtt")
        time.sleep(0.5)

        os.system("mpp-solar -p /dev/hidraw1 -c QPIWS -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver2 -o mqtt")
        time.sleep(0.5)
        os.system("mpp-solar -p /dev/hidraw1 -c QPIRI -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver2_conf -o mqtt")
        time.sleep(0.5)
        print("PUSH Another Done")

        counter_another_status = 0
    else:
        counter_another_status += 1

    # print("SLEEP 20s")
    # time.sleep(20)

