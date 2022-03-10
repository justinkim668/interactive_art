import serial
from pyo import *

ser = serial.Serial('/dev/cu.usbserial-023E572B', 115200)
s = Server().boot()
s.start()


while(True):
    a = Sine().out()
    print(str(ser.readline().strip(), 'ascii'))
