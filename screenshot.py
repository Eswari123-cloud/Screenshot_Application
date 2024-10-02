from unicodedata import name
import pyautogui
import time
import tkinter as tk

def screenshot():
    time.sleep(5)
    name = time.time()
    name = 'C:/Users/NEW/{}.png'.format(name)
    img = pyautogui.screenshot()
    img.save(name)
    img.show()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame,text="Take ScreenShot",command=screenshot)
button.pack(side=tk.LEFT)

close = tk.Button(frame,text="Quit",command=quit)
close.pack(side=tk.LEFT)

root.mainloop()
