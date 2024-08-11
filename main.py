import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("MAX")

# Load assistant image
image_path = "assets/images/mascot.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate poisition to place window in bottom right corner
window_width = photo.width()
window_height = photo.height()
taskbar_height = 80

x_position = screen_width - window_width
y_position = screen_height- window_height - taskbar_height

# Set the window size and poisition
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Set transparency transparency and background color
root.attributes('-transparentcolor', 'white')

# Create a label to hold the image
label = tk.Label(root, image=photo, bg='white')
label.pack()

# Bind a key to close the window
root.bind('<Escape>', lambda e: root.destroy())

# Run the application
root.mainloop()