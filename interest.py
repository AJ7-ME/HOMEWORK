from tkinter import *
def simple_interest():
    principal = float(entry_principal.get())
    rate = float(entry_rate.get())
    time = float(entry_time.get())
    interest = (principal * rate * time) / 100
    result.config(text=f"Interest: {interest:.2f}")
def compound_interest():
    principal = float(entry_principal.get())
    rate = float(entry_rate.get())
    time = float(entry_time.get())
    n = 1  # Yearly compounding
    amount = principal * (1 + (rate / (100 * n))) ** (n * time)
    interest = amount - principal
    result.config(text=f"Interest: {interest:.2f}")
root = Tk()
root.title("Interest Calculator")
root.geometry("400x400")
Label(root, text="Principal Amount:").grid(row=0, column=0)
entry_principal = Entry(root)
entry_principal.grid(row=0, column=1)
Label(root, text="Rate of Interest:").grid(row=1, column=0)
entry_rate = Entry(root)
entry_rate.grid(row=1, column=1)
Label(root, text="Time (in years):").grid(row=2, column=0)
entry_time = Entry(root)
entry_time.grid(row=2, column=1)
Button(root, text="Calculate Simple Interest", command=simple_interest).grid(row=3, column=0, columnspan=2)
Button(root, text="Calculate Compound Interest", command=compound_interest).grid(row=3, column=2, columnspan=2)
result = Label(root, text="")
result.grid(row=4, column=0, columnspan=2)
root.mainloop()