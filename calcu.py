import tkinter as tk
import math

def press(key):
    entry.insert(tk.END, key)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expr = entry.get()
        result = eval(expr)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Scientific functions
def sin():
    entry.insert(tk.END, "math.sin(")

def cos():
    entry.insert(tk.END, "math.cos(")

def tan():
    entry.insert(tk.END, "math.tan(")

def log():
    entry.insert(tk.END, "math.log10(")

def ln():
    entry.insert(tk.END, "math.log(")

def sqrt():
    entry.insert(tk.END, "math.sqrt(")

def pi():
    entry.insert(tk.END, "math.pi")

def power2():
    entry.insert(tk.END, "**2")

# Window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("420x500")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entry.pack(fill="both", padx=10, pady=10)

frame = tk.Frame(root)
frame.pack()

buttons = [
    ("7", lambda: press("7")), ("8", lambda: press("8")), ("9", lambda: press("9")), ("/", lambda: press("/")), ("sin", sin),
    ("4", lambda: press("4")), ("5", lambda: press("5")), ("6", lambda: press("6")), ("*", lambda: press("*")), ("cos", cos),
    ("1", lambda: press("1")), ("2", lambda: press("2")), ("3", lambda: press("3")), ("-", lambda: press("-")), ("tan", tan),
    ("0", lambda: press("0")), (".", lambda: press(".")), ("=", calculate), ("+", lambda: press("+")), ("√", sqrt),
    ("(", lambda: press("(")), (")", lambda: press(")")), ("log", log), ("ln", ln), ("π", pi),
    ("x²", power2), ("C", clear)
]

row = 0
col = 0

for text, cmd in buttons:
    tk.Button(frame, text=text, width=6, height=2, font=("Arial", 14),
              command=cmd).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 4:
        col = 0
        row += 1

root.mainloop()