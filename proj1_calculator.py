import tkinter as tk
from tkinter import ttk, messagebox
import requests

# currency logic coden is here
def convert_currency():
    try:
        amount = float(entry.get())
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()
        api_key = "69b2f2730f2c343c1c75c168" 
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
        response = requests.get(url)
        rates = response.json()["conversion_rates"]
        conversion_rate = rates[to_currency]
        converted_amount = amount * conversion_rate
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"{converted_amount:.2f} {to_currency}")
    except Exception as e:
        messagebox.showerror("Error", "Failed to convert currency. Please check your internet connection or input.")
        entry.delete(0, tk.END)

def on_click(text):
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "Convert":
        convert_currency()
    else:
        entry.insert(tk.END, text)

# buttons code 
def create_round_button(root, text, row, col, command=None, color="#7b1fa2"):
    canvas = tk.Canvas(root, width=70, height=70, bg="#2b2b2b", highlightthickness=0)
    canvas.grid(row=row, column=col, padx=1, pady=1)  
   
    oval = canvas.create_oval(5, 5, 65, 65, outline=color, fill=color)
    text_label = canvas.create_text(35, 35, text=text, fill="white", font="Arial 14 bold")
   
    canvas.tag_bind(oval, "<Button-1>", lambda event: command(text))
    canvas.tag_bind(text_label, "<Button-1>", lambda event: command(text))

def create_rect_button(root, text, row, col, command=None, color="#FFA500"):
    button = tk.Button(root, text=text, font="Arial 14 bold", bg=color, fg="white", bd=0, command=lambda: command(text))
    button.grid(row=row, column=col, padx=1, pady=(15, 1), sticky="nsew")

    

# Create the main window
root = tk.Tk()
root.title("Enhanced Calculator with Currency Converter")
root.configure(bg="#2b2b2b")

# output panel code
entry = tk.Entry(root, font="Arial 24", bd=10, insertwidth=2, width=20, borderwidth=4, bg="#1c1c1c", fg="white")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# text for currency 
from_label = tk.Label(root, text="From:", font="Arial 12", bg="#2b2b2b", fg="white")
from_label.grid(row=1, column=0, padx=5, pady=5, sticky='E')

to_label = tk.Label(root, text="To:", font="Arial 12", bg="#2b2b2b", fg="white")
to_label.grid(row=1, column=2, padx=5, pady=5, sticky='E')

# Currency dropdown menus
from_currency_var = tk.StringVar()
to_currency_var = tk.StringVar()
currency_choices = ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD", "PKR", "INR"]  # Added PKR and INR

from_currency_dropdown = ttk.Combobox(root, textvariable=from_currency_var, values=currency_choices, state="readonly", font="Arial 14")
from_currency_dropdown.grid(row=1, column=1, padx=5, pady=5)
from_currency_dropdown.set("USD")  

to_currency_dropdown = ttk.Combobox(root, textvariable=to_currency_var, values=currency_choices, state="readonly", font="Arial 14")
to_currency_dropdown.grid(row=1, column=3, padx=5, pady=5)
to_currency_dropdown.set("PKR")  

# Button layout
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('+', 2, 3, "#FFA500"),  # Orange color
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3, "#FFA500"),  # Orange color
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('*', 4, 3, "#FFA500"),  # Orange color
    ('C', 5, 0, "#FFA500"), ('.', 5, 1, "#FFA500"), ('0', 5, 2), ('/', 5, 3, "#FFA500"),  # Orange color
    ('(', 6, 0, "#FFA500"), (')', 6, 1, "#FFA500"), ('=', 6, 2, "#FFA500"), ('Convert', 6, 3, "#FFA500")  # Orange color
]

# Create buttons and add them to the window
for button in buttons:
    if len(button) == 4:
        text, row, col, color = button
        create_round_button(root, text, row, col, command=on_click, color=color)
    elif len(button) == 3:
        text, row, col = button
        create_round_button(root, text, row, col, command=on_click)

# Adjust the grid size
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(i, weight=1)

# Run the application
root.mainloop()
