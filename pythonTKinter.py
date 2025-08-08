import tkinter as tk

def on_button_click():
    print("Button clicked!")
    label_in_frame.config(text="You clicked the button again!")


# Create the main window
root = tk.Tk()
root.title("Frame Example")

# Create a frame
my_frame = tk.Frame(root, bg="olive", bd=12, relief=tk.GROOVE)
my_frame.pack(fill=tk.BOTH, expand=True)

# Add widgets to the frame
label_in_frame = tk.Label(my_frame, width=40, height=40, text="This is inside the frame.")
label_in_frame.pack(padx=400, pady=10)

button_in_frame = tk.Button(my_frame, text="Frame Button", command=on_button_click())
button_in_frame.pack(pady=5, padx=100)

# Start the Tkinter event loop
root.mainloop()


