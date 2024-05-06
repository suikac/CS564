import tkinter as tk
import time
import pyscreenshot as ImageGrab

# Create the main window object using tkinter
root = tk.Tk()
# Set the window to fullscreen by changing the attributes of the window
root.attributes("-fullscreen", True)

# Get the width of the screen using the winfo_screenwidth method of the root window
screen_width = root.winfo_screenwidth()
# Get the height of the screen using the winfo_screenheight method of the root window
screen_height = root.winfo_screenheight()

# Capture the current screen using the grab method from ImageGrab
screenshot = ImageGrab.grab()
# Save the captured screenshot to a file named "screenshot.png"
screenshot.save("screenshot.png")
# Destroy the root window to close the GUI application
root.destroy()