from logging import disable
import tkinter as tk
import random

def new_game():
    global n, minnum, maxnum
    minnum = int(min_entry.get())
    maxnum = int(max_entry.get())
    n = random.randint(minnum, maxnum)
    instruction_label.config(text=f"Guess a number between {minnum} and {maxnum}",font=("Arial",11,"bold"))
    message_label.config(text="")
    guess_entry.delete(0, tk.END)
    guess_button.config(state=tk.NORMAL)

def check_guess():
    user_guess = int(guess_entry.get())
    if user_guess < n:
        message_label.config(text="Too low")
    elif user_guess > n:
        message_label.config(text="Too high!")
    else:
        message_label.config(text="You guessed it right!!")
        guess_button.config(state=tk.DISABLED)
        guess_entry.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Number Guessing Game")

min_label = tk.Label(root, text="Enter the minimum range:",font=("Arial",11,"bold"))
min_entry = tk.Entry(root)
max_label = tk.Label(root, text="Enter the maximum range:",font=("Arial",11,"bold"))
max_entry = tk.Entry(root)
start_button = tk.Button(root, text="Start Game", command=new_game,font=("Arial",10,"italic","bold"))
instruction_label = tk.Label(root, text="")
guess_entry = tk.Entry(root)
guess_button = tk.Button(root, text="Check", command=check_guess,font=("Arial",10,"italic","bold"))
message_label = tk.Label(root, text="", fg="blue",font=("Arial",10,"bold"))
new_game_button = tk.Button(root, text="New Game", command=new_game,font=("Arial",10,"italic","bold"))

min_label.pack()
min_entry.pack()
max_label.pack()
max_entry.pack()
start_button.pack()
instruction_label.pack()
guess_entry.pack()
guess_button.pack()
message_label.pack()
new_game_button.pack()

root.mainloop()
