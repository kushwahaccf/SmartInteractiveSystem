import tkinter as tk
class ListGenerator:
    def __init__(self, root,width,height,x,y):
        self.root = root
        self.list_items = []
        self.item_index = 0
        self.x=x
        self.y=y
        self.width=width
        self.height=height

        self.listbox = tk.Listbox(root, width=self.width, height=self.height,bg='black',fg='cyan')
        self.listbox.place(x=self.x, y=self.y)


    def generate_item(self):
        if self.item_index < len(self.list_items):
            item = self.list_items[self.item_index]
            self.item_index += 1
            self.listbox.insert(tk.END, item)
            self.root.after(2000, self.generate_item)
        else:
            self.listbox.delete(0, tk.END)  # Clear the listbox
            self.item_index = 0  # Reset the item index
            self.root.after(2000, self.generate_item)

    def start_generation(self, items):

        self.list_items = items
        self.item_index = 0
        self.generate_item()


