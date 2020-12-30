from tkinter import *
from tkinter.messagebox import showinfo
import csv
import random
import subprocess

rows = []
check_buttons = []
random_letters = ['F', 'A', 'B', 'C', 'D', 'E', '1', '0', '2', '3', '4', '5', '6']

def onSave():

    cycles = (e1.get())
    if int(cycles) > 1000000 or int(cycles) <=0:
        showinfo("Too Many words ", "Please enter number less than 10 and greater than 0")
        return
    e = Label(text="Data", font=('Helvetica', 18, 'bold'))
    e.grid(row=4, column=1)

    e = Label(text="C_BE", font=('Helvetica', 18, 'bold'))
    e.grid(row=4, column=2)
    for i in range(7, 7+int(cycles)):
        cols = []
        for j in range(0, 2):
            e = Entry(width=20, fg='blue',
                      font=('Arial', 16, 'bold'))
            e.grid(row=i, column=j+1, sticky=NSEW)
            if j == 0:
                rnd = ''.join(random.choice(random_letters) for _ in range(4))
            elif j == 1:
                rnd = ''.join(str(random.choice([0, 1])) for _ in range(4))

            e.insert(END, rnd)
            cols.append(e)
        rows.append(cols)
        cb_statues = IntVar()
        check_buttons.append(cb_statues)
        cb_statues.set(1)
        cb = Checkbutton(text="TRDY", variable=cb_statues)
        cb.grid(row=i, sticky=W)
    Button(text='Generate', command=read).grid()


e0 = Label(text="Number of words")
e0.grid(row=0,column=0)
e1 = Entry(width=20, fg='red',
                  font=('Arial', 16, 'bold'))
e1.grid(row=1, column=0, sticky=NSEW)
e1.insert(END, '0')
Button(text='Read', command=onSave, width=10, height=2).grid()
Button(text='Write',  command=onSave, width=10, height=2).grid()


def read():
    print(check_buttons[0].get())
    # name of csv file
    filename = "scripts/data.csv"

    fields = ['Data', 'C_BE', 'TRDY']
    rows_mod = []
    counter = 0
    for row in rows:
        rows_mod.append([])
        for col in row:
            rows_mod[counter].append("1"+str(col.get()))
            print(col.get())
            print("----", len(col.get()))
            if len(col.get()) > 4:
                showinfo("Word format error", "Please enter the word in hexa format, you should enter only 4 letters")
                return
        if check_buttons[counter].get() == 0:
            rows_mod[counter].append(1)
        else:
            rows_mod[counter].append(0)
        counter += 1
    print(rows_mod)
    # writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        csvwriter.writerow(fields)

        # writing the data rows
        csvwriter.writerows(rows_mod)
    subprocess.call([r'sa.bat'])
    exit()

mainloop()
