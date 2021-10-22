from tkinter import *


class CalculatorStd:
    def __init__(self, parent):
        self.parent = parent
        self.button_font = ('Verdana', 15)

        self.display = StringVar()
        self.display.set("0")
        self.display_label = Label(parent, textvariable=self.display, bd=2, anchor=E)
        self.display_label.grid(row=0, columnspan=7)

        self.status_bar = Frame(parent)
        self.status_bar.grid(row=7, column=2, columnspan=3)
        self.label_mode = Label(self.status_bar, text="STD", relief=SUNKEN)
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

        self.blank_button("", 1, 0)
        self.blank_button("", 1, 1)
        self.blank_button("", 1, 2)
        self.op_button("%", 1, 3, "percent")
        self.alt_button("CLR", 1, 4, "clear all")
        self.alt_button("C", 1, 5, "clear last")
        self.alt_button("<--", 1, 6, "backspace")

        self.blank_button("", 2, 0)
        self.blank_button("", 2, 1)
        self.blank_button("", 2, 2)
        self.alt_button("1/x", 2, 3, "reciprocal")
        self.alt_button("SQ", 2, 4, "square")
        self.alt_button("SQT", 2, 5, "square_root")
        self.op_button("/", 2, 6, "division")

        self.blank_button("", 3, 0)
        self.blank_button("", 3, 1)
        self.blank_button("", 3, 2)
        self.num_button("7", 3, 3)
        self.num_button("8", 3, 4)
        self.num_button("9", 3, 5)
        self.op_button("*", 3, 6, "multiplication")

        self.blank_button("", 4, 0)
        self.blank_button("", 4, 1)
        self.blank_button("", 4, 2)
        self.num_button("4", 4, 3)
        self.num_button("5", 4, 4)
        self.num_button("6", 4, 5)
        self.op_button("-", 4, 6, "subtraction")

        self.blank_button("", 5, 1)
        self.blank_button("", 5, 2)
        self.num_button("1", 5, 3)
        self.num_button("2", 5, 4)
        self.num_button("3", 5, 5)
        self.op_button("+", 5, 6, "addition")

        self.blank_button("", 6, 1)
        self.blank_button("", 6, 2)
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

    def blank_button(self, text_, x_, y_):
        self.b = Button(self.parent, text=text_, width=self.button_width, height=self.button_height,
                        bg="green")
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