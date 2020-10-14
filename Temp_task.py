# Imports libraries
from tkinter import *
from tkinter import messagebox as mb

# Creates window
window = Tk()
window.geometry("420x180")
window.title("Temperature")


# Calculation for Celsius
def calc():
    tempc = (float(cel_box.get()) * 9 / 5) + 32
    return anslabel.config(text=tempc)


# Calculation for Fahrenheit
def calk():
    tempk = (float(k_box.get()) - 32) * 5 / 9

    return anslabel.config(text=tempk)


# Label for fahrenheit
Fahlabel = Label(window, text="Celsius to Fahrenheit:")

# label for celsius
Cellabel = Label(window, text="Fahrenheit to Celsius:")

# Defines Label
anslabel = Label(window, text="answer")

# Creates box for celcius
cel_box = Entry(window, state=DISABLED)

# Button for celcius
_buttonCel = Button(window, text="Celsius", height=1, width=10, command=calc, state=DISABLED)

# Box for Fahrenheit
k_box = Entry(window, state=DISABLED)

# Button for Fahrenheit
_buttonK = Button(window, text="Fahrenheit", height=1, width=10, command=calk, state=DISABLED)

# Button to close
_buttonClose = Button(window, text="exit", height=2, width=3, command=window.destroy)


# Function to make radio button active
def enableCel():
    k_box.configure(state=DISABLED)
    _buttonK.configure(state=DISABLED)
    k_box.update()
    _buttonK.update()
    cel_box.configure(state="normal")
    cel_box.update()
    _buttonCel.configure(state="normal")
    _buttonCel.update()


# Function to make radio button active
def enableFah():
    cel_box.configure(state=DISABLED)
    cel_box.update()
    _buttonCel.configure(state=DISABLED)
    _buttonCel.update()
    k_box.configure(state="normal")
    k_box.update()
    _buttonK.configure(state="normal")
    k_box.update()


R = StringVar()
enableCell_button = Radiobutton(window, text="Activate Celsius", variable=R, value="0", command=enableCel, state="normal")

enableFah_box = Radiobutton(window, text="Active Fahrenheit", variable=R, value="1", command=enableFah, state="normal")

enableFah_box.grid(row=0, column=0, sticky=W)
enableCell_button.grid(row=1, column=0, sticky=W)
k_box.grid(row=2, column=2)
_buttonK.grid(row=2, column=3)
cel_box.grid(row=3, column=2)
_buttonCel.grid(row=3, column=3)
anslabel.grid(row=4, column=0)
Fahlabel.grid(row=2, column=0)
Cellabel.grid(row=3, column=0)
_buttonClose.grid(row=5, column=0)
window.mainloop()
