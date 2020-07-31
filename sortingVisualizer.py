import tkinter as tk
import random


def swap_two_pos(pos_0, pos_1):
    Bar1x1, _, Bar1x2, _ = canvas.coords(pos_0)
    Bar2x1, _, Bar2x2, _ = canvas.coords(pos_1)
    canvas.move(pos_0, Bar2x1-Bar1x1, 0)
    canvas.move(pos_1, Bar1x2-Bar2x2, 0)


def _mergeSort(nums):


    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]

        right = nums[mid:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:

                nums[k] = left[i]

                i += 1
            else:
                nums[k] = right[j]

                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

    #enableResetButton()
    return nums


def _insertionSort():
    global barList
    global lengthList

    for i in range(len(lengthList)):
        cursor = lengthList[i]
        cursorBar = barList[i]
        pos = i

        while pos > 0 and lengthList[pos - 1] > cursor:
            lengthList[pos] = lengthList[pos - 1]
            barList[pos], barList[pos - 1] = barList[pos - 1], barList[pos]
            swap_two_pos(barList[pos], barList[pos-1])   # <-- updates the display
            yield                                       # <-- suspends the execution
            pos -= 1                                    # <-- execution resumes here when next is called

        lengthList[pos] = cursor
        barList[pos] = cursorBar
        swap_two_pos(barList[pos], cursorBar)


worker = None    # <-- Not a thread in spite of the name.


def mergeSort():     # <-- commands the start of both the animation, and the sort
    global worker
   # worker = _merge_sort()
    animate()


def insertionSort():     # <-- commands the start of both the animation, and the sort
    global worker
    worker = _insertionSort()
    animate()


def animate():      # <-- commands resuming the sort once the display has been updated
                    # controls the pace of the animation
    global worker
    if worker is not None:
        try:
            next(worker)
            window.after(10, animate)    # <-- repeats until the sort is complete,
        except StopIteration:            # when the generator is exhausted
            worker = None
        finally:
            window.after_cancel(animate)  # <-- stop the callbacks


def resetArr():
    global barList
    global lengthList
    canvas.delete('all')
    start = 5
    end = 15
    barList = []
    lengthList = []

    for x in range(1, 100):
        randomY = random.randint(1, 495)
        x = canvas.create_rectangle(start, randomY, end, 500, fill='red')
        barList.append(x)
        start += 10
        end += 10

    for bar in barList:
        x = canvas.coords(bar)
        length = x[3] - x[1]
        lengthList.append(length)

    for i in range(len(lengthList)-1):
        if lengthList[i] == min(lengthList):
            canvas.itemconfig(barList[i], fill='blue')
        elif lengthList[i] == max(lengthList):
            canvas.itemconfig(barList[i], fill='green')


window = tk.Tk()
window.title("Jeff's Sorting Visualizer")
window.geometry('1000x600')
canvas = tk.Canvas(window, width='1000', height='550', bg="#e8f0fc")
canvas.grid(column=0, row=0, columnspan=50)

#qiuxk
merge = tk.Button(window, text='Merge Sort', bg="#c9c9c9")
#selection
insert = tk.Button(window, text='Insertion Sort', command=insertionSort, bg="#c9c9c9")
#bubble
reset = tk.Button(window, text='Generate New Array', command=resetArr, bg="#0dff67")
insert.grid(column=40, row=1)
reset.grid(column=0, row=1)

resetArr()
window.mainloop()
