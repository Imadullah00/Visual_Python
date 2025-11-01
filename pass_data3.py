import time
import serial
from vpython import *
import numpy as np

arrow_length =1
arrow_width = 0.02 

hubL = 0.02
hubR = 0.02

ticklen = 0.1
tickwidth = 0.02
tickhight = 0.02

count = 0

for thetaT in np.linspace(5*np.pi/6, np.pi/6, 6):
    tickmajor = box(color=color.black, pos=vector(arrow_length*np.cos(thetaT), arrow_length*np.sin(thetaT), 0), size=vector(ticklen, tickwidth, tickhight), axis=vector(arrow_length*np.cos(thetaT), arrow_length*np.sin(thetaT), 0))

for thetaU in np.linspace(5*np.pi/6, np.pi/6, 51):
    tickminor = box(color=color.black, pos=vector(arrow_length*np.cos(thetaU), arrow_length*np.sin(thetaU), 0), size=vector(ticklen/2, tickwidth/2, tickhight/2), axis=vector(arrow_length*np.cos(thetaU), arrow_length*np.sin(thetaU), 0))

labF=1.1
for thetaT in np.linspace(5*np.pi/6, np.pi/6, 6):
    lab = text(text = str(count), color=color.black, pos=vector(labF*arrow_length*np.cos(thetaT), labF*arrow_length*np.sin(thetaT), 0), height=0.1, align='center', axis=vector(arrow_length*np.cos(thetaT-np.pi/2), arrow_length*np.sin(thetaT-np.pi/2), 0))
    count = count+1


my_arrow = arrow(Length= arrow_length, shaftwidth=arrow_width, color=color.red,axis=vector(0,1,0))

hub = cylinder(color=color.red, radius=hubR, length=hubL, axis=vector(0,1,0))

boxX = 2.5
boxY = 2
boxZ = 0.1

mycase = box(color=color.white,size=vector(boxX, boxY, boxZ),pos=vector(0,0.9*boxY/2,-boxZ))

mylabel = text(text='Voltmeter', color=color.red, pos=vector(0,1.5,0),height=0.25, align='center' )

arduinoData = serial.Serial('com6', 115200)                 #whatever COM port you are on
time.sleep(1)

while True:
    while(arduinoData.in_waiting == 0):
        pass
    dataPacket  = arduinoData.readline()
    dataPacket = str(dataPacket, 'utf-8')
    dataPacket = int(dataPacket.strip("\r\n"))

    potVal = dataPacket
    theta = ((-2*np.pi)/3069)*potVal + ((5*np.pi)/6)
    my_arrow.axis = vector(arrow_length*np.cos(theta), arrow_length*np.sin(theta), 0)
