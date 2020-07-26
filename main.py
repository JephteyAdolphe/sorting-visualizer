import tkinter as tk
import random

HEIGHT = 600
WIDTH = 1000

numArr = []

root = tk.Tk()
root.resizable(False, False)

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# Components

headerFrame = tk.Frame(root, bg="black")
headerFrame.place(relwidth=1, relheight=0.1)

mainFrame = tk.Frame(root, bg="gray")
mainFrame.place(relwidth=1, relheight=0.9, rely=0.1)

arrayCanvas = tk.Canvas(mainFrame)
arrayCanvas.place(relwidth=0.94, relheight=0.9, relx=0.03, rely=0.05)


def resetArr():
    x = 10
    arrayCanvas.delete("all")
    numArr.clear()

    for i in range(133):
        randomNumber = random.randint(0, 475)

        arrayCanvas.create_line(x, 480, x, randomNumber, width=5)
        x += 7

        numArr.append(randomNumber * -1)
    print(numArr)


resetButton = tk.Button(headerFrame, text="Generate New Array", command=resetArr)
resetButton.place(relx=0.03, rely=0.25)

resetArr()

root.mainloop()
