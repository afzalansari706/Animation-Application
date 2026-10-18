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
        # Read the selected rotation angle
        selected = ListBox1.curselection()

        if not selected:
            print("Please select a rotation angle.")
            return

        angle = ListBox1.get(selected[0])
        if angle == "30 degree":
            theta = np.pi / 6

        elif angle == "45 degree":
            theta = np.pi / 4

        elif angle == "60 degree":
            theta = np.pi / 3

        elif angle == "90 degree":
            theta = np.pi / 2

        elif angle == "180 degree":
            theta = np.pi

        elif angle == "270 degree":
            theta = 3 * np.pi / 2

        y = [
            [np.cos(theta), np.sin(theta)],
            [-np.sin(theta), np.cos(theta)]
        ]
                

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
        if result:
            result.append(result[0].copy())

        # Draw the result
        
        ab.penup()
        ab.goto(0, 0)
        ab.pendown()

        for point in result:
            if len(point) >= 2:
                ab.goto(point[0], point[1])

       

        
