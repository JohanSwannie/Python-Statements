
import tkinter as tk
import random

def random_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

root = tk.Tk()
root.title("81 Colored Boxes")

frame = tk.Frame(root)
frame.pack()

rows, cols = 9, 9

for i in range(rows):
    for j in range(cols):
        color = random_color()
        box = tk.Label(frame, width=5, height=2, bg=color)
        box.grid(row=i, column=j, padx=1, pady=1)

root.mainloop()