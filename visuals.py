from vpython import*
import numpy as np

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
mylabG = label(text='Blue', color=color.blue, height=20, xoffset=70)

#my_slider = slider(min=0, max=255, value=100, length=300,right=15, bind=update_color)

while True:
    rate(10)