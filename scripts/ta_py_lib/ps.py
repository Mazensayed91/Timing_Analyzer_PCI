import tkinter
from tkinter import ttk
from tkinter import StringVar
from tkinter import messagebox
from tkinter import Entry
from tkinter import Button
import os
import subprocess
import re
import subprocess


class Sys(tkinter.Frame):

    def checkhex(self, h):
        for x in range(len(h)):
            if (h[x] == '0' or h[x] == '1' or h[x] == '2' or h[x] == '3' or h[x] == '4' or h[x] == '5' or h[x] == '6' or
                    h[x] == '7' or h[x] == '9' or h[x] == 'a' or h[x] == 'b' or h[x] == 'c' or h[x] == 'd' or h[
                        x] == 'e' or h[x] == 'f' or h[x] == 'A' or h[x] == 'B' or h[x] == 'C' or h[x] == 'D' or h[
                        x] == 'E' or h[x] == 'F'):
                # print(1)
                pass
            else:
                return Fals

    def array_of_inputs(self):

        if (self.in1.get() == ''):
            messagebox.showerror('Error', 'Please enter a decimal number')
            return False
        else:
            self.l3 = tkinter.Label(self.parent, text="Input fields", font=("Times New Roman Bold", 24)).place(
                relx=0.41, rely=0.15)
            a = int(self.in1.get())
            i = 0
            r_label = 0.23
            r_entry = 0.233
            self.Data = {}
            self.BE = {}
            while (i <= a):
                self.Data[i] = StringVar()
                self.BE[i] = StringVar()
                if (i == 0):
                    self.l4 = tkinter.Label(self.parent, text="Enter Address in hexadecimal",
                                            font=("Cambria", 12)).place(relx=0.012, rely=r_label)
                    self.entry4 = tkinter.Entry(self.parent, textvariable=self.Data[i], validate="key", width=5,
                                                font=("Cambria", 12))
                    self.entry4['validatecommand'] = (self.entry4.register(self.testValHexadecimal), '%P', '%d')
                    self.entry4.place(relx=0.265, rely=r_entry)
                    self.l5 = tkinter.Label(self.parent, text="Enter Command in binary", font=("Cambria", 12)).place(
                        relx=0.685, rely=r_label)
                    self.entry5 = tkinter.Entry(self.parent, textvariable=self.BE[i], width=5, font=("Cambria", 12))
                    self.entry5.place(relx=0.921, rely=r_entry)
                    self.parent.update()
                else:
                    self.l4 = tkinter.Label(self.parent, text="Enter Data in hexadecimal", font=("Cambria", 12)).place(
                        relx=0.012, rely=r_label)
                    self.entry4 = tkinter.Entry(self.parent, textvariable=self.Data[i], validate="key", width=5,
                                                font=("Cambria", 12))
                    self.entry4['validatecommand'] = (self.entry4.register(self.testValHexadecimal), '%P', '%d')
                    self.entry4.place(relx=0.235, rely=r_entry)
                    self.l5 = tkinter.Label(self.parent, text="Enter Byte Enable in binary",
                                            font=("Cambria", 12)).place(relx=0.685, rely=r_label)
                    self.entry5 = tkinter.Entry(self.parent, textvariable=self.BE[i], width=5, font=("Cambria", 12))
                    self.entry5.place(relx=0.921, rely=r_entry)
                    self.parent.update()
                i += 1
                r_entry += 0.05
                r_label += 0.05
            self.bt2 = Button(self.parent, text="               Send Data               ", font=("Times New Roman", 16),
                              bg="#7bd45d", command=self.getAll).place(relx=0.365, rely=r_label)

    def getAll(self):
        self.data = []
        self.be = []
        for x in self.Data:
            if (self.Data[x].get() == '' or self.BE[x].get() == ''):
                messagebox.showerror('Error', 'Please fill the empty entry')
                return False
            else:
                self.data.append(self.Data[x].get())
                self.be.append(self.BE[x].get())
        file1 = open("scripts/data.txt", "w")
        for i in range(len(self.data)):
            file1.write(self.data[i])
            file1.write("\n")

        for i in range(len(self.be)):
            file1.write(self.be[i])
            file1.write("\n")
        file1.flush()
        subprocess.call([r'sa.bat'])

    def getAD(self):
        return self.data

    def getC_BE(self):
        return self.be

    def testValDecimal(self, inStr, acttyp):
        if (acttyp == '1'):
            try:
                if (isinstance(int(inStr), int)):
                    1
            except:
                return False
        return True

    def testValHexadecimal(self, inStr, acttyp):
        if (acttyp == '1'):
            try:
                if (self.checkhex(inStr)):
                    1
            except:
                return False
        return True

    def __init__(self, parent):

        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.in1 = StringVar()
        self.label1 = tkinter.Label(self.parent, text="CO Visualizer", font=("Times New Roman Bold", 30)).place(
            relx=0.36, rely=0.01)
        self.label2 = tkinter.Label(self.parent, text="Number of words", font=("Cambria", 16)).place(relx=0.01,
                                                                                                     rely=0.1)
        self.entry = tkinter.Entry(self.parent, textvariable=self.in1, validate="key", width=10, font=("Cambria", 16))
        self.entry['validatecommand'] = (self.entry.register(self.testValDecimal), '%P', '%d')
        self.entry.place(relx=0.21, rely=0.1)
        self.bt1 = Button(self.parent, text="Generate", font=("Times New Roman", 11), bg="lightblue",
                          command=self.array_of_inputs).place(relx=0.37, rely=0.098)


def simpo():
    subprocess.call('java -jar jlib\jython.jar', shell=True)


def main():
    window = tkinter.Tk()
    window.withdraw()
    window.title("CO Visualizer")
    window.geometry('845x700+230+0')
    window.resizable(0, 0)
    Sys(window).place(relx=1, rely=1)
    window.deiconify()
    window.mainloop()


if __name__ == "__main__":
    main()

execfile('start_app.py')

from ta_py_lib.ta.app import *
from ta_py_lib.td.logic import *
from ta_py_lib.td.commands import *
import os

td = new_timing_diagram(taApp)

start_script(td)

AD = []
C_BE = []
# exec(open('CO_GUI.py').read())
os.system('CO_GUI.py')
file1 = open("scripts\data.txt", "r+")
AD_file = file1.readlines()
file1.flush()
index = len(AD_file) / 2
for i in range(int(index)):
    AD.append(AD_file[i][0:-1])
    C_BE.append(AD_file[i + int(index)][0:-1])

no_of_data = len(AD) - 1

clk = add_digital_clock(td, "CLK", "L", 10e7)

sigFrame = add_digital_signal(td, "Frame", "H")
tf_frame = 10.0 * no_of_data

sigAD = add_digital_bus(td, "AD[31:0]", "Z", "HEX")
sigC_BE = add_digital_bus(td, "C_BE[3:0]", "Z", "BIN")
sigDEVSEL = add_digital_signal(td, "DEVSEL", "H")
sigTRDY = add_digital_signal(td, "TRDY", "H")

########################################################################

if C_BE[0] == "0111":

    #   Frame
    add_pulse(sigFrame, 10.0, tf_frame + 10.0, "L")

    #   AD
    for i in range(len(AD)):
        add_edge(sigAD, 10.0 + (i * 10), AD[i])

    add_edge(sigAD, len(AD) * 10 + 10.0, "Z")

    # C_BE
    for i in range(len(C_BE)):
        add_edge(sigC_BE, 10.0 + (i * 10), C_BE[i])

    add_edge(sigC_BE, len(C_BE) * 10 + 10.0, "Z")

    # DEVSEL
    add_pulse(sigDEVSEL, 20.0, tf_frame + 20, "L")

    # TRDY
    add_pulse(sigTRDY, 20.0, tf_frame + 20, "L")


elif C_BE[0] == "0110":

    #   Frame
    add_pulse(sigFrame, 10.0, tf_frame + 20.0, "L")

    #   AD
    flag = False
    for i in range(len(AD)):
        if (i == 1):
            add_edge(sigAD, 10.0 + (i * 10), "Z")
            flag = True

        if flag:
            add_edge(sigAD, 20.0 + (i * 10), AD[i])
            flag = False
        else:
            if i == 0:
                add_edge(sigAD, 10.0 + (i * 10), AD[i])
            else:
                add_edge(sigAD, 20.0 + (i * 10), AD[i])

    add_edge(sigAD, len(AD) * 10 + 20.0, "Z")

    # C_BE
    for i in range(1):
        add_edge(sigC_BE, 10.0 + (i * 10), C_BE[i])

    add_edge(sigC_BE, len(AD) * 10 + 20.0, "Z")

    # DEVSEL
    add_pulse(sigDEVSEL, 20.0, tf_frame + 30, "L")

    # TRDY
    add_pulse(sigTRDY, 20.0, tf_frame + 30, "L")

############################################################################


stop_script(td)

