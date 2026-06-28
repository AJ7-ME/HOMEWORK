from tkinter import *
def check():
    password = entry.get()
    if len(password) <= 5:
        result.config(text="Weak", fg="red")
    elif len(password) <= 8:
        result.config(text="Medium", fg="yellow")
    elif len(password) <= 12:
        result.config(text="Strong", fg="light green")
    else:
        result.config(text="Very Strong", fg="dark green")
root = Tk()
root.title("Length Converter App")
root.geometry("400x400")
Label(root, text="Password").grid(row=0, column=0)
entry = Entry(root, show="*")
entry.grid(row=0, column=1)
Button(root, text="Check", command=check).grid(row=1, column=0, columnspan=2)
result = Label(root, text="")
result.grid(row=2, column=0, columnspan=2)
root.mainloop()