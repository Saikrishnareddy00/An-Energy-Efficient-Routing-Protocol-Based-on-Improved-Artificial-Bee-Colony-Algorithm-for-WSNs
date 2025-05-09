import tkinter
from tkinter import *
import math
import random
from threading import Thread 
from collections import defaultdict
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
import time

global mobile
global labels
global mobile_x
global mobile_y
global text
global canvas
global mobile_list
global ch1,ch2,ch3
global line1,line2,line3
option = 0
global root
global path_length

def fitnessFunction(iot_x,iot_y,x1,y1):
    flag = False
    for i in range(len(iot_x)):
        dist = math.sqrt((iot_x[i] - x1)*2 + (iot_y[i] - y1)*2)
        if dist < 80:
            flag = True
            break
    return flag

    
def startDataTransferSimulation(text,canvas,line1,line2,line3,x1,y1,x2,y2,x3,y3):
    class SimulationThread(Thread):
        def _init_(self,text,canvas,line1,line2,line3,x1,y1,x2,y2,x3,y3): 
            Thread._init_(self) 
            self.canvas = canvas
            self.line1 = line1
            self.line2 = line2
            self.line3 = line3
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2
            self.x3 = x3
            self.y3 = y3
            self.text = text
            
 
        def run(self):
            time.sleep(1)
            for i in range(0,3):
                self.canvas.delete(self.line1)
                self.canvas.delete(self.line2)
                self.canvas.delete(self.line3)
                time.sleep(1)
                self.line1 = canvas.create_line(self.x1, self.y1,self.x2, self.y2,fill='black',width=3)
                self.line2 = canvas.create_line(self.x2, self.y2,self.x3, self.y3,fill='black',width=3)
                self.line3 = canvas.create_line(self.x3, self.y3,25, 370,fill='black',width=3)
                time.sleep(1)
            self.canvas.delete(self.line1)
            self.canvas.delete(self.line2)
            self.canvas.delete(self.line3)
            canvas.update()
                
    newthread = SimulationThread(text,canvas,line1,line2,line3,x1,y1,x2,y2,x3,y3) 
    newthread.start()
    
    
def generate():
    global mobile
    global labels
    global mobile_x
    global mobile_y
    mobile = []
    mobile_x = []
    mobile_y = []
    labels = []
    canvas.update()
    x = 5
    y = 350
    mobile_x.append(x)
    mobile_y.append(y)
    name = canvas.create_oval(x,y,x+40,y+40, fill="blue")
    lbl = canvas.create_text(x+20,y-10,fill="darkblue",font="Times 7 italic bold",text="Base Station")
    labels.append(lbl)
    mobile.append(name)

    for i in range(1,20):
        run = True
        while run == True:
            x = random.randint(100, 450)
            y = random.randint(50, 600)
            flag = fitnessFunction(mobile_x,mobile_y,x,y)
            if flag == False:
                mobile_x.append(x)
                mobile_y.append(y)
                run = False
                name = canvas.create_oval(x,y,x+40,y+40, fill="red")
                lbl = canvas.create_text(x+20,y-10,fill="darkblue",font="Times 8 italic bold",text="Node "+str(i))
                labels.append(lbl)
                mobile.append(name)
    

def initializeCGTABC1():
    text.delete('1.0', END)
    global ch1,ch2,ch3
    distance = 10000
    for i in range(1,20): #loop all bees
        x1 = mobile_x[i] #on worker bee location means node location
        y1 = mobile_y[i]
        fitness = math.sqrt((x1 - 5)*2 + (y1 - 350)*2) #calculate fitness
        if fitness < distance and y1 > 5 and y1 < 200: #if source nectar has more food or node is having close distance
            distance = fitness
            ch1 = i #find cluster head closer to base station as extension concept
    print(distance)        
    distance = 10000
    for i in range(1,20):
        x1 = mobile_x[i]
        y1 = mobile_y[i]
        fitness = math.sqrt((x1 - 5)*2 + (y1 - 350)*2)
        if fitness < distance and i != ch1 and y1 > 250 and y1 <= 350 :
            distance = fitness
            ch2 = i
    print(distance)
    distance = 10000
    for i in range(1,20):
        x1 = mobile_x[i]
        y1 = mobile_y[i]
        fitness = math.sqrt((x1 - 5)*2 + (y1 - 350)*2)
        if fitness < distance and i != ch1 and i != ch2 and y1 > 450 and y1 < 650:
            distance = fitness
            ch3 = i
    print(distance)
                
    text.insert(END,"Selected Cluster Head 1 is : "+str(ch1)+"\n")
    text.insert(END,"Selected Cluster Head 2 is : "+str(ch2)+"\n")
    text.insert(END,"Selected Cluster Head 3 is : "+str(ch3)+"\n")
    canvas.delete(mobile[ch1])
    canvas.delete(mobile[ch2])
    canvas.delete(mobile[ch3])
    canvas.delete(labels[ch1])
    canvas.delete(labels[ch2])
    canvas.delete(labels[ch3])
    name = canvas.create_oval(mobile_x[ch1],mobile_y[ch1],mobile_x[ch1]+40,mobile_y[ch1]+40, fill="green")
    mobile[ch1] = name
    name = canvas.create_oval(mobile_x[ch2],mobile_y[ch2],mobile_x[ch2]+40,mobile_y[ch2]+40, fill="green")
    mobile[ch2] = name
    name = canvas.create_oval(mobile_x[ch3],mobile_y[ch3],mobile_x[ch3]+40,mobile_y[ch3]+40, fill="green")
    mobile[ch3] = name
    lbl = canvas.create_text(mobile_x[ch1]+20,mobile_y[ch1]-10,fill="green",font="Times 10 italic bold",text="CH1-"+str(ch1))
    labels[ch1] = lbl
    lbl = canvas.create_text(mobile_x[ch2]+20,mobile_y[ch2]-10,fill="green",font="Times 10 italic bold",text="CH2-"+str(ch2))
    labels[ch2] = lbl
    lbl = canvas.create_text(mobile_x[ch3]+20,mobile_y[ch3]-10,fill="green",font="Times 10 italic bold",text="CH3-"+str(ch3))
    labels[ch3] = lbl

    canvas.create_oval(50,5,500,245)
    canvas.create_oval(50,240,500,450)
    canvas.create_oval(50,430,500,670)
    
    canvas.update()

def CGTABC2Algorithm():
    global option
    global path_length
    global line1,line2,line3
    text.delete('1.0', END)
    src = int(mobile_list.get())
    if option == 1:
        canvas.delete(line1)
        canvas.delete(line2)
        canvas.delete(line3)
        canvas.update()
    src_x = mobile_x[src]
    src_y = mobile_y[src]
    distance = 10000
    hop = 0
    selected_cluster = 0
    for i in range(1,20):
        temp_x = mobile_x[i]
        temp_y = mobile_y[i]
        if i != src and i != ch1 and i != ch2 and i != ch3 and temp_x < src_x:
            dist = math.sqrt((src_x - temp_x)*2 + (src_y - temp_y)*2)
            if dist < distance:
                distance = dist
                hop = i
    if hop != 0:
        hop_x = mobile_x[hop]
        hop_y = mobile_y[hop]
        distance1 = math.sqrt((hop_x - mobile_x[ch1])*2 + (hop_y - mobile_y[ch1])*2)
        distance2 = math.sqrt((hop_x - mobile_x[ch2])*2 + (hop_y - mobile_y[ch2])*2)
        distance3 = math.sqrt((hop_x - mobile_x[ch3])*2 + (hop_y - mobile_y[ch3])*2)
        if distance1 <= distance2 and distance1 <= distance3: #select optimize cluster head closer to base station base on location and energy
            selected_cluster = ch1
            path_length = distance1
        elif distance2 <= distance1 and distance2 <= distance3:
            selected_cluster = ch2
            path_length = distance2
        else:
            selected_cluster = ch3
            path_length = distance3
    if selected_cluster != 0 and hop != 0:
        text.insert(END,"Selected Source Node is : "+str(src)+"\n")
        text.insert(END,"Selected HOP Node is : "+str(hop)+"\n")
        text.insert(END,"Selected Nearest Optimize cluster head is : "+str(selected_cluster)+"\n")
        line1 = canvas.create_line(mobile_x[src]+20, mobile_y[src]+20,mobile_x[hop]+20, mobile_y[hop]+20,fill='black',width=3)
        line2 = canvas.create_line(mobile_x[hop]+20, mobile_y[hop]+20,mobile_x[selected_cluster]+20, mobile_y[selected_cluster]+20,fill='black',width=3)
        line3 = canvas.create_line(mobile_x[selected_cluster]+20, mobile_y[selected_cluster]+20,mobile_x[0]+20, mobile_y[0]+20,fill='black',width=3)
        startDataTransferSimulation(text,canvas,line1,line2,line3,(mobile_x[src]+20),(mobile_y[src]+20),(mobile_x[hop]+20),(mobile_y[hop]+20),(mobile_x[selected_cluster]+20),(mobile_y[selected_cluster]+20))
        option = 1
        
    else:
        text.insert(END,"No next hop path found. Try another source\n")
            
   
 
if _name== 'main_' :
    Main ()
