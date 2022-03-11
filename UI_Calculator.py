from tkinter import *
from tkinter.font import *

expression = ""


def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def clear():
    global expression
    expression = ""
    equation.set(expression)


def equal():
    global expression

    try:

        total = str(eval(expression))
        equation.set(total)
        expression = ""

    except:
        equation.set(" ERROR ")
        expression = ""



calculator = Tk()
calculator.title("CALCULATOR")
calculator.geometry("500x500")
equation = StringVar()
Entry(calculator, textvariable=equation, width=76, state=DISABLED, bg="white").grid(row=0, column=0, columnspan=3, padx=20, pady=20)
Button(calculator, text=" 1 ", height=1, width=7, command=lambda: press(1)).grid(row=1, column=0)
calculator.mainloop()
