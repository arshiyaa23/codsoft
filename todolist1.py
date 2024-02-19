
import tkinter as tk
from tkinter import messagebox

def addt():
    task = e1.get()
    if task:
        listbox.insert(tk.END, task)
        e1.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter the task to add.")

def dlt():
    dlt_task = listbox.curselection()
    if dlt_task:
        listbox.delete(dlt_task)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def update(new_items):
    listbox.delete(0, tk.END)
    for item in new_items:
        listbox.insert(tk.END, item)

root = tk.Tk()
root.title("To-Do List")
root.configure(bg="light blue")
root.state('zoomed')
font_style=("New Times Roman",32,"bold")
fonts=("New Times Roman",20,"bold")

l1 = tk.Label(root, text="TODO List",font=font_style).place(x=600,y=20)
t1 = tk.Label(root, text="Enter your tasks:",font=fonts).place(x=550,y=100)
e1 = tk.Entry(root,width=40)
e1.place(x=900,y=100)
b1 = tk.Button(root, text="Add Task", command=addt,font=fonts).place(x=450,y=450)
b2 = tk.Button(root, text="Delete Task", command=dlt,font=fonts).place(x=700,y=450)
b3 = tk.Button(root, text="Update Task", command=lambda: update([]),font=fonts).place(x=950,y=450)
listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=30, height=10)
listbox.place(x=650,y=200)

root.mainloop()
