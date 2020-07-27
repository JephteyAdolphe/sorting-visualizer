import tkinter as tk
import random
import string

HEIGHT = 600
WIDTH = 1000

numArr = []
coordsArr = []  # list of each bar's coordinates
lines = {}


def mergeSort(nums):
    arr = nums

    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr


def generateRandomKey():
    letters = string.ascii_lowercase
    res = ''.join(random.choice(letters) for i in range(2))
    return res


root = tk.Tk()
root.resizable(False, False)
root.title("Jeff's Sorting Visualizer")

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
    x = 7.1
    arrayCanvas.delete("all")
    numArr.clear()
    lines.clear()

    for i in range(128):
        coords = []

        randomNumber = random.randint(0, 475)
        arrayCanvas.create_line(x, 480, x, randomNumber, width=5)
        x += 7.3

        numArr.append(randomNumber * -1)
        coords.append(x)
        coords.append(480)
        coords.append(x)
        coords.append(randomNumber)
        coordsArr.append(coords)

        if generateRandomKey() not in lines.keys():
            lines[generateRandomKey()] = coords     # remember to loop thru this backwards

    print(numArr)


resetButton = tk.Button(headerFrame, text="Generate New Array", command=resetArr, bg="#0dff67")
resetButton.place(relx=0.03, rely=0.25)

quick = tk.Button(headerFrame, text="Quick Sort")
quick.place(relx=0.47, rely=0.25)

merge = tk.Button(headerFrame, text="Merge Sort")
merge.place(relx=0.57, rely=0.25)

selection = tk.Button(headerFrame, text="Selection Sort")
selection.place(relx=0.67, rely=0.25)

insertion = tk.Button(headerFrame, text="Insertion Sort")
insertion.place(relx=0.77, rely=0.25)

bubble = tk.Button(headerFrame, text="Bubble Sort")
bubble.place(relx=0.87, rely=0.25)

resetArr()
print(coordsArr[0])
print(coordsArr[1])
print(mergeSort(numArr))

root.mainloop()
