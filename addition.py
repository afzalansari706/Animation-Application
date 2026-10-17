from tkinter import *
 #Addition of matrix
def addmatrix(T1,T2,ab):

        # Read the first matrix
        data1 = T1.get("1.0", END).strip()
        rows1 = data1.split("\n")
        x = []

        for r in rows1:
            if r.strip():
                numbers1 = [float(value) for value in r.split()]
                x.append(numbers1)

        # Read the second matrix
        data2 = T2.get("1.0", END).strip()
        rows2 = data2.split("\n")
        y = []

        for r in rows2:
            if r.strip():
                numbers2 = [float(value) for value in r.split()]
                y.append(numbers2)

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

      

        if len(x) != len(y) or len(x[0]) != len(y[0]):
            print("Matrices must have the same dimensions.")
            return

        result = [
            [0 for j in range(len(x[0]))]
            for i in range(len(x))
        ]

        for i in range(len(x)):
            for j in range(len(x[0])):
                result[i][j] = x[i][j] + y[i][j]

        # Display the result
        if result:
            result.append(result[0].copy())

        print("Result matrix:")
        for r in result:
            print(r)

        # Draw the result
     
        ab.penup()
        

        for point in result:
            if len(point) >= 2:
                ab.goto(point[0], point[1])
                ab.pd()

