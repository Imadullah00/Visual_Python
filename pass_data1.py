import time
import serial
arduinoData = serial.Serial('com6', 115200)                      #whatever port you connect your arduino to
time.sleep(1)

while True:
    while(arduinoData.in_waiting == 0):
        pass
    dataPacket = arduinoData.readline()
    dataPacket = str(dataPacket, 'utf-8')
    dataPacket = dataPacket.strip('\r\n')

    splitPacket  = dataPacket.split(",")
    x = float(splitPacket[0])
    y = float(splitPacket[1])
    z = float(splitPacket[2])
    print("X=",x, " " "Y=", y, " " "Z=", z)

    #print(dataPacket)