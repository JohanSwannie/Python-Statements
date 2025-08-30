import tkinter as tk

def create_color_grid_app():
    """
    Creates a Tkinter application with an 81-box color grid.
    Clicking a box displays the color's name in a label below the grid.
    """
    root = tk.Tk()
    root.title("Color Grid")

    # A dictionary of 81 colors with their names and hex codes
    # This list can be customized with any valid Tkinter color names or hex codes
    color_map = {
        'red': '#FF0000', 'orange': '#FFA500', 'yellow': '#FFFF00', 'lime': '#00FF00', 'green': '#008000',
        'teal': '#008080', 'cyan': '#00FFFF', 'blue': '#0000FF', 'navy': '#000080',
        'purple': '#800080', 'violet': '#EE82EE', 'magenta': '#FF00FF', 'pink': '#FFC0CB', 'brown': '#A52A2A',
        'maroon': '#800000', 'beige': '#F5F5DC', 'tan': '#D2B48C', 'silver': '#C0C0C0', 'gray': '#808080',
        'black': '#000000', 'white': '#FFFFFF', 'snow': '#FFFAFA', 'salmon': '#FA8072', 'coral': '#FF7F50',
        'tomato': '#FF6347', 'darkorange': '#FF8C00', 'gold': '#FFD700', 'lemonchiffon': '#FFFACD', 'olive': '#808000',
        'palegreen': '#98FB98', 'seagreen': '#2E8B57', 'turquoise': '#40E0D0', 'cadetblue': '#5F9EA0', 'skyblue': '#87CEEB',
        'steelblue': '#4682B4', 'indigo': '#4B0082', 'mediumpurple': '#9370DB', 'hotpink': '#FF69B4', 'rosybrown': '#BC8F8F',
        'saddlebrown': '#8B4513', 'peru': '#CD853F', 'burlywood': '#DEB887', 'wheat': '#F5DEB3', 'gainsboro': '#DCDCDC',
        'lightgray': '#D3D3D3', 'dimgray': '#696969', 'honeydew': '#F0FFF0', 'mintcream': '#F5FFFA', 'azure': '#F0FFFF',
        'aliceblue': '#F0F8FF', 'ghostwhite': '#F8F8FF', 'mistyrose': '#FFE4E1', 'lavenderblush': '#FFF0F5', 'oldlace': '#FDF5E6',
        'ivory': '#FFFFF0', 'floralwhite': '#FFFAF0', 'seashell': '#FFF5EE', 'chocolate': '#D2691E', 'sandybrown': '#F4A460',
        'goldenrod': '#DAA520', 'darkkhaki': '#BDB76B', 'olivedrab': '#6B8E23', 'lawngreen': '#7CFC00', 'aquamarine': '#7FFFD4',
        'powderblue': '#B0E0E6', 'deepskyblue': '#00BFFF', 'royalblue': '#4169E1', 'slateblue': '#6A5ACD', 'plum': '#DDA0DD',
        'orchid': '#DA70D6', 'fuchsia': '#FF00FF', 'deeppink': '#FF1493', 'crimson': '#DC143C', 'firebrick': '#B22222',
        'darksalmon': '#E9967A', 'peachpuff': '#FFDAB9', 'navajowhite': '#FFDEAD', 'mocasin': '#FFE4B5', 'khaki': '#F0E68C',
        'paleturquoise': '#AFEEEE'
    }

    # Extract color names for display
    color_names = list(color_map.keys())
    
    # Check if there are 81 colors, and pad if necessary
    num_colors = 81
    if len(color_names) > num_colors:
        color_names = color_names[:num_colors]
    elif len(color_names) < num_colors:
        # Pad with a default color if needed
        color_names.extend(['lightgray'] * (num_colors - len(color_names)))

    # Function to update the label text
    def update_label(color_name):
        color_name_label.config(text=f"Selected Color: {color_name.capitalize()}")

    # Create a frame to hold the grid of color boxes
    grid_frame = tk.Frame(root)
    grid_frame.pack(padx=10, pady=10)

    # Create and place 81 color buttons (9x9 grid)
    for i in range(81):
        row = i // 9
        col = i % 9
        color_name = color_names[i]
        hex_code = color_map.get(color_name, '#FFFFFF')  # Use white as fallback
        
        # Use a lambda to capture the current color name for each button
        button = tk.Button(grid_frame,
                           bg=hex_code,
                           width=3, height=1,
                           command=lambda name=color_name: update_label(name))
        button.grid(row=row, column=col, padx=2, pady=2)

    # Create a label at the bottom to display the color name
    color_name_label = tk.Label(root, text="Click a box to see its color name", font=("Helvetica", 12))
    color_name_label.pack(pady=10)

    root.mainloop()

# Run the program
create_color_grid_app()
