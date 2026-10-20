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
root.title('Animation Window')
root.state('zoomed')

#main Canvas
main_canvas = Canvas(root)

#main Scrollbar
main_scrollbar = ttk.Scrollbar(root,orient="vertical",command=main_canvas.yview)

#Frame that will contain all application widgets
main_frame= Frame(main_canvas)

#Update Scrolling while the frame size is change
main_frame.bind(
    "<Configure>",#Configure is like event when size of window
    lambda event: main_canvas.configure(scrollregion=main_canvas.bbox("all"))#it will return the coordinate of window
)

# Put the frame inside the canvas
main_canvas.create_window(
    (0, 0),
    window=main_frame,
    anchor="nw"
)

# Connect the canvas and scrollbar
main_canvas.configure(
    yscrollcommand=main_scrollbar.set
)

main_canvas.pack(side="left", fill="both", expand=True)
main_scrollbar.pack(side="right", fill="y")

def scroll_main_window(event):# call when yview scorll happen throught mouse
    main_canvas.yview_scroll(
        int(-1 * (event.delta / 120)),# int(+1/-1) indicate direction and movement of scrollbar (+ve move downward)(-ve move up )
        "units" 
    )# if i scroll down event.delta = -120 for up event.delta=120

main_canvas.bind_all("<MouseWheel>", scroll_main_window)

myfont = font.Font(family='helvetica', size=22, weight='bold')
myfont1 = font.Font(family='helvetica', size=20, weight='bold')


L1 = Label(main_frame, text='Matrix to Graph', font=myfont, fg='cyan')
L1.grid(row=0, column=1)

L2 = Label(main_frame, text='2D Transformation', font=myfont,
           fg='black', bg='white')
L2.grid(row=1, column=1)

L3 = Label(main_frame, text='Matrix', font=myfont1,
           fg='black', bg='white')
L3.grid(row=3, column=0)

T1 = Text(main_frame, bd=4, height=10, width=23)
T1.grid(row=3, column=1)

L4 = Label(main_frame, text='Transformation', font=myfont1,
           fg='black', bg='white')
L4.grid(row=4, column=0)

T2 = Text(main_frame, bd=4, height=10, width=23)
T2.grid(row=4, column=1)

L5 = Label(main_frame,text = 'Select the degree for rotation',font = myfont1,fg='purple',bg='white',height = "2",width="90")
L5.grid(row=5,column=1)

ListBox1 = Listbox(main_frame,selectmode= 'single')
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
history_frame = Frame(main_frame)
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
    main_frame,
    bd=5,
    font=myfont,
    command=lambda: multimatrix(T1, T2,ab,refresh_history),
    text='Scale'
)
B1.grid(row=7, column=0)

B2 = Button(
    main_frame,
    bd=5,
    font=myfont,
    command=lambda: addmatrix(T1,T2,ab,refresh_history),
    text='Translate'
)
B2.grid(row=7, column=1)
B3 = Button(
    main_frame,
    bd=5,
    font=myfont,
    command=lambda : rotatematrix(T1,ListBox1,ab,refresh_history),
    text='Rotate'
)
B3.grid(row=7, column=2)


root.mainloop()
