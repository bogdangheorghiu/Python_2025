

import tkinter as tk
from tkinter import messagebox
import time
import random


I_AM_NOT_HUNGRY = "I am NOT hungry."
I_AM_HUNGRY = "I am hungry."
I_AM_HAPPY = "I am happy !!!"
DONT_FEED_ME = "Don't feed me"
FEED_ME = "Feed me"

WIN_SIZE = 500

main_window = tk.Tk()


status_label = tk.Label(main_window, text=I_AM_NOT_HUNGRY)
status_label.pack()

is_game_running = True
is_hungry = False

new_frame = tk.Frame(main_window)
new_frame.pack()

def give_food():
    global is_game_running
    if not is_game_running:
        return
    
    print("give_food is called")
    if is_hungry:
        print("You winn")
        stop_time = time.time()
        delta = stop_time - start_time
        messagebox.showinfo(title="Congrats !", message=f"You win in {delta} seconds!!")
        status_label.config(text=I_AM_HAPPY)
        feed_button.config(text=DONT_FEED_ME)
    else:
        print("You losse")
        messagebox.showerror(title="Uuuuu!", message="You lost my fried !")






def show_i_am_hungry():
    global is_hungry
    print("Tamagocci is hungry")
    status_label.config(text=I_AM_HUNGRY)
    feed_button.config(text=FEED_ME)
    is_hungry = True


feed_button = tk.Button(new_frame, text=DONT_FEED_ME, command=give_food)
feed_button.grid()


main_window.geometry(f"{WIN_SIZE}x{WIN_SIZE}")

status_label.after(3000, show_i_am_hungry)
start_time = time.time()


main_window.mainloop()


