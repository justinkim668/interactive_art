import serial
from pyo import *

ser = serial.Serial('/dev/cu.usbserial-023E572B', 115200)


while(True):
  print(str(ser.readline().strip(), 'ascii'))
