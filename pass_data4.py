import serial

arduinoData = serial.Serial('com6', 115200)             #whatever com port you are on

while True:
    cmd = input('Please enter your command ')
    cmd = cmd+'\r'
    arduinoData.write(cmd.encode())

    while(arduinoData.in_waiting == 0):
        pass

    dataPacket  = arduinoData.readline()
    dataPacket = str(dataPacket, 'utf-8')
    dataPacket = dataPacket.strip("\r\n")
    print(dataPacket)
    

