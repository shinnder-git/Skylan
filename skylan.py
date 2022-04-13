import win32gui, win32con
import os

hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide , win32con.SW_HIDE)

os.system(f"python code/app.py")

