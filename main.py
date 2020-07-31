import tkinter as tk
import random
import string
from collections import OrderedDict
import time

HEIGHT = 600
WIDTH = 1000

numArr = []
coordsArr = []  # list of each bar's coordinates (list of lists)
lines = OrderedDict()
tagList = []


def generateRandomKey():
    letters = string.ascii_lowercase
    res = ''.join(random.choice(letters) for i in range(2))

    if res in lines:
        return generateRandomKey()
    else:
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
    tagList.clear()

    for i in range(4):
        coords = []
        tag = generateRandomKey()

        randomNumber = random.randint(0, 475)
        #arrayCanvas.create_line(x, 480, x, randomNumber, width=5, tags=tag)
        arrayCanvas.create_rectangle(x, 480, x + 4, randomNumber, fill="black", tags=tag)
        x += 7.3

        numArr.append(randomNumber * -1)
        coords.append(x)
        coords.append(480)
        coords.append(x + 4)
        coords.append(randomNumber)
        coordsArr.append(coords)

        lines[tag] = coords
        tagList.append(tag)


def updateCoords(tag, newTag, newX):
    arrayCanvas.coords(tag, newX, 480, newX, lines[newTag][3])


def mergeSort(nums, tags):
    #disableButtons()
    #arrayCanvas.delete("all")

    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        leftTags = tags[:mid]

        right = nums[mid:]
        rightTags = tags[mid:]

        mergeSort(left, leftTags)
        mergeSort(right, rightTags)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                #time.sleep(0.5)
                arrayCanvas.coords(tags[k], lines[leftTags[i]][0], 480, lines[leftTags[i]][2], left[i] * - 1)

                print("nums before --> " + str(nums))
                nums[k] = left[i]
                print("nums after --> " + str(nums))
                tags[k] = leftTags[i]
                i += 1
            else:
                #time.sleep(0.5)
                arrayCanvas.coords(tags[k], lines[rightTags[j]][0], 480, lines[rightTags[j]][2], right[j] * - 1)

                print("nums before --> " + str(nums))
                nums[k] = right[j]
                print("nums after --> " + str(nums))
                tags[k] = rightTags[j]
                j += 1
            k += 1

        while i < len(left):
            #time.sleep(0.5)
            arrayCanvas.coords(tags[k], lines[leftTags[i]][0], 480, lines[leftTags[i]][2], left[i] * - 1)


            print("nums before --> " + str(nums))
            nums[k] = left[i]
            print("nums after --> " + str(nums))
            tags[k] = leftTags[i]
            i += 1
            k += 1

        while j < len(right):
            #time.sleep(0.5)
            arrayCanvas.coords(tags[k], lines[rightTags[j]][0], 480, lines[rightTags[j]][2], right[j] * - 1)

            print("nums before --> " + str(nums))
            nums[k] = right[j]
            print("nums after --> " + str(nums))
            tags[k] = rightTags[j]
            j += 1
            k += 1

    #enableResetButton()
    return nums


quick = tk.Button(headerFrame, text="Quick Sort")
quick.place(relx=0.47, rely=0.25)

merge = tk.Button(headerFrame, text="Merge Sort", command=lambda: mergeSort(numArr, tagList))
merge.place(relx=0.57, rely=0.25)

selection = tk.Button(headerFrame, text="Selection Sort")
selection.place(relx=0.67, rely=0.25)


def createALine():
    arrayCanvas.create_line(300, 150, 300, 30, width=5, tags="hey")


def moveLine():
    arrayCanvas.coords("hey", 500, 150, 500, 30)
    arrayCanvas.create_line(100, 150, 100, 30, width=5, tags="hey")


insertion = tk.Button(headerFrame, text="Insertion Sort", command=createALine )
insertion.place(relx=0.77, rely=0.25)

bubble = tk.Button(headerFrame, text="Bubble Sort", command=moveLine)
bubble.place(relx=0.87, rely=0.25)


resetArr()


def disableButtons():
    resetButton["state"] = "disabled"
    quick["state"] = "disabled"
    merge["state"] = "disabled"
    selection["state"] = "disabled"
    insertion["state"] = "disabled"
    bubble["state"] = "disabled"


def enableButtons():
    quick["state"] = "normal"
    merge["state"] = "normal"
    selection["state"] = "normal"
    insertion["state"] = "normal"
    bubble["state"] = "normal"


def enableResetButton():
    resetButton["state"] = "normal"


def generateNewArray():
    #enableButtons()
    resetArr()


resetButton = tk.Button(headerFrame, text="Generate New Array", command=generateNewArray, bg="#0dff67")
resetButton.place(relx=0.03, rely=0.25)


#print(coordsArr[0])
#print(coordsArr[1])
#mergeSort(numArr, tagList)
#print(lines["ja"][3])

root.mainloop()
