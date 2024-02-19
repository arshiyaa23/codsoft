import tkinter as tk
from tkinter import messagebox

def calculate():
    try:     
        num1 = float(enum1.get())
        num2 = float(enum2.get())
        operation = var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero"
        else:
            result = "Invalid operation"

        result_text.delete(1.0, tk.END) 
        result_text.insert(tk.END, f"Result: {result}")
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter valid numeric input.")


root = tk.Tk()
root.title("Basic Calculator")
root.configure(bg="black")
root.state('zoomed')
font_style=("New Times Roman",32,"bold")
fonts=("New Times Roman",20,"bold")


enum1 = tk.Entry(root, width=10)
enum2 = tk.Entry(root, width=10)
l1=tk.Label(root,text="Calculator",font =font_style)
l2= tk.Label(root, text="Enter two numbers:",font=fonts)
label = tk.Label(root, text="Choose Operation:",font=fonts)
var = tk.StringVar(root)
var.set('+')
dropdown = tk.OptionMenu(root,var, '+', '-', '*', '/','%')


calculate_button = tk.Button(root, text="Calculate",font=fonts, command=calculate)


rlabel = tk.Label(root, text="Result: ",font=fonts)

result_text = tk.Text(root, height=1, width=20)
l1.place(x=600,y=20)
l2.place(x=550,y=100)
enum1.place(x=900,y=100)
label.place(x=550,y=200)
enum2.place(x=1000,y=100)
dropdown.place(x=900,y=200)
calculate_button.place(x=700,y=300)
rlabel.place(x=550,y=400)
result_text.place(x=900,y=400)

root.mainloop()
