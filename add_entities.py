import os
import time

string_5048 = 'ac_input_voltage 226.4 V ac_input_frequency 50.0 Hz ac_output_voltage 0.0 V ac_output_frequency 0.0 Hz ac_output_apparent_power 0 VA ac_output_active_power 0 W ac_output_load 0 % bus_voltage 393 V battery_voltage 53.4 V battery_charging_current 25 A battery_capacity 52 % inverter_heat_sink_temperature 48 C pv_input_current_for_battery 25.0 A pv_input_voltage 251.8 V battery_voltage_from_scc 0.0 V battery_discharge_current 0 A is_sbu_priority_version_added 0 bool is_configuration_changed 0 bool is_scc_firmware_updated 0 bool is_load_on 0 bool is_battery_voltage_to_steady_while_charging 0 bool is_charging_on 0 bool is_scc_charging_on 1 bool is_ac_charging_on 0 bool rsv1 0 A rsv2 0 A pv_input_power 1597 W is_charging_to_float 0 bool is_switched_on 0 bool is_reserved 0 bool ac_input_voltage 230.0 V ac_input_current 21.7 A ac_output_voltage 230.0 V ac_output_frequency 50.0 Hz ac_output_current 21.7 A ac_output_apparent_power 5000 VA ac_output_active_power 5000 W battery_voltage 48.0 V battery_recharge_voltage 50.0 V battery_under_voltage 48.0 V battery_bulk_charge_voltage 54.8 V battery_float_charge_voltage 54.4 V battery_redischarge_voltage 52.0 V max_ac_charging_current 40 A max_charging_current 80 A max_parallel_units 9 units'
string_5048_split = string_5048.split(' ')

string_5048_wo = 'device_mode Line battery_type User input_voltage_range UPS output_source_priority SBU charger_source_priority Only machine_type Off topology transformerless output_mode single inverter_fault 0 bus_over_fault 0 bus_under_fault 0 bus_soft_fail_fault 0 line_fail_warning 0 opv_short_warning 0 inverter_voltage_too_low_fault 0 inverter_voltage_too_high_fault 0 over_temperature_fault 0 fan_locked_fault 0 battery_voltage_to_high_fault 0 battery_low_alarm_warning 0 reserved 0 battery_under_shutdown_warning 0 overload_fault 0 eeprom_fault 0 inverter_over_current_fault 0 inverter_soft_fail_fault 0 self_test_fail_fault 0 op_dc_voltage_over_fault 0 bat_open_fault 0 current_sensor_fail_fault 0 battery_short_fault 0 power_limit_warning 0 pv_voltage_high_warning 0 mppt_overload_fault 0 mppt_overload_warning 0 battery_too_low_to_charge_warning 0'
string_5048_wo_split = string_5048_wo.split(' ')


string_8048 = 'ac_input_voltage 221.5 V ac_input_frequency 50.0 Hz ac_output_voltage 230.3 V ac_output_frequency 49.9 Hz ac_output_apparent_power 0 VA ac_output_active_power 0 W ac_output_load 0 % bus_voltage 426 V battery_voltage 54.3 V battery_charging_current 76 A battery_capacity 71 % inverter_heat_sink_temperature 62 C pv1_input_current 7.1 A pv1_input_voltage 289.6 V battery_voltage_from_scc 0.0 V battery_discharge_current 0 A is_sbu_priority_version_added 0 bool is_configuration_changed 0 bool is_scc_firmware_updated 0 bool is_load_on 1 bool is_battery_voltage_to_steady_while_charging 0 bool is_charging_on 1 bool is_scc_charging_on 1 bool is_ac_charging_on 0 bool battery_voltage_offset_for_fans_on 0 10mV eeprom_version 0 V pv1_charging_power 2070 W is_charging_to_float 0 bool is_switched_on 1 bool is_dustproof_installed 0 bool pv2_input_current 7 A pv2_input_voltage 22 V pv2_charging_power 232 W ac_input_voltage 230.0 V ac_input_current 34.7 A ac_output_voltage 230.0 V ac_output_frequency 50.0 Hz ac_output_current 34.7 A ac_output_apparent_power 8000 VA ac_output_active_power 8000 W battery_voltage 48.0 V battery_recharge_voltage 51.0 V battery_under_voltage 47.0 V battery_bulk_charge_voltage 54.8 V battery_float_charge_voltage 54.4 V battery_redischarge_voltage 53.0 V max_ac_charging_current 10 A max_charging_current 120 A max_parallel_units 9 units'
string_8048_split = string_8048.split(' ')

string_8048_wo = 'device_mode Line inverter_charge_status absorb pv_loss_warning 0 inverter_fault 0 bus_over_fault 0 bus_under_fault 0 bus_soft_fail_fault 0 line_fail_warning 0 opv_short_warning 0 inverter_voltage_too_low_fault 0 inverter_voltage_too_high_fault 0 over_temperature_fault 0 fan_locked_fault 0 battery_voltage_to_high_fault 0 battery_low_alarm_warning 0 reserved 0 battery_under_shutdown_warning 0 battery_derating_warning 0 overload_fault 0 eeprom_fault 0 inverter_over_current_fault 0 inverter_soft_fail_fault 0 self_test_fail_fault 0 op_dc_voltage_over_fault 0 bat_open_fault 0 current_sensor_fail_fault 0 battery_short_fault 0 power_limit_warning 0 pv_voltage_high_warning 0 mppt_overload_fault 0 mppt_overload_warning 0 battery_too_low_to_charge_warning 0 battery_weak 0 battery_equalisation_warning 0'
string_8048_wo_split = string_8048_wo.split(' ')

while True:
    #### 5048 1 start
    for i in range(len(string_5048_split)//3):
        print(string_5048_split[i*3], string_5048_split[(3*i)+2])
        txt = "mosquitto_pub -r -h 192.168.1.102 -u sonoff -P sonoff -t \"homeassistant/sensor/mppsolar_5048_1_{}/config\" -m \'{{\"name\": \"MPP-Solar_5048_1_{}\", \"state_topic\": \"inver1/status/{}/value\", \"unit_of_measurement\": \"{}\"" + "}}'"
        # print(txt.format(string_8048_split[i*3], string_8048_split[i*3], string_8048_split[i*3], string_8048_split[i*3+2]))
        jadi = txt.format(string_5048_split[i*3], string_5048_split[i*3], string_5048_split[i*3], string_5048_split[i*3+2])
        print(jadi)
        os.system(jadi)
        time.sleep(1)
        print("\n\n")

    for q in range(len(string_5048_wo_split)//2):
        print(string_5048_wo_split[q*2])
        txt_ = "mosquitto_pub -r -h 192.168.1.102 -u sonoff -P sonoff -t \"homeassistant/sensor/mppsolar_5048_1_{}/config\" -m \'{{\"name\": \"MPP-Solar_5048_1_{}\", \"state_topic\": \"inver1/status/{}/value\"}}'"
        jadi_ = txt_.format(string_5048_wo_split[q*2], string_5048_wo_split[q*2], string_5048_wo_split[q*2])
        print(jadi_)
        os.system(jadi_)
        time.sleep(1)
        print("\n\n")

    #### 5048 1 end

    #### 5048 2 start

    for i in range(len(string_5048_split)//3):
        print(string_5048_split[i*3], string_5048_split[(3*i)+2])
        txt = "mosquitto_pub -r -h 192.168.1.102 -u sonoff -P sonoff -t \"homeassistant/sensor/mppsolar_5048_2_{}/config\" -m \'{{\"name\": \"MPP-Solar_5048_2_{}\", \"state_topic\": \"inver2/status/{}/value\", \"unit_of_measurement\": \"{}\"" + "}}'"
        # print(txt.format(string_8048_split[i*3], string_8048_split[i*3], string_8048_split[i*3], string_8048_split[i*3+2]))
        jadi = txt.format(string_5048_split[i*3], string_5048_split[i*3], string_5048_split[i*3], string_5048_split[i*3+2])
        print(jadi)
        os.system(jadi)
        time.sleep(1)
        print("\n\n")

    for q in range(len(string_5048_wo_split)//2):
        print(string_5048_wo_split[q*2])
        txt_ = "mosquitto_pub -r -h 192.168.1.102 -u sonoff -P sonoff -t \"homeassistant/sensor/mppsolar_5048_2_{}/config\" -m \'{{\"name\": \"MPP-Solar_5048_2_{}\", \"state_topic\": \"inver2/status/{}/value\"}}'"
        jadi_ = txt_.format(string_5048_wo_split[q*2], string_5048_wo_split[q*2], string_5048_wo_split[q*2])
        print(jadi_)
        os.system(jadi_)
        time.sleep(1)
        print("\n\n")

    #### 5048 2 end


    #### 8048 start

    for q in range(len(string_8048_wo_split)//2):
        print(string_8048_wo_split[q*2])
        txt_ = "mosquitto_pub -r -h 192.168.1.102 -u sonoff -P sonoff -t \"homeassistant/sensor/mppsolar_8048_{}/config\" -m \'{{\"name\": \"MPP-Solar_8084_{}\", \"state_topic\": \"inver4/status/{}/value\"}}'"
        jadi_ = txt_.format(string_8048_wo_split[q*2], string_8048_wo_split[q*2], string_8048_wo_split[q*2])
        print(jadi_)
        os.system(jadi_)
        time.sleep(1)
    
    for i in range(len(string_8048_split)//3):
        print(string_8048_split[i*3], string_8048_split[(3*i)+2])
        txt = "mosquitto_pub -r -h 192.168.1.102 -u sonoff -P sonoff -t \"homeassistant/sensor/mppsolar_8048_{}/config\" -m \'{{\"name\": \"MPP-Solar_8084_{}\", \"state_topic\": \"inver4/status/{}/value\", \"unit_of_measurement\": \"{}\"" + "}}'"
        # print(txt.format(string_8048_split[i*3], string_8048_split[i*3], string_8048_split[i*3], string_8048_split[i*3+2]))
        jadi = txt.format(string_8048_split[i*3], string_8048_split[i*3], string_8048_split[i*3], string_8048_split[i*3+2])
        print(jadi)
        os.system(jadi)
        time.sleep(1)
        print("\n\n")

    #### 8048 end

    time.sleep(60*10)

