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
        
    def determineType(voltage1, voltage2):

    if (json_data['joyValX'] <= 4056 and json_data['joyValX'] > 2028):
        mod = 0
    else:
        mod = 3

    if (json_data['joyValY'] <= 4056 and json_data['joyValY'] > 2028):
        mod = 1
    else:
        mod = 2

    if (json_data['joyValY'] <= 4056 and json_data['joyValY'] > 2028):
        mod = 1
    else:
        mod = 2


    a = LFO(freq = freq, type = mod).out()
