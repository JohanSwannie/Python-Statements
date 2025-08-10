import tkinter as tk

def on_button_click():
    if begin:
        begin.set(False)
        displayTotal = total.get()
        print("Button clicked!")
    else:
        total.set(2)
        displayTotal = total.get()
    display_text.set(f"You have clicked on the buton {displayTotal} times")
    label_in_frame.config(textvariable=display_text)

# Create the main window
root = tk.Tk()
root.title("Frame Example")

begin = tk.BooleanVar(value=True)
total = tk.IntVar(root, value=1)
display_text = tk.StringVar()

# Create a frame
my_frame = tk.Frame(root, bg="olive", bd=12, relief=tk.GROOVE)
my_frame.pack(fill=tk.BOTH, expand=True)

# Add widgets to the frame
label_in_frame = tk.Label(my_frame, width=40, height=40, text="This is inside the frame.")
label_in_frame.pack(padx=400, pady=10)

button_in_frame = tk.Button(my_frame, text="Frame Button", command=on_button_click)
button_in_frame.pack(pady=5, padx=100)

# Start the Tkinter event loop
root.mainloop()


