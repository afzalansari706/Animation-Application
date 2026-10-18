from tkinter import *
import tkinter.font as font
import turtle
import numpy as np
from multiplication import multimatrix
from addition import addmatrix
from Rotation import rotatematrix
from tkinter import ttk
from drawing_history import patterns,save_pattern


ab = turtle.Turtle()
ab.speed(2)


root = Tk()
root.minsize(900, 700)
root.title('Graph Maker')
root.state('zoomed')

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

#Making a tree view for showing data and doing clear,redo, and undo operation
columns = ("Serial No.","Operation","Matrix")
# Frame to hold the history table and scrollbar
history_frame = Frame(root)
history_frame.grid(row=8, column=1, sticky="nsew")

# History table
history_table = ttk.Treeview(
    history_frame,
    columns=columns,
    show="headings",
    height=8
)

history_table.heading("Serial No.", text="Serial No.")
history_table.heading("Operation", text="Operation")
history_table.heading("Matrix", text="Matrix")

history_table.column("Serial No.", width=80, anchor="center")
history_table.column("Operation", width=130)
history_table.column("Matrix", width=350)

# Vertical scrollbar
history_scrollbar = ttk.Scrollbar(
    history_frame,
    orient="vertical",
    command=history_table.yview
)

# Connect the table to the scrollbar
history_table.configure(
    yscrollcommand=history_scrollbar.set
)

# Place the table and scrollbar side by side
history_table.grid(row=0, column=0, sticky="nsew")
history_scrollbar.grid(row=0, column=1, sticky="ns")

# Allow the table to expand inside the frame
history_frame.grid_rowconfigure(0, weight=1)
history_frame.grid_columnconfigure(0, weight=1)

#now we make function that do 2 task
#1st remove the existing rows from table[it remove becoz we have to show lastest change]
#2nd it will add all pattern with id,operation,matrix till lastest update
def refresh_history():
    for item in history_table.get_children():
        history_table.delete(item)

    for pattern in patterns:
        matrix_text = str(pattern['matrix'])

        history_table.insert(
            "",
            "end",
            iid=str(pattern['id']),
            values=(
                pattern["id"],
                pattern["operation"],
                matrix_text
            )
        )

B1 = Button(
    root,
    bd=5,
    font=myfont,
    command=lambda: multimatrix(T1, T2,ab,refresh_history),
    text='Scale'
)
B1.grid(row=7, column=0)

B2 = Button(
    root,
    bd=5,
    font=myfont,
    command=lambda: addmatrix(T1,T2,ab,refresh_history),
    text='Translate'
)
B2.grid(row=7, column=1)
B3 = Button(
    root,
    bd=5,
    font=myfont,
    command=lambda : rotatematrix(T1,ListBox1,ab,refresh_history),
    text='Rotate'
)
B3.grid(row=7, column=2)

root.mainloop()
