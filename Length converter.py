from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Length Converter")
root.geometry("800x400")
def Length():
    user_input = length_entry.get()
    try:
        inches = float(user_input)
        cm = inches * 2.54
        result_label.config(text=f"Your Amount in CM is: {cm:.2f} cm")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
length_entry = Entry(root, width=30)
length_entry.pack(pady=10)
submit_btn = Button(root, text="Convert\nInches to CM", command=Length)
submit_btn.pack(pady=5)
result_label = Label(root, text="")
result_label.pack(pady=10)
root.mainloop()