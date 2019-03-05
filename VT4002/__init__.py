import serial
import time
import json
READ_ACTUAL_VAL = "I"

class VT4002:
    def __init__(self, raw_data):
        parsed_output = raw_data.split(" ");
        self.nominal_value_1 = parsed_output[0] # Nominal value of control variable 1
        self.actual_value_1 = parsed_output[1] # Actual value of control variable 1
        self.nominal_value_2 = parsed_output[2] # Nominal value of control variable 2
        self.actual_value_2 = parsed_output[3] # Actual value of control variable 2
        self.ctrl_value_1 = parsed_output[4] # Control value 1
        self.ctrl_value_2 = parsed_output[5] # Control value 2
        self.actual_value_Pt100_1 = parsed_output[7] # Actual value Pt100-1 (°C, analog I/O card)1)
        self.actual_value_Pt100_2 = parsed_output[9] # Actual value Pt100-2 (°C, analog I/O card)1)
        self.actual_value_Pt100_3 = parsed_output[11] # Actual value Pt100-3 (°C, analog I/O card)1)
        self.actual_value_Pt100_4 = parsed_output[13] # Actual value Pt100-4 (°C, analog I/O card)1)
        self.digital_output = parsed_output[14] # Digital output

    def temp1_nominal(self):
        return float(self.nominal_value_1)
    def temp1_actual(self):
        return float(self.actual_value_1)
    def temp2_nominal(self):
        return float(self.nominal_value_2)
    def temp2_actual(self):
        return float(self.actual_value_2)

class Connection:
    def __init__(self, port, baudrate=9600, chamber_address="00", timeout_s=5):
        self.port=port
        self.baudrate=baudrate
        self.timeout=timeout_s
        self.ser = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
        self.chamber_address = chamber_address
    def __del__(self):
        self.ser.close()
    def _serial_read(self):
        try:
            return self.ser.readline().decode()
        except UnicodeDecodeError:
            return ""
    def _serial_write(self, data):
        self.ser.write(data.encode('utf-8'))

    def get_actual_values(self):
        self._serial_write(("$"+self.chamber_address+READ_ACTUAL_VAL+"\r\n"))
        reading = self._serial_read()
        try:
            return VT4002(reading)
        except IndexError:
            return self.get_actual_values()
