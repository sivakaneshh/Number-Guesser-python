from logging import disable
import tkinter as tk
import random
import math

# Define global variables
global n, minnum, maxnum, max_guesses
max_guesses = 0

def new_game():
    global n, minnum, maxnum, max_guesses
    minnum = int(min_entry.get())
    maxnum = int(max_entry.get())
    n = random.randint(minnum, maxnum)
    instruction_label.config(text=f"Guess a number between {minnum} and {maxnum}", font=("Arial", 11, "bold"))
    message_label.config(text="")
    guess_entry.delete(0, tk.END)
    guess_button.config(state=tk.NORMAL)
    
    # Calculate max_guesses based on the range
    range_size = maxnum - minnum + 1
    max_guesses = int(math.log2(range_size) + 1)
    update_guesses_label()  # Update the guesses left label

def check_guess():
    global max_guesses
    user_guess = int(guess_entry.get())

    if user_guess < n:
        message_label.config(text="Too low")
    elif user_guess > n:
        message_label.config(text="Too high!")
    else:
        message_label.config(text="You guessed it right!!")
        guess_button.config(state=tk.DISABLED)
        guess_entry.config(state=tk.DISABLED)

    # Decrement max_guesses after each guess
    max_guesses -= 1
    update_guesses_label()  # Update the guesses left label

    # Check if the player has reached the maximum number of guesses
    if max_guesses <= 0:
        message_label.config(text=f"Out of guesses. The correct number was {n}")
        guess_button.config(state=tk.DISABLED)
        guess_entry.config(state=tk.DISABLED)

def update_guesses_label():
    guesses_left_label.config(text=f"Guesses left: {max_guesses}")

root = tk.Tk()
root.geometry("300x300")
root.title("Number Guessing Game")

min_label = tk.Label(root, text="Enter the minimum range:", font=("Arial", 11, "bold"))
min_entry = tk.Entry(root)
max_label = tk.Label(root, text="Enter the maximum range:", font=("Arial", 11, "bold"))
max_entry = tk.Entry(root)
start_button = tk.Button(root, text="Start Game", command=new_game, font=("Arial", 10, "italic", "bold"))
instruction_label = tk.Label(root, text="")
guess_entry = tk.Entry(root)
guess_button = tk.Button(root, text="Check", command=check_guess, font=("Arial", 10, "italic", "bold"))
message_label = tk.Label(root, text="", fg="blue", font=("Arial", 10, "bold"))
guesses_left_label = tk.Label(root, text="", font=("Arial", 10, "bold"))
new_game_button = tk.Button(root, text="New Game", command=new_game, font=("Arial", 10, "italic", "bold"))

min_label.pack()
min_entry.pack()
max_label.pack()
max_entry.pack()
start_button.pack()
instruction_label.pack()
guess_entry.pack()
guess_button.pack()
message_label.pack()
guesses_left_label.pack()
new_game_button.pack()

root.mainloop()
