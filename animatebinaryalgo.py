from tkinter import Tk, Frame, Canvas, Label, StringVar, Entry, Button, LEFT, RIGHT
import tkinter.messagebox
import random


class StepControl:
    def __init__(self):
        self.list = [x for x in range(1, 40)]
        self.reset()
        self.key = 0
        self.low = 0
        self.high = len(self.list) - 1

    def reset(self):
        self.i = -1  # current index
        self.done = False
        self.low = 0
        self.high = len(self.list) - 1
        # random.shuffle(self.list)
        self.drawAStep()

    def step(self):
        if self.done:
            tkinter.messagebox.showinfo("showinfo", "Key is found")
            return
        
        if not self.high >= self.low:
            tkinter.messagebox.showinfo("showinfo", "Key is not found")
            return

        self.i = (self.low + self.high) // 2
        self.drawAStep()

        if self.key < self.list[self.i]:
            self.high = self.i - 1
        elif self.key == self.list[self.i]:
            self.done = True
            tkinter.messagebox.showinfo("showinfo", "Key is found")
        else:
            self.low = self.i + 1

    def drawAStep(self):
        bottomGap = 10
        canvas.delete("line")
        canvas.create_line(10, height - bottomGap, width - 10, height - bottomGap, tag="line")
        barWidth = (width - 20) / len(self.list)

        maxCount = int(max(self.list))
        for i in range(len(self.list)):
            canvas.create_rectangle(i * barWidth + 10, (height - bottomGap) * (1 - self.list[i] / (maxCount + 4)),
                                    (i + 1) * barWidth + 10, height - bottomGap, tag="line")
            canvas.create_text(i * barWidth + 10 + barWidth / 2,
                               (height - bottomGap) * (1 - self.list[i] / (maxCount + 4)) - 8,
                               text=str(self.list[i]), tag="line")

        if self.i >= 0:
            canvas.create_rectangle(self.i * barWidth + 10,
                                    (height - bottomGap) * (1 - self.list[self.i] / (maxCount + 4)),
                                    (self.i + 1) * barWidth + 10, height - bottomGap, fill="red", tag="line")


def step():
    control.key = float(key.get())
    control.step()


def reset():
    control.reset()


window = Tk()  # Create a window
window.title("Linear Search Animation")  # Set title

width = 650
height = 150
radius = 2
canvas = Canvas(window, width=width, height=height)
canvas.pack()

frame = Frame(window)
frame.pack()

Label(frame, text="Enter a key (in float):").pack(side=LEFT)
key = StringVar()
Entry(frame, textvariable=key, justify=RIGHT, width=3).pack(side=LEFT)
Button(frame, text="Step", command=step).pack(side=LEFT)
Button(frame, text="Reset", command=reset).pack(side=LEFT)

control = StepControl()
control.drawAStep()

window.mainloop()  # Create an event loop
