from tkinter import *
import tkinter.font as font
import turtle
import numpy as np
from multiplication import multimatrix
from addition import addmatrix
from Rotation import rotatematrix

ab = turtle.Turtle()
ab.speed(2)
ab.setposition(0, 0)

root = Tk()
root.minsize(900, 700)
root.title('Graph Maker')

myfont = font.Font(family='helvetica', size=22, weight='bold')
myfont1 = font.Font(family='helvetica', size=20, weight='bold')


L1 = Label(root, text='Matrix to Graph', font=myfont, fg='cyan')
L1.grid(row=0, column=1)

L2 = Label(root, text='2D Transformation', font=myfont,
           fg='black', bg='white')
L2.grid(row=1, column=1)

L3 = Label(root, text='Matrix', font=myfont1,
           fg='black', bg='white')
L3.grid(row=3, column=0)

T1 = Text(root, bd=4, height=10, width=23)
T1.grid(row=3, column=1)

L4 = Label(root, text='Transformation', font=myfont1,
           fg='black', bg='white')
L4.grid(row=4, column=0)

T2 = Text(root, bd=4, height=10, width=23)
T2.grid(row=4, column=1)

L5 = Label(root,text = 'Select the degree for rotation',font = myfont1,fg='purple',bg='white',height = "2",width="90")
L5.grid(row=5,column=1)

ListBox1 = Listbox(root,selectmode= 'single')
ListBox1.insert(1,"30 degree")
ListBox1.insert(2,"45 degree")
ListBox1.insert(3,"60 degree")
ListBox1.insert(4,"90 degree")
ListBox1.insert(5,"180 degree")
ListBox1.insert(6,"270 degree")
ListBox1.grid(row=6,column = 1)



B1 = Button(
    root,
    bd=5,
    font=myfont,
    command=lambda: multimatrix(T1, T2,ab),
    text='Scale'
)
B1.grid(row=7, column=0)

B2 = Button(
    root,
    bd=5,
    font=myfont,
    command=lambda: addmatrix(T1,T2,ab),
    text='Translate'
)
B2.grid(row=7, column=1)
B3 = Button(
    root,
    bd=5,
    font=myfont,
    command=rotatematrix,
    text='Rotate'
)
B3.grid(row=7, column=2)

root.mainloop()
