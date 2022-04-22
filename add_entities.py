import os
import time

string_to_ext = 'ac_input_voltage 221.5 V ac_input_frequency 50.0 Hz ac_output_voltage 230.3 V ac_output_frequency 49.9 Hz ac_output_apparent_power 0 VA ac_output_active_power 0 W ac_output_load 0 % bus_voltage 426 V battery_voltage 54.3 V battery_charging_current 76 A battery_capacity 71 % inverter_heat_sink_temperature 62 C pv1_input_current 7.1 A pv1_input_voltage 289.6 V battery_voltage_from_scc 0.0 V battery_discharge_current 0 A is_sbu_priority_version_added 0 bool is_configuration_changed 0 bool is_scc_firmware_updated 0 bool is_load_on 1 bool is_battery_voltage_to_steady_while_charging 0 bool is_charging_on 1 bool is_scc_charging_on 1 bool is_ac_charging_on 0 bool battery_voltage_offset_for_fans_on 0 10mV eeprom_version 0 V pv1_charging_power 2070 W is_charging_to_float 0 bool is_switched_on 1 bool is_dustproof_installed 0 bool pv2_input_current 7 A pv2_input_voltage 22 V pv2_charging_power 232 W'
# string_to_ext = 'ac_input_voltage 221.5 V ac_input_frequency 50.0 Hz ac_output_voltage 230.3 V ac_output_frequency 49.9 Hz ac_output_apparent_power 0 VA ac_output_active_power 0 W ac_output_load 0 % bus_voltage 426 V battery_voltage 54.3 V battery_charging_current 76 A battery_capacity 71 % inverter_heat_sink_temperature 62 C pv1_input_current 7.1 A pv1_input_voltage 289.6 V battery_voltage_from_scc 0.0 V battery_discharge_current 0 A is_sbu_priority_version_added 0 bool is_configuration_changed 0 bool is_scc_firmware_updated 0 bool is_load_on 1 bool is_battery_voltage_to_steady_while_charging 0 bool is_charging_on 1 bool is_scc_charging_on 1 bool is_ac_charging_on 0 bool battery_voltage_offset_for_fans_on 0 10mV'
spliiter = string_to_ext.split(' ')


without_unit = 'device_mode Line inverter_charge_status absorb'
without_unit_split = without_unit.split(' ')

while True:
    for q in range(len(without_unit_split)//2):
        txt_ = "mosquitto_pub -r -h 192.168.1.102 -u sonoff -P sonoff -t \"homeassistant/sensor/mppsolar_8048_{}/config\" -m \'{{\"name\": \"MPP-Solar_8084_{}\", \"state_topic\": \"inver4/status/{}/value\"}}'"
        jadi_ = txt_.format(without_unit_split[q*2], without_unit_split[q*2], without_unit_split[q*2])
        print(jadi_)
        os.system(jadi_)
        time.sleep(1)
    
    for i in range(len(spliiter)//3):
        # print(spliiter[i*3], spliiter[(3*i)+2])
        txt = "mosquitto_pub -r -h 192.168.1.102 -u sonoff -P sonoff -t \"homeassistant/sensor/mppsolar_8048_{}/config\" -m \'{{\"name\": \"MPP-Solar_8084_{}\", \"state_topic\": \"inver4/status/{}/value\", \"unit_of_measurement\": \"{}\"" + "}}'"
        # print(txt.format(spliiter[i*3], spliiter[i*3], spliiter[i*3], spliiter[i*3+2]))
        jadi = txt.format(spliiter[i*3], spliiter[i*3], spliiter[i*3], spliiter[i*3+2])
        print(jadi)
        os.system(jadi)
        time.sleep(1)

    time.sleep(60*5)

