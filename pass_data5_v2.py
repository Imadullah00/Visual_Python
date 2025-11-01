import serial
from vpython import *

arduinoData = serial.Serial('com6', 115200)             #whatever com port you are on

ledR=0
ledG=0
ledB=0

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

def update_red(s):
    global ledR
    ledR = int(s.value)
    mylabR.text = f"Red: {ledR}"

def update_green(s):
    global ledG
    ledG = int(s.value)
    mylabG.text = f"Green: {ledG}"

def update_blue(s):
    global ledB
    ledB = int(s.value)
    mylabB.text = f"Blue: {ledB}"

red_slider = slider(min=0, max=255, value=0, length=300, bind=update_red, right=15)
scene.append_to_caption('\n')  # Move to the next line

green_slider = slider(min=0, max=255, value=0, length=300, bind=update_green, right=15)
scene.append_to_caption('\n')  # Move to the next line

blue_slider = slider(min=0, max=255, value=0, length=300, bind=update_blue, right=15)


while True:
    cmd = str(ledR) + ":" + str(ledG) + ":" + str(ledB) + "\r"
    cmd = cmd+'\r'
    arduinoData.write(cmd.encode())

    red = ledR / 255
    green = ledG / 255
    blue = ledB / 255

    myOrb.color = vector(red, green, blue)
    largeCyl.color = vector(red, green, blue)
  
    mylabR.text = str(ledR)
    mylabG.text = str(ledG)
    mylabB.text = str(ledB)

   

    # while(arduinoData.in_waiting == 0):
    #     pass

    # dataPacket  = arduinoData.readline()
    # dataPacket = str(dataPacket, 'utf-8')
    # dataPacket = dataPacket.strip("\r\n")
    # print(dataPacket)