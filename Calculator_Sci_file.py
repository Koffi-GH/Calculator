# Note: ALL trig functions are evaluated using radians
from tkinter import *
from math import *


class CalculatorSci:
    def __init__(self, parent):
        self.parent = parent
        self.button_font = ('Verdana', 15)

        self.display = StringVar()
        self.display.set("0")
        self.display_label = Label(parent, textvariable=self.display, bd=2, anchor=E)
        self.display_label.grid(row=0, columnspan=7)

        self.status_bar = Frame(parent)
        self.status_bar.grid(row=7, column=2, columnspan=3)
        self.label_mode = Label(self.status_bar, text="SCI", relief=SUNKEN)
        self.label_mode.grid(row=0, sticky="ew")

        self.list_of_digits = []
        self.b = None
        self.joined_digits = None
        self.result_1 = None            # most recent number.
        self.result_2 = None            # stored number from previous operation.
        self.symbol = None
        self.previous_operator = None
        self.equals_flag = None

        self.parent.bind("<Key>", self.key_press)
        self.parent.bind("<Delete>", self.del_press)
        self.parent.bind("<Escape>", self.clr_press)
        self.parent.bind("<Return>", self.enter_press)
        self.parent.bind("<BackSpace>", self.bksp_press)

        self.button_height = 1
        self.button_width = 6

        self.alt_button("pi", 1, 0, "pi")
        self.alt_button("cos", 1, 1, "cos")
        self.alt_button("x!", 1, 2, "factorial")
        self.op_button("%", 1, 3, "percent")
        self.alt_button("CLR", 1, 4, "clear all")
        self.alt_button("C", 1, 5, "clear last")
        self.alt_button("<--", 1, 6, "backspace")

        self.alt_button("deg/rad", 2, 0, "to rad")
        self.alt_button("sin", 2, 1, "sin")
        self.op_button("10^x", 2, 2, "EE")
        self.alt_button("1/x", 2, 3, "reciprocal")
        self.alt_button("SQ", 2, 4, "square")
        self.alt_button("SQT", 2, 5, "square_root")
        self.op_button("/", 2, 6, "division")

        self.alt_button("rad/deg", 3, 0, "to deg")
        self.alt_button("tan", 3, 1, "tan")
        self.op_button("x^y", 3, 2, "custom power")
        self.num_button("7", 3, 3)
        self.num_button("8", 3, 4)
        self.num_button("9", 3, 5)
        self.op_button("*", 3, 6, "multiplication")

        self.alt_button("abs", 4, 0, "abs")
        self.alt_button("arccos", 4, 1, "acos")
        self.alt_button("log", 4, 2, "log")
        self.num_button("4", 4, 3)
        self.num_button("5", 4, 4)
        self.num_button("6", 4, 5)
        self.op_button("-", 4, 6, "subtraction")

        self.alt_button("arcsin", 5, 1, "asin")
        self.alt_button("e", 5, 2, "e")
        self.num_button("1", 5, 3)
        self.num_button("2", 5, 4)
        self.num_button("3", 5, 5)
        self.op_button("+", 5, 6, "addition")

        self.alt_button("arctan", 6, 1, "atan")
        self.alt_button("ln", 6, 2, "ln")
        self.alt_button("+/-", 6, 3, "sign")
        self.num_button("0", 6, 4)
        self.num_button(".", 6, 5)
        self.alt_button("=", 6, 6, "evaluation")

    def num_button(self, text_, x_, y_):                                                                        # For digits and decimal point
        self.b = Button(self.parent, text=text_, width=self.button_width, height=self.button_height,
                        bg="green3", command=lambda: self.concat(text_))
        self.b.grid(row=x_, column=y_)

    def op_button(self, text_, x_, y_, op):                                                                     # For addition, subtraction, multiplication, and division
        self.b = Button(self.parent, text=text_, width=self.button_width, height=self.button_height,
                        bg="green", command=lambda: self.arith_1(op))
        self.b.grid(row=x_, column=y_)

    def alt_button(self, text_, x_, y_, alt_function):                                                          # For everything else?
        self.b = Button(self.parent, text=text_, width=self.button_width, height=self.button_height,
                        bg="green", command=lambda: self.alternate_fn(alt_function))
        self.b.grid(row=x_, column=y_)

    def concat(self, digit):
        if digit == "." and self.list_of_digits.count("."):
            pass

        else:
            try:
                self.list_of_digits.append(digit)                           # list of multiple strings
                self.joined_digits = "".join(self.list_of_digits)           # one single string
                self.display.set(self.joined_digits)
                self.result_1 = float(self.joined_digits)
            except ValueError:
                pass

            # self.list_of_digits.append(digit)                         # Tried using only 1 variable
            # self.list_of_digits = "".join(self.list_of_digits)
            # self.display.set(self.list_of_digits)
            # self.list_of_digits = [self.list_of_digits]

    def key_press(self, event):                     # Keyboard bindings for digits and a few calc fns ________________
        key = event.char
        if key.isdigit() or key == ".":
            self.concat(key)
        elif key == "+":
            self.arith_1("addition")
        elif key == "-":
            self.arith_1("subtraction")
        elif key == "*":
            self.arith_1("multiplication")
        elif key == "/":
            self.arith_1("division")
        elif key == "+":
            self.arith_1("addition")

    def enter_press(self, event):
        self.alternate_fn("evaluation")

    def bksp_press(self, event):
        self.alternate_fn("backspace")

    def clr_press(self, event):
        self.alternate_fn("clear all")

    def del_press(self, event):
        self.alternate_fn("clear last")                 # End of bindings ------------------------------------|

    def arith_1(self, operation_1):
        if self.result_2 is None:
            self.result_2 = self.result_1
            self.previous_operator = operation_1

        elif self.equals_flag == "yes":                  # flag to ensure a subsequent operation can occur after an '='
            self.previous_operator = operation_1

        else:
            if self.previous_operator == "addition":
                self.result_2 += self.result_1

            elif self.previous_operator == "subtraction":
                self.result_2 -= self.result_1

            elif self.previous_operator == "multiplication":
                self.result_2 *= self.result_1

            elif self.previous_operator == "division":
                self.result_2 /= self.result_1

            elif self.previous_operator == "percent":
                self.result_2 = self.result_2 * self.result_1 / 100

            elif self.previous_operator == "EE":
                self.result_2 = self.result_2 * (10 ** self.result_1)

            elif self.previous_operator == "custom power":
                self.result_2 = self.result_2 ** self.result_1

            self.previous_operator = operation_1

        self.display.set(str(self.result_2))
        self.list_of_digits = []
        self.joined_digits = None
        self.result_1 = None
        self.equals_flag = None

    def alternate_fn(self, function):
        if function == "evaluation":
            if self.result_2 is None:
                pass

            elif self.previous_operator == "addition":  # Heavy code repetition here, improve.
                self.result_2 += self.result_1

            elif self.previous_operator == "subtraction":
                self.result_2 -= self.result_1

            elif self.previous_operator == "multiplication":
                self.result_2 *= self.result_1

            elif self.previous_operator == "division":
                self.result_2 /= self.result_1

            elif self.previous_operator == "percent":
                self.result_2 = self.result_2 * self.result_1 / 100

            elif self.previous_operator == "EE":
                self.result_2 = self.result_2 * (10 ** self.result_1)

            elif self.previous_operator == "custom power":
                self.result_2 = self.result_2 ** self.result_1

            self.display.set(str(self.result_2))
            self.list_of_digits = []
            self.joined_digits = None
            self.equals_flag = "yes"

        elif function == "clear all":
            self.list_of_digits = []
            self.joined_digits = None
            self.result_1 = None
            self.result_2 = None
            self.previous_operator = None
            self.display.set("0")

        elif function == "clear last":
            self.list_of_digits = []
            self.joined_digits = None
            self.result_1 = None

        elif function == "reciprocal":      # Can only be done stand-alone, not continuous
            self.result_2 = 1 / self.result_1
            self.display.set(str(self.result_2))

        elif function == "square":
            self.result_2 = self.result_1 ** 2
            self.display.set(str(self.result_2))

        elif function == "square_root":
            self.result_2 = self.result_1 ** 0.5
            self.display.set(str(self.result_2))

        elif function == "backspace":
            self.list_of_digits.pop()
            self.joined_digits = "".join(self.list_of_digits)
            self.display.set(self.joined_digits)
            self.result_1 = float(self.joined_digits)

        elif function == "sign":
            if self.result_2 is None:
                self.result_2 = self.result_1 * (-1)
            else:
                self.result_2 = self.result_2 * (-1)

            self.display.set(str(self.result_2))

        elif function == "ln":
            self.result_2 = log(self.result_1)
            self.display.set(str(self.result_2))

        elif function == "e":
            self.result_2 = exp(self.result_1)
            self.display.set(str(self.result_2))

        elif function == "log":
            self.result_2 = log10(self.result_1)
            self.display.set(str(self.result_2))

        elif function == "factorial":
            self.result_2 = factorial(self.result_1)
            self.display.set(str(self.result_2))

        elif function == "abs":
            self.result_2 = abs(self.result_1)
            self.display.set(str(self.result_2))

        elif function == "to rad":
            self.result_2 = self.result_1 * (pi / 180)
            self.display.set(str(self.result_2))

        elif function == "to deg":
            self.result_2 = self.result_1 * (180 / pi)
            self.display.set(str(self.result_2))

        elif function == "pi":
            self.result_1 = pi
            self.display.set(str(self.result_1))

        # Angles measured in radians
        elif function == "acos":
            self.result_2 = acos(self.result_1)
            self.display.set(str(self.result_2))

        elif function == "asin":
            self.result_2 = asin(self.result_1)
            self.display.set(str(self.result_2))

        elif function == "atan":
            self.result_2 = atan(self.result_1)
            self.display.set(str(self.result_2))

        elif function == "cos":
            self.result_2 = cos(self.result_1)
            self.display.set(str(self.result_2))

        elif function == "sin":
            self.result_2 = sin(self.result_1)
            self.display.set(str(self.result_2))

        elif function == "tan":
            self.result_2 = tan(self.result_1)
            self.display.set(str(self.result_2))

