import time
import serial
from vpython import *

tube = cylinder(color=color.blue,radius=1, length=5, axis= vector(0,1,0))

arduinoData = serial.Serial('com6', 115200)                 #whatever COM port you are on

time.sleep(1)

lab = label(text = '5Volts', box=False, pos=vector(0,0.2,0))

while True:
    while(arduinoData.in_waiting == 0):
        pass
    dataPacket  = arduinoData.readline()
    dataPacket = str(dataPacket, 'utf-8')
    dataPacket = int(dataPacket.strip("\r\n"))

    voltage = ((dataPacket/1023.0)*5.0) 
    voltage = round(voltage, 2)
    
    if(voltage ==0):
        voltage = 0.001
    tube.length = voltage

    voltage = round(voltage, 2)

    lab.text = str(voltage)+"Volts"

   # print("rawdata=", dataPacket, "Voltage=", voltage, " (V)")
