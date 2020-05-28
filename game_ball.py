
from tkinter import *
import tkinter as tk
import random as rnd
import math
from PIL import ImageTk, Image

root = tk.Tk()
canvas = tk.Canvas(root, height=999, width=999, bg='blue')
canvas.pack()


 
m=[10]
root.geometry('850x450')
root.resizable(width=False, height=False)
# def motion(event):
    # x, y = event.x, event.y
    # print('{}, {}'.format(x, y))

# root.bind('<Motion>', motion)

shape_id = canvas.create_oval(0, 0, 40, 40, outline="red", 
        fill="green", width=20)
n=[]
def move_oval(event):
    canvas.coords(shape_id, event.x - 10, event.y - 10, event.x + 10, event.y + 10)
    ics = event.x+10
    igr = event.y-10
    n.clear()
    n.append(ics)
    n.append(igr)

def gomot(x):
    eat=canvas.create_oval(999, x,1019, x+20,  outline="red", fill="green", width=30)
    a=canvas.create_text(30, 30, text=m[-1], fill="#0F0",tag="some_tag",font=("calibri", 30))
    def motion():
        try:
            a=canvas.coords(eat)
            canvas.move(eat, -10, 0)
            if a[2]<=20.0:
                canvas.delete(eat)
                canvas.delete('some_tag')
                m.append(m[-1]-5)
            ics1=a[0]+10
            igr1=a[1]-10
            f=(ics1-n[0])**2+(igr1-n[1])**2
            if math.sqrt(f)<=35:
                canvas.delete(eat)
                canvas.delete('some_tag')
                m.append(m[-1]+5)
            root.after(20, motion)
        except:
            
            return             
    motion() 
    canvas.after(2500, lambda: gomot(rnd.randint(1,400)))   
gomot(20)

canvas.bind('<Motion>', move_oval)
root.mainloop()
