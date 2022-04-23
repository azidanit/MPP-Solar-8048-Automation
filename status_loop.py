import os
import time

while True:
    ############## 8048 #############
    os.system("mpp-solar -p /dev/ttyUSB0 -c QPIGS -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver4 -P PI30MAX -o mqtt")
    time.sleep(1)
    os.system("mpp-solar -p /dev/ttyUSB0 -c QPIGS2 -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver4 -P PI30MAX -o mqtt")
    time.sleep(1)
    os.system("mpp-solar -p /dev/ttyUSB0 -c QMOD -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver4 -P PI30MAX -o mqtt")
    time.sleep(1)
    os.system("mpp-solar -p /dev/ttyUSB0 -c Q1 -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver4 -P PI30 -o mqtt")
    time.sleep(1)
    os.system("mpp-solar -p /dev/ttyUSB0 -c QPIWS -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver4 -P PI30MAX -o mqtt")
    time.sleep(1)
    os.system("mpp-solar -p /dev/ttyUSB0 -c QPIRI -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver4 -P PI30 -o mqtt")
    ############## 8048 #############

    ############## 5048 1 #############
    os.system("mpp-solar -p /dev/hidraw0 -c QPIGS -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver1 -o mqtt")
    time.sleep(1)
    os.system("mpp-solar -p /dev/hidraw0 -c QMOD -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver1 -o mqtt")
    time.sleep(1)
    os.system("mpp-solar -p /dev/hidraw0 -c QPIWS -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver1 -o mqtt")
    time.sleep(1)
    os.system("mpp-solar -p /dev/hidraw0 -c QPIRI -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver1 -o mqtt")
    ############## 5048 1 #############

    ############## 5048 2 #############
    os.system("mpp-solar -p /dev/hidraw1 -c QPIGS -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver2 -o mqtt")
    time.sleep(1)
    os.system("mpp-solar -p /dev/hidraw1 -c QMOD -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver2 -o mqtt")
    time.sleep(1)
    os.system("mpp-solar -p /dev/hidraw1 -c QPIWS -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver2 -o mqtt")
    time.sleep(1)
    os.system("mpp-solar -p /dev/hidraw1 -c QPIRI -q 192.168.1.102 --mqttuser sonoff --mqttpass sonoff --tag inver2 -o mqtt")
    ############## 5048 2 #############

    time.sleep(15)

