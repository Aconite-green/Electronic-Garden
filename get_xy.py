import tkinter as tk
import pyautogui
from pynput import keyboard

class CoordinateLogger:
    def __init__(self, root):
        self.root = root
        self.root.title("Mouse Coordinate Logger")
        self.text = tk.Text(self.root, height=15, width=50)
        self.text.pack()
        self.coordinates = []
        self.log_coordinates()
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

    def log_coordinates(self):
        x, y = pyautogui.position()
        self.root.after(100, self.log_coordinates)

    def on_press(self, key):
        try:
            if key.char == 'a':
                self.start_logging()
        except AttributeError:
            pass

    def start_logging(self):
        x, y = pyautogui.position()
        self.coordinates.append((x, y))
        self.text.insert(tk.END, f"{x}, {y}\n")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = CoordinateLogger(root)
    app.run()