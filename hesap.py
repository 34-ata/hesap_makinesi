import tkinter as tk
import ctypes
from sympy import sympify

lib = ctypes.CDLL("./hesap.so") #static object dosyamızı dahil ediyoruz.


#burada da fonksiyonlarımızın tanımını ve atamalarını yapıyoruz.
add_func = lib.add
add_func.argtypes = [ctypes.c_double, ctypes.c_double]
add_func.restype = ctypes.c_double

subtract_func = lib.subtract
subtract_func.argtypes = [ctypes.c_double, ctypes.c_double]
subtract_func.restype = ctypes.c_double

multiply_func = lib.multiply
multiply_func.argtypes = [ctypes.c_double, ctypes.c_double]
multiply_func.restype = ctypes.c_double

divide_func = lib.divide
divide_func.argtypes = [ctypes.c_double, ctypes.c_double]
divide_func.restype = ctypes.c_double

window = tk.Tk()
window.title("Calculator with ctypes")
window.geometry("400x200")

current = ""

text_input = tk.Entry(window, width=35, borderwidth=5)
text_input.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(char):
    global current
    current += str(char)
    if char == '=':
        button_equal()
    elif char == 'C':
        button_clear()
    text_input.delete(0, tk.END)
    text_input.insert(0, current)

def button_clear():
    global current
    current = ""
    text_input.delete(0, tk.END)

def button_equal():
    global current
    try:
        parsed_exp = sympify(current.replace('=', "")) #sympify ile sadece ayırmak ile kalmıyoruz işlemleri de yapıyoruz (gayet kullanışlı).
        current = str(parsed_exp)
        text_input.delete(0, tk.END)
        text_input.insert(0, current)
    except:
        current = "ERROR"
        text_input.delete(0, tk.END)
        text_input.insert(0, current)

buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "0", "/", "=", "C"
]
row_value = 1
col_value = 0
for button_text in buttons:
    button = tk.Button(window, text=button_text, command=lambda char=button_text: button_click(char))
    button.grid(row=row_value, column=col_value)
    col_value += 1
    if col_value > 3:
        col_value = 0
        row_value += 1

window.mainloop()