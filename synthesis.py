import serial
import json
import ast
from pyo import *

s = Server().boot()
s.start()
ser = serial.Serial('/dev/cu.usbserial-023E572B', 115200)

while(True):
    json_input = str(ser.readline().strip(), "ascii")
    json_data = json.loads(json_input)
    freq = json_data['potValue']/4
    mod = 0

    if (json_data['joyValSW'] == 0):
        a = SuperSaw(freq = freq).out()
    else:
        if (json_data['joyValX'] == 0):
            mod = 0
        elif(json_data['joyValX'] == 4056):
            mod = 3
        elif(json_data['joyValY'] == 0):
            mod = 1
        elif(json_data['joyValY'] == 4056):
            mod = 2

        a = LFO(freq = freq, type = mod).out()
    print(json_data)
