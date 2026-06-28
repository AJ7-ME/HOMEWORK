from tkinter import *
from datetime import date

def age():
    today = date.today()

    d = int(day.get())
    m = int(month.get())
    y = int(year.get())

    a = today.year - y

    if (today.month, today.day) < (m, d):
        a -= 1

    result.config(text="Hello " + name.get() + "! You are " + str(a) + " years old.")

root = Tk()
root.title("Age Calculator App")
root.geometry("400x400")

Label(root, text="Name").grid(row=0, column=0)
name = Entry(root)
name.grid(row=0, column=1)

Label(root, text="Date").grid(row=1, column=0)
day = Entry(root)
day.grid(row=1, column=1)

Label(root, text="Month").grid(row=2, column=0)
month = Entry(root)
month.grid(row=2, column=1)

Label(root, text="Year").grid(row=3, column=0)
year = Entry(root)
year.grid(row=3, column=1)

Button(root, text="Calculate Age", command=age).grid(row=4, column=0, columnspan=2)

result = Label(root, text="")
result.grid(row=5, column=0, columnspan=2)

root.mainloop()