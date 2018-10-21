from MLdata import writeML
from tkinter import *
import tkinter.messagebox
stage = 1
def genderButton(gender, frame, master):
    ml.sex = gender
    master.destroy()
def checkColour(colour, master):
    ml.colour = colour
    master.destroy()
def ageChange(change, v):
    if change == "+":
        ml.age += 1

    elif change == "-":
        ml.age -= 1

    elif change == "--":
        ml.age -= 5

    elif change == "++":
        ml.age += 5
    v.set(ml.age)

def takeName(master, e):
    ml.name = e.get()
    print(ml.name)
    master.destroy()

def done(command, master):
    if command == "Write":
        ml.write()
    else:
        ml.predicting()
        tkinter.messagebox.showinfo("Predicted", ml.predict)
    master.destroy()

ml = writeML(0, None, None, None)
root = Tk()

frame = Frame(root)
frame.pack()

label1 = Label(frame, text="Hey, what's your gender?")
label1.grid(row=0, column=1, sticky=E)

button1 = Button(frame, text="Boy", command=lambda:genderButton("Male", frame, root))
button2 = Button(frame, text="Girl", command=lambda:genderButton("Female", frame, root))


button1.grid(row=1, column=2, sticky=W)
button2.grid(row=1, column=1, sticky=W)

root.mainloop()
stage = 2
root = Tk()
window = Frame(root)
window.pack()
label1 = Label(window, text="Hey, how old are you?")
label1.grid(row=1, column=3)

v = StringVar()
l = Label(window, textvariable=v)
l.grid(row=2, column=3, sticky=S)
v.set(ml.age)

button1 = Button(window, text="+", command=lambda: ageChange("+", v))
button2 = Button(window, text="-", command=lambda: ageChange("-", v))

button1.grid(row=2, column=2, sticky=E)
button2.grid(row=2, column=4, sticky=W)

button3 = Button(window, text="+5", command=lambda: ageChange("++", v))
button4 = Button(window, text="-5", command=lambda: ageChange("--", v))

button3.grid(row=2, column=1, sticky=E)
button4.grid(row=2, column=5, sticky=W)

button5 = Button(window, text="Done", command=root.destroy)
button5.grid(row=3, column=3, sticky=N)
root.mainloop()
stage = 3

root = Tk()
colour = Frame(root)
colour.pack()

l = Label(colour, text="Whats your favourite colour?")
l.grid(row=0, column=1, sticky=N)

button1 = Button(colour, text="Red", command=lambda: checkColour("Red", root))
button2 = Button(colour, text="Yellow", command=lambda: checkColour("Yellow", root))
button3 = Button(colour, text="Green", command=lambda: checkColour("Green", root))
button4 = Button(colour, text="Blue", command=lambda: checkColour("Blue", root))
button5 = Button(colour, text="Purple", command=lambda: checkColour("Purple", root))
button6 = Button(colour, text="Pink", command=lambda: checkColour("Pink", root))
button7 = Button(colour, text="Black", command=lambda: checkColour("Black", root))
button8 = Button(colour, text="White", command=lambda: checkColour("White", root))
button9 = Button(colour, text="Brown", command=lambda: checkColour("Brown", root))
button10 = Button(colour, text="Grey", command=lambda: checkColour("Grey", root))
button11 = Button(colour, text="Orange", command=lambda: checkColour("Orange", root))

button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
button10.grid(row=4, column=0)
button11.grid(row=4, column=1)

root.mainloop()

root = Tk()
name = Frame(root)
name.pack()

e = StringVar()
v = Entry(root, textvariable=e)
v.pack(side=TOP)


b = Button(name, text="Done", command=lambda: takeName(root, e))
b.pack(side=BOTTOM)
root.mainloop()
# print("yay")
root = Tk()

# print("yay")
l = Label(root, text="What do you want to do?")
l.pack()
w = Button(root, text="Write", command=lambda: done("Write", root))
w.pack()
p = Button(root, text="Predict", command=lambda: done("NotWrite", root))
p.pack()
# print("yay")
root.mainloop()
