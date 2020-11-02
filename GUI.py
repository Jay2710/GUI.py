import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

if os.path.isfile('save1.txt'):
      with open('save1.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename= filedialog.askopenfilename(initialdir="/",title="Select File",
                                         filetypes=(("executables", "*.exe"),("all files","*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()   

def runApps():
    for app in apps:
        os.startfile(app)


def deleteapps():
    
    for widget in frame.winfo_children():
       widget.destroy()
    

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

openfile = tk.Button(root, text="open File", padx="10", pady="5", fg="White", bg="#263D42", command=addApp)
openfile.pack()
runApps = tk.Button(root, text="Run apps", pady="10", padx="5", fg="White", bg="#263D42", command=runApps)
runApps.pack()
deleteapps = tk.Button(root, text="Delete apps", pady="10", padx="5", fg="White", bg="#263D42", command=deleteapps)
deleteapps.pack()


for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('save1.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
        os.remove('save1.txt')
        print("Saved file deleted") 


