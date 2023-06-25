import tkinter as tk
from tkinter import messagebox

class MessageBox:
    def __init__(self, root):
        self.root = root

    def show_message(self, title, message):
        messagebox.showinfo(title, message)
