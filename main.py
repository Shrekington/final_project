import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("MAX")

# Remove windows decorations
root.overrideredirect(True)

# Set transparency transparency and background color
root.attributes('-transparentcolor', 'white')

# Load assistant image
image_path = "assets/images/mascot.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

# Create a label to hold the image
label = tk.Label(root, image=photo, bg='white')
label.pack()

# Bind a key to close the window
root.bind('<Escape>', lambda e: root.destroy())

# Run the application
root.mainloop()