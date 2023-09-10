from tkinter import *
import random


def roll_dice():
    num_dice = int(entry_window.get())
    results = []
    for _ in range(num_dice):
        result = random.randint(1, 6)
        results.append(result)
        
    result_label.config(text="Results: " + ", ".join(map(str, results)))
    btn_roll.pack_forget()
    btn_play_again.pack()
    btn_quit.pack()
    
    
def play_again():
    entry_window.delete(0, END)
    result_label.config(text="")
    btn_play_again.pack_forget()
    btn_quit.pack_forget()
    btn_roll.pack()


root = Tk()
root.title("Dice Roller")
root.geometry("500x200")

label = Label(root, text="Enter the number of dice to roll")
label.pack()

entry_window = Entry(root)
entry_window.pack()

btn_roll = Button(root, text="Roll", command=roll_dice)
btn_roll.pack()

result_label = Label(root, text="")
result_label.pack()

btn_play_again = Button(root, text="play again", command=play_again)
btn_quit = Button(root, text="Quit", command=root.destroy)


root.mainloop()
