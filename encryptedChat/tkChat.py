import tkinter as tk
from tkinter import ttk
from enc import Encryptor

class Chat(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_input()
        self.create_output()
        self.enc = Encryptor()   

    def create_input(self):
        self.input = tk.Entry(self)
        self.input.pack(side=tk.BOTTOM, fill=tk.X, expand=True, padx=5, pady=5)
        self.input.bind('<Return>', self.send_msg)

    def create_output(self):
        self.output = tk.Text(self)
        self.output.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5, anchor=tk.NW, ipadx=5, ipady=5)

    def send_msg(self, event):
        msg = self.input.get()
        self.input.delete(0, tk.END)
        self.output.insert(1.0, 'You: ' + self.enc.encrypt(msg).decode('utf-8') + '\n')   
        





root = tk.Tk()
root.title("tkChat")
app = Chat(master=root)
app.mainloop()