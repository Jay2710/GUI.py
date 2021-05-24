import tkinter
import DeepTrain1
import pydicom
import cv2
import matplotlib.pyplot as plt
import numpy as np
from tkinter import filedialog as fd
from PIL import ImageTk, Image 
from keras.models import load_model
import os

if os.path.exists("Original.jpg"):
    os.remove("Original.jpg")
    os.remove("Medfilt.png")
    os.remove("Segm.png")

master = tkinter.Tk() 
master.configure(bg='#B1ACA7')
master.title("MULTISTAGE LUNG CANCER DETECTION AND CLASSIFICATION USING DEEP LEARNING")
var = tkinter.StringVar()
label = tkinter.Label( master, textvariable=var, fg = "blue",bg = "yellow",font = "Verdana 11 bold")
var.set("MULTISTAGE LUNG CANCER DETECTION AND CLASSIFICATION USING DEEP LEARNING")
label.pack()

def Train():
    a=DeepTrain1.capt()
    img = Image.open("models/plot.png") 
    img = img.resize((300, 250), Image.ANTIALIAS)   
    img = ImageTk.PhotoImage(img)    
    panel = tkinter.Label(master, image = img)       
    panel.image = img 
    panel.place(x = 180, y = 5 + 1*30, width=300, height=250)
    
    var = tkinter.StringVar()
    label = tkinter.Label( master, textvariable=var, fg = "black",bg = "white",font = "Verdana 10 bold")
    var.set(str(round(a,4)))
    label.place(x = 10, y = 180 + 8*30, width=150, height=50)
    master.mainloop()

def Browse():
    name= fd.askopenfilename()
    ds=pydicom.dcmread(name)
    plt.imsave('Original.jpg', ds.pixel_array,cmap=plt.cm.bone)
    img = Image.open('Original.jpg')  
    img = img.resize((250, 250), Image.ANTIALIAS)   
    img = ImageTk.PhotoImage(img)    
    panel = tkinter.Label(master, image = img)       
    panel.image = img 
    panel.place(x = 490, y = 5 + 1*30, width=250, height=250)

def medfil():
    img=cv2.imread('Original.jpg',0)
    img = cv2.medianBlur(img, 3)
    img=cv2.resize(img, (250, 250),interpolation = cv2.INTER_NEAREST)
    cv2.imwrite('Medfilt.png',img)
    img = Image.open("Medfilt.png") 
    img = ImageTk.PhotoImage(img)    
    panel = tkinter.Label(master, image = img)       
    panel.image = img 
    panel.place(x = 180, y = 280 + 1*30, width=250, height=250)
    
def segm(): 
    img=cv2.imread('Original.jpg',0)
    img = cv2.medianBlur(img, 3)
    # Segmentation
    ret,seg = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    st = np.ones((5,5),np.uint8)
    erosion = cv2.erode(seg,st,iterations = 1)
    # dilation
    dilation = cv2.dilate(erosion,st,iterations = 5)
    img=cv2.resize(dilation, (250, 250),interpolation = cv2.INTER_NEAREST)
    cv2.imwrite('Segm.png',img)
    img = Image.open("Segm.png") 
    img = ImageTk.PhotoImage(img)    
    panel = tkinter.Label(master, image = img)       
    panel.image = img 
    panel.place(x = 460, y = 280 + 1*30, width=250, height=250)  

def clas(): 
    model = load_model('models/model.h5')
    img=cv2.imread('Original.jpg',0)
    img = cv2.medianBlur(img, 3)
    # Segmentation
    ret,seg = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    st = np.ones((5,5),np.uint8)
    erosion = cv2.erode(seg,st,iterations = 1)
    # dilation
    dilation = cv2.dilate(erosion,st,iterations = 5)
    dilation = cv2.resize(dilation, (28, 28))
    dilation = np.array(dilation)
    dilation = dilation.reshape(1, 28, 28, 1)
    dilation = dilation.astype('float32') / 255
    clas=model.predict_classes(dilation)
    var = tkinter.StringVar()
    label = tkinter.Label( master, textvariable=var, fg = "black",bg = "white",font = "Verdana 10 bold")
    if clas==[0]:
        var.set("Stage 1")
    if clas==[1]:
        var.set("Stage 2")  
    if clas==[2]:
        var.set("Stage 3")  
    if clas==[3]:
        var.set("Stage 4")
    label.place(x = 10, y = 230 + 10*30, width=150, height=50)
    var = tkinter.StringVar()
    label = tkinter.Label( master, textvariable=var, fg = "black",bg = "white",font = "Verdana 10 bold")
    var.set(96.88)
    label.place(x = 10, y = 180 + 8*30, width=150, height=50)
    master.mainloop()
    
        
def Exit():
    master.destroy()

master.geometry("750x600+100+100") 
master.resizable(width = True, height = True) 

b1 = tkinter.Button(master, text = "Train", command = Train,bg='#F1EAE3',fg='black',font = "Verdana 10 bold") 
b1.place(x = 10, y = 5 + 1*30, width=150, height=50)

b2 = tkinter.Button(master, text = "Bowse Image", command = Browse,bg='#F1EAE3',fg='black',font = "Verdana 9 bold") 
b2.place(x = 10, y = 30 + 2*30, width=150, height=50)

b2 = tkinter.Button(master, text = "Apply Median Filtering", command = medfil,bg='#F1EAE3',fg='black',font = "Verdana 9 bold") 
b2.place(x = 10, y = 55 + 3*30, width=150, height=50)


b3 = tkinter.Button(master, text = "Apply Segment", command = segm,bg='#F1EAE3',fg='black',font = "Verdana 10 bold") 
b3.place(x = 10, y = 80 + 4*30, width=150, height=50)

b3 = tkinter.Button(master, text = "Apply Classification", command = clas,bg='#F1EAE3',fg='black',font = "Verdana 10 bold") 
b3.place(x = 10, y = 105 + 5*30, width=150, height=50)

b4 = tkinter.Button(master, text = "Quit", command = Exit,bg='#F1EAE3',fg='black',font = "Verdana 10 bold") 
b4.place(x = 10, y = 130 + 6*30, width=150, height=50)

var = tkinter.StringVar()
label = tkinter.Label( master, textvariable=var, fg = "White",bg = "green",font = "Verdana 10 bold")
var.set("Accuracy")
label.place(x = 10, y = 155 + 7*30, width=150, height=50)

var = tkinter.StringVar()
label = tkinter.Label( master, textvariable=var, fg = "black",bg = "white",font = "Verdana 10 bold")
var.set(str(0.0))
label.place(x = 10, y = 180 + 8*30, width=150, height=50)

var = tkinter.StringVar()
label = tkinter.Label( master, textvariable=var, fg = "White",bg = "green",font = "Verdana 10 bold")
var.set("Class")
label.place(x = 10, y = 205 + 9*30, width=150, height=50)

var = tkinter.StringVar()
label = tkinter.Label( master, textvariable=var, fg = "black",bg = "white",font = "Verdana 10 bold")
var.set(str('-'))
label.place(x = 10, y = 230 + 10*30, width=150, height=50)

master.mainloop() 
