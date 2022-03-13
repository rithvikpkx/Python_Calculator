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
        expression = total

    except:

        equation.set(" ERROR ")
        expression = ""


calculator = Tk()
calculator.title("CALCULATOR")
calculator.iconbitmap("calculator-icon.ico")
# calculator.configure(bg="#DCE2C8") alternate background color that also looks good.
calculator.configure(bg="#D3C4D1")
equation = StringVar()
Entry(calculator, textvariable=equation, width=50, state=DISABLED, disabledbackground="#A2AEBB",
      disabledforeground="black", font=BOLD).grid(row=0, column=0, columnspan=3, padx=5, pady=12)
Button(calculator, text=" 7 ", font=(BOLD, 16), bg="#EB8A90", activebackground="#d66b74", fg="black", height=2,
       width=12,
       command=lambda: press(7)).grid(row=1, column=0)
Button(calculator, text=" 8 ", font=(BOLD, 16), bg="#EB8A90", activebackground="#d66b74", fg="black", height=2,
       width=12,
       command=lambda: press(8)).grid(row=1, column=1)
Button(calculator, text=" 9 ", font=(BOLD, 16), bg="#EB8A90", activebackground="#d66b74", fg="black", height=2,
       width=12,
       command=lambda: press(9)).grid(row=1, column=2)
Button(calculator, text=" 4 ", font=(BOLD, 16), bg="#EB8A90", activebackground="#d66b74", fg="black", height=2,
       width=12,
       command=lambda: press(4)).grid(row=2, column=0)
Button(calculator, text=" 5 ", font=(BOLD, 16), bg="#EB8A90", activebackground="#d66b74", fg="black", height=2,
       width=12,
       command=lambda: press(5)).grid(row=2, column=1)
Button(calculator, text=" 6 ", font=(BOLD, 16), bg="#EB8A90", activebackground="#d66b74", fg="black", height=2,
       width=12,
       command=lambda: press(6)).grid(row=2, column=2)
Button(calculator, text=" 1 ", font=(BOLD, 16), bg="#EB8A90", activebackground="#d66b74", fg="black", height=2,
       width=12,
       command=lambda: press(1)).grid(row=3, column=0)
Button(calculator, text=" 2 ", font=(BOLD, 16), bg="#EB8A90", activebackground="#d66b74", fg="black", height=2,
       width=12,
       command=lambda: press(2)).grid(row=3, column=1)
Button(calculator, text=" 3 ", font=(BOLD, 16), bg="#EB8A90", activebackground="#d66b74", fg="black", height=2,
       width=12,
       command=lambda: press(3)).grid(row=3, column=2)
Button(calculator, text=" 0 ", font=(BOLD, 16), bg="#EB8A90", activebackground="#d66b74", fg="black", height=2,
       width=12,
       command=lambda: press(0)).grid(row=4, column=1)
Button(calculator, text=" + ", font=(BOLD, 16), bg="#EB8A90", activebackground="#d66b74", fg="black", height=2,
       width=12,
       command=lambda: press("+")).grid(row=4, column=0)
Button(calculator, text=" - ", font=(BOLD, 16), bg="#EB8A90", activebackground="#d66b74", fg="black", height=2,
       width=12,
       command=lambda: press("-")).grid(row=4, column=2)
Button(calculator, text=" * ", font=(BOLD, 16), bg="#EB8A90", activebackground="#d66b74", fg="black", height=2,
       width=12,
       command=lambda: press("*")).grid(row=5, column=2)
Button(calculator, text=" / ", font=(BOLD, 16), bg="#EB8A90", activebackground="#d66b74", fg="black", height=2,
       width=12,
       command=lambda: press("/")).grid(row=5, column=0)
Button(calculator, text=" = ", font=(BOLD, 16), bg="#EB8A90", activebackground="#d66b74", fg="black", height=2,
       width=12, command=equal).grid(row=5,
                                     column=1, )
Button(calculator, text=" CLEAR ", font=(BOLD, 16), bg="#EB8A90", activebackground="#d66b74", fg="black", height=2,
       width=12, command=clear).grid(
    row=6, column=1)
calculator.mainloop()
