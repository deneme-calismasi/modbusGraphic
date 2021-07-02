import tkinter as tk
import time
from random import shuffle

root = tk.Tk()
root.geometry("400x200+200+200")
btn1 = tk.Button(root, text="butn_3")
btn1.place(relx=0.2, rely=0.5)
root.update()
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black", "white", "cyan"]

while True:
    shuffle(colors)
    for i in range(0, len(colors)):
        btn1.config(background=colors[i])
        btn1.update()
        time.sleep(1)

root.mainloop()
