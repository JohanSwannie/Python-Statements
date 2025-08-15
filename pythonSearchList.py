import tkinter as tk

from tkinter import messagebox


names_list = ["Helen", "Barnie", "Luke", "Mary", "Adam", "John", "Jules", "Richard", "Ron", "Matthew", "Carl", "Kim"]


def search_name():

    name = entry.get().strip()

    if name in names_list:

        messagebox.showinfo("Search Result", f"{name} is in the list.")

    else:

        messagebox.showinfo("Search Result", f"{name} is NOT in the list.")


root = tk.Tk()

root.title("Name Search")

label = tk.Label(root, text="Enter a name to search:")

label.pack(pady=5)

entry = tk.Entry(root)

entry.pack(pady=5)

search_button = tk.Button(root, text="Search", command=search_name)

search_button.pack(pady=5)

root.mainloop()