# Version 2.
# Combined all 7 operation functions into 2 main ones.
# Added backspace functionality

from tkinter import *
# from Calculator_Functions import *




root = Tk()
root.title("Edwin's Calculator")
root.geometry("200x200")


display = StringVar()
display.set("0")
list_of_digits = []

# -----------------------------------------------------------------------------------------------------------------
# Place functions in separate module


def concat(digit):

    if digit == "." and list_of_digits.count("."):
        pass
    else:
        global digits_joined
        list_of_digits.append(digit)                  # listofdigits is list of digits of typed number
        digits_joined = "".join(list_of_digits)      # digits_joined: the string of digits of typed number (not a list)
        display.set(digits_joined)


def arith_1(operation_1):
    global result
    result = float(digits_joined)              # stores the string of digits of typed number as an integer called result

    global list_of_digits
    list_of_digits = []                       # resetting to 0 to start a new list of digits

    global symbol
    symbol = operation_1                         # Can be addition/subtraction/multiplication/division


def arith_2(operation_2):
    global result

    if operation_2 == "reciprocal":
        result = 1 / float(digits_joined)
        display.set(result)

    elif operation_2 == "square":
        result = float(digits_joined) ** 2
        display.set(result)

    elif operation_2 == "square_root":
        result = float(digits_joined) ** 0.5
        display.set(result)


def equals():
    global result

    if symbol == "addition":
        result = result + float(digits_joined)
        display.set(result)

    elif symbol == "subtraction":
        result = result - float(digits_joined)
        display.set(result)

    elif symbol == "multiplication":
        result = result * float(digits_joined)
        display.set(result)

    elif symbol == "division":
        result = result / float(digits_joined)
        display.set(result)

    elif symbol == "percent":
        result = (result / 100) * float(digits_joined)
        display.set(result)


def clear_all():
    global list_of_digits

    list_of_digits = []
    display.set("0")


def clear_last():
    global list_of_digits

    list_of_digits = []


def backspace():
    global list_of_digits
    global digits_joined

    list_of_digits.pop()
    digits_joined = "".join(list_of_digits)
    display.set(digits_joined)


# -----------------------------------------------------------------------------------------------------------
#   ----------------------------------------------------------------------------------------------------------
# Separate module for GUI code

my_menu = Menu(root)
root.config(menu=my_menu)

submenu_file = Menu(my_menu)
my_menu.add_cascade(label="File", menu=submenu_file)
submenu_file.add_command(label="Exit", command=root.quit)

submenu_switch = Menu(my_menu)                  # Find a way to bypass making this a drop down menu (Button? see LN 149)
my_menu.add_cascade(label="Switch", menu=submenu_switch)
submenu_switch.add_command(label="Switch")

display_label = Label(root, textvariable=display, bd=2, anchor=E)
display_label.grid(row=0, columnspan=4)

button_percent = Button(root, text="%", width=4, height=1, bg="green",
                        command=lambda: arith_1("percent"))
button_percent.grid(row=1)

button_CLR = Button(root, text="CLR", width=4, height=1, bg="green",
                    command=clear_all)
button_CLR.grid(row=1, column=1)

button_C = Button(root, text="C", width=4, height=1, bg="green",
                  command=clear_last)
button_C.grid(row=1, column=2)

button_backspace = Button(root, text="<--", width=4, height=1, bg="green",
                          command=backspace)
button_backspace.grid(row=1, column=3)

button_reciprocal = Button(root, text="1/x", width=4, height=1, bg="green",
                           command=lambda: arith_2("reciprocal"))
button_reciprocal.grid(row=2)

button_square = Button(root, text="SQ", width=4, height=1, bg="green",
                       command=lambda: arith_2("square"))
button_square.grid(row=2, column=1)

button_sqrt = Button(root, text="SQT", width=4, height=1, bg="green",
                     command=lambda: arith_2("square_root"))
button_sqrt.grid(row=2, column=2)

button_divide = Button(root, text="/", width=4, height=1, bg="green",
                       command=lambda: arith_1("division"))
button_divide.grid(row=2, column=3)

button_7 = Button(root, text="7", width=4, height=1, bg="green",
                  command=lambda: concat("7"))
button_7.grid(row=3, column=0)

button_8 = Button(root, text="8", width=4, height=1, bg="green",
                  command=lambda: concat("8"))
button_8.grid(row=3, column=1)

button_9 = Button(root, text="9", width=4, height=1, bg="green",
                  command=lambda: concat("9"))
button_9.grid(row=3, column=2)

button_multiply = Button(root, text="*", width=4, height=1, bg="green",
                         command=lambda: arith_1("multiplication"))
button_multiply.grid(row=3, column=3)

button_4 = Button(root, text="4", width=4, height=1, bg="green",
                  command=lambda: concat("4"))
button_4.grid(row=4)

button_5 = Button(root, text="5", width=4, height=1, bg="green",
                  command=lambda: concat("5"))
button_5.grid(row=4, column=1)

button_6 = Button(root, text="6", width=4, height=1, bg="green",
                  command=lambda: concat("6"))
button_6.grid(row=4, column=2)

button_subtract = Button(root, text="-", width=4, height=1, bg="green",
                         command=lambda: arith_1("subtraction"))
button_subtract.grid(row=4, column=3)
#
#
button_1 = Button(root, text="1", width=4, height=1, bg="green",
                  command=lambda: concat("1"))
button_1.grid(row=5)
#
#
button_2 = Button(root, text="2", width=4, height=1, bg="green",
                  command=lambda: concat("2"))
button_2.grid(row=5, column=1)
#
#
button_3 = Button(root, text="3", width=4, height=1, bg="green",
                  command=lambda: concat("3"))
button_3.grid(row=5, column=2)
#
#
button_add = Button(root, text="+", width=4, height=1, bg="green",
                    command=lambda: arith_1("addition"))
button_add.grid(row=5, column=3)
#
#
button_sign = Button(root, text="+/-", width=4, height=1, bg="green")
button_sign.grid(row=6)
#
#
button_0 = Button(root, text="0", width=4, height=1, bg="green",
                  command=lambda: concat("0"))
button_0.grid(row=6, column=1)
#
#
button_decimal = Button(root, text=".", width=4, height=1, bg="green",
                        command=lambda: concat("."))
button_decimal.grid(row=6, column=2)
#
#
button_equal = Button(root, text="=", width=4, height=1, bg="green",
                      command=equals)
button_equal.grid(row=6, column=3)

status_bar = Frame(root)
status_bar.grid(row=7, column=3)
label_mode = Label(status_bar, text="STD", relief=SUNKEN, anchor=W)  # Should become 'textvariable' when SCI is ready
label_mode.grid(row=0)


root.mainloop()









