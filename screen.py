import tkinter as tk
import time
import pyscreenshot as ImageGrab

root = tk.Tk()
root.attributes("-fullscreen", True)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

screenshot = ImageGrab.grab()
screenshot.save("screenshot.png")
root.destroy()