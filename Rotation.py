    #Rotation Matrix
from tkinter import *
import numpy as np
def rotatematrix(T1,ListBox1,ab):

        # Read the first matrix
        data1 = T1.get("1.0", END).strip()
        rows1 = data1.split("\n")
        x = []

        for r in rows1:
            if r.strip():
                numbers1 = [float(value) for value in r.split()]
                x.append(numbers1)

        # Read the rotation
        if(ListBox1.get(ListBox1.curselection()) == "30 degree"):
            y = [[np.cos(np.pi/6),np.sin(np.pi/6)],[-np.sin(np.pi/6),np.cos(np.pi/6)]]
        elif(ListBox1.get(ListBox1.curselection()) == "45 degree"):
            y = [[np.cos(np.pi/4),np.sin(np.pi/4)],[-np.sin(np.pi/4),np.cos(np.pi/4)]]
        elif(ListBox1.get(ListBox1.curselection()) == "60 degree"):
            y = [[np.cos(np.pi/3),np.sin(np.pi/3)],[-np.sin(np.pi/3),np.cos(np.pi/3)]]
        elif(ListBox1.get(ListBox1.curselection()) == "90 degree"):
            y = [[np.cos(np.pi/2),np.sin(np.pi/2)],[-np.sin(np.pi/2),np.cos(np.pi/2)]]
        elif(ListBox1.get(ListBox1.curselection()) == "180 degree"):
            y = [[np.cos(np.pi),np.sin(np.pi)],[-np.sin(np.pi),np.cos(np.pi)]]
        elif(ListBox1.get(ListBox1.curselection()) == "270 degree"):
            y = [[np.cos(3*(np.pi)/2),np.sin(3*(np.pi)/2)],[-np.sin(3*(np.pi)/2),np.cos(3*(np.pi)/2)]]
            
        

        # Check that both matrices contain data
        if not x or not y:
            print("Please enter both matrices.")
            return

        # Check that each matrix has consistent row lengths
        if any(len(row) != len(x[0]) for row in x):
            print("The first matrix has inconsistent row lengths.")
            return

        if any(len(row) != len(y[0]) for row in y):
            print("The second matrix has inconsistent row lengths.")
            return

        # Check matrix multiplication dimensions
        if len(x[0]) != len(y):
            print("Matrix dimensions are incompatible.")
            return

        # Create the result matrix dynamically
        result = [
            [0 for j in range(len(y[0]))]
            for i in range(len(x))
        ]

        # Matrix multiplication
        for i in range(len(x)):
            for j in range(len(y[0])):
                for k in range(len(y)):
                    result[i][j] += x[i][k] * y[k][j]

        # Display the result
        print("Result matrix:")
        for r in result:
            print(r)

        # Draw the result
        ab.clear()
        ab.penup()
        ab.goto(0, 0)
        ab.pendown()

        for point in result:
            if len(point) >= 2:
                ab.goto(point[0], point[1])

        ab.goto(0, 0)

        
