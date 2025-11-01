import serial
from vpython import *

global_offset = 1.2
myOrb = sphere(color=color.white, radius=0.3, pos=vector(0,0.5+global_offset,0))



largeCyl = cylinder(color=color.yellow, radius=0.3,length=0.6,pos=vector(0,-0.1+global_offset,0),axis=vector(0,1,0))

baseCyl = cylinder(color=color.white, radius=0.4, length=0.05, pos=vector(0,-0.1+global_offset,0),axis=vector(0,1,0))

filCyl1 = cylinder(color=color.red, radius=0.02, length=0.8, pos=vector(-0.3,-0.1+global_offset,0),axis=vector(0,-1,0))
filCyl2 = cylinder(color=color.white, radius=0.02, length=0.9, pos=vector(-0.1,-0.1+global_offset,0),axis=vector(0,-1,0))
filCyl3 = cylinder(color=color.green, radius=0.02, length=0.8, pos=vector(0.1,-0.1+global_offset,0),axis=vector(0,-1,0))
filCyl4 = cylinder(color=color.blue, radius=0.02, length=0.8, pos=vector(0.3,-0.1+global_offset,0),axis=vector(0,-1,0))

mylabR = label(text='Red', color=color.red, height=20, xoffset=-70)
mylabG = label(text='Green', color=color.green, height=20, xoffset=0)
mylabB = label(text='Blue', color=color.blue, height=20, xoffset=70)


arduinoData = serial.Serial('com6', 115200)             #whatever com port you are on


while True:
    cmd = input('Please enter your colour R:G:B(0-255): ')
    cmd = cmd+'\r'
    arduinoData.write(cmd.encode())

    myColor = (cmd.split(':'))
    red = int(myColor[0])/255
    green = int(myColor[1])/255
    blue = int(myColor[2])/255

    myOrb.color = vector(red, green, blue)
    largeCyl.color = vector(red, green, blue)
    
    mylabR.text = str(myColor[0])
    mylabG.text = str(myColor[1])
    mylabB.text = str(myColor[2])

   

    # while(arduinoData.in_waiting == 0):
    #     pass

    # dataPacket  = arduinoData.readline()
    # dataPacket = str(dataPacket, 'utf-8')
    # dataPacket = dataPacket.strip("\r\n")
    # print(dataPacket)