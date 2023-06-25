import tkinter as tk

class JarvisWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Clock")
        self.root.iconbitmap('..\\Resources\\icon\\icon.ico')
        self.root.geometry("1366x768")
        self.root.attributes("-fullscreen", True)

    def run_jarvis(self):
        self.root.mainloop()


# Usage example
if __name__ == "__main__":
    jarvis = JarvisWindow()
    jarvis.run_jarvis()
