import tkinter as tk

def on_button_click():
    print("Button clicked!")
    label_in_frame.config(text="You clicked the button!")


# Create the main window
root = tk.Tk()
root.title("Frame Example")

# Create a frame
my_frame = tk.Frame(root, bg="olive", bd=12, relief=tk.GROOVE)
my_frame.pack(padx=100, pady=100)

# Add widgets to the frame
label_in_frame = tk.Label(my_frame, text="This is inside the frame.")
label_in_frame.pack(padx=500, pady=255)

button_in_frame = tk.Button(my_frame, text="Frame Button", command=on_button_click)
button_in_frame.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()

