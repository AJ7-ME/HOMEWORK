from tkinter import *
import random

def play(user):
    computer = random.choice(["Rock", "Paper", "Scissors"])

    if user == computer:
        result.config(text="Draw!")
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissors" and computer == "Paper"):
        result.config(text="You Win!")
    else:
        result.config(text="Computer Wins!")

root = Tk()
root.title("Rock Paper Scissors App")
root.geometry("400x400")

Button(root, text="Rock", command=lambda: play("Rock")).pack(pady=10)
Button(root, text="Paper", command=lambda: play("Paper")).pack(pady=10)
Button(root, text="Scissors", command=lambda: play("Scissors")).pack(pady=10)

result = Label(root, text="")
result.pack(pady=20)

root.mainloop()