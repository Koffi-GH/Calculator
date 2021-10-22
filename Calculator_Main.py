# Scientific is currently WIP. Could just add its extra functions to the Standard calc but learning to switch be helpful
from tkinter import *
from Calculator_Std_file import *
from Calculator_Sci_file import *


class Ui:
    def __init__(self, master):
        self.master = master
        master.title("Edwin's Calculator")
        # master.geometry("180x200")

        self.my_menu = Menu(master)
        master.config(menu=self.my_menu)

        self.submenu_file = Menu(self.my_menu)
        self.my_menu.add_cascade(label="File", menu=self.submenu_file)
        self.submenu_file.add_command(label="Exit", command=master.quit)

        self.submenu_switch = Menu(self.my_menu)
        self.my_menu.add_cascade(label="Switch", menu=self.submenu_switch)
        self.submenu_switch.add_command(label="Switch", command=self.switch_frame)

        container = Frame(master)
        container.pack(side="top", fill="both", expand=True)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        self.master.bind("<Shift_L>", self.shift_press)

        self.frames = {}                            # Dictionary of both calculator frames
        self.frame_flag = 2                         # Setting it to be standard calc by default

        calc_frame1 = StdFrame(container)
        self.frames["std"] = calc_frame1
        calc_frame1.grid(row=0, column=0, sticky="nsew")

        calc_frame2 = SciFrame(container)
        self.frames["sci"] = calc_frame2
        calc_frame2.grid(row=0, column=0, sticky="nsew")

        self.switch_frame()

    def switch_frame(self):
        if self.frame_flag == 1:                        # Switching from std to sci
            active_frame = self.frames["sci"]
            self.frame_flag = 2

        else:                                           # Switching from sci to std
            active_frame = self.frames["std"]
            self.frame_flag = 1

        active_frame.tkraise()

    def shift_press(self, event):
        self.switch_frame()


class StdFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        my_calculator = CalculatorStd(self)
        Ui.frame_flag = 1


class SciFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        my_calculator = CalculatorSci(self)
        Ui.frame_flag = 2


root = Tk()
calculator_UI = Ui(root)
root.mainloop()

