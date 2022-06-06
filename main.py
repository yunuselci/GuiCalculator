from tkinter import *

expression = ""
ans = ""
resultStatus = False


def pressNumbers(var):
    global expression, resultStatus
    if resultStatus:
        summary.set("")
    resultStatus = False
    summary.set(summary.get() + (str(var)))


def pressAc():
    global expression
    expression = ""
    summary.set("")


def pressClear():
    global expression, resultStatus
    expression = ""
    resultStatus = False
    summary.set(summary.get()[0:-1])


def pressAns():
    try:
        global expression, resultStatus, ans
        summary.set(ans)
        resultStatus = False
    except Exception as e:
        print(e)
        summary.set("Error")
        expression = ""


def pressEqual():
    try:
        global expression, resultStatus, ans
        expression = summary.get()
        result = str(eval(expression))
        summary.set(result)
        ans = result
        expression = ""
        resultStatus = True
    except Exception as e:
        print(e)
        summary.set("Error")
        expression = ""


if __name__ == "__main__":
    tk = Tk()
    tk.configure(background="#F5F5F5")
    tk.title("Gui Calculator With Python")
    tk.geometry("375x667")
    tk.resizable(True, True)
    summary = StringVar()

    inputFrame = Frame(tk, width=312, height=50, bd=0)
    inputFrame.pack(side=TOP)

    inputField = Entry(inputFrame, textvariable=summary, width=50, fg="#FFFFFF", bg="#1C1C1C", bd=0,
                       font=("Arial", 40, "bold"), justify=RIGHT)
    inputField.grid(row=0, column=0)
    inputField.pack(ipady=13)

    mainFrame = Frame(tk, bg="#F5F5F5")
    mainFrame.pack(expand=True, fill='both')

    mainFrame.rowconfigure(0, weight=1)
    for x in range(1, 5):
        mainFrame.rowconfigure(x, weight=1)
        mainFrame.columnconfigure(x, weight=1)

    digits = {
        7: (1, 1), 8: (1, 2), 9: (1, 3),
        4: (2, 1), 5: (2, 2), 6: (2, 3),
        1: (3, 1), 2: (3, 2), 3: (3, 3),
        0: (4, 2), '.': (4, 1)
    }
    for digit, digitGrid in digits.items():
        digitButton = Button(mainFrame, text=str(digit), fg="#FFFFFF", bd=0, bg="#505050", font=("Arial", 24, "bold"),
                             width=3, height=3, command=lambda iteration=digit: pressNumbers(iteration))
        digitButton.grid(row=digitGrid[0], column=digitGrid[1], sticky=NSEW)

    clearButton = Button(mainFrame, text="C", bg="#D4D4D2", fg="#1C1C1C", font=("Arial", 20),
                         borderwidth=0, command=pressClear)
    clearButton.grid(row=0, column=1, sticky=NSEW)

    equalButton = Button(mainFrame, text="=", bg="#FF9500", fg="#F5F5F5", font=("Arial", 20),
                         borderwidth=0, command=pressEqual)
    equalButton.grid(row=4, column=3, columnspan=2, sticky=NSEW)

    acButton = Button(mainFrame, text="AC", bg="#D4D4D2", fg="#1C1C1C", font=("Arial", 20),
                      borderwidth=0, command=pressAc)
    acButton.grid(row=0, column=2, sticky=NSEW)

    buttonAns = Button(mainFrame, text="ANS", bg="#D4D4D2", fg="#1C1C1C", font=("Arial", 20),
                       borderwidth=0, command=pressAns)
    buttonAns.grid(row=0, column=3, sticky=NSEW)

    operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
    i = 0
    for operator, symbol in operations.items():
        acButton = Button(mainFrame, text=symbol, bg="#FF9500", fg="#F5F5F5", font=("Arial", 20),
                          borderwidth=0, command=lambda iteration=operator: pressNumbers(iteration))
        acButton.grid(row=i, column=4, sticky=NSEW)
        i += 1

    tk.mainloop()
