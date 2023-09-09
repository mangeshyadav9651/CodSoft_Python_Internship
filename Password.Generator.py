import string
import random
import tkinter as tk

characters = string.ascii_letters + string.digits + string.punctuation

def generate_password():
    password_length = int(length_entry.get())
    password = ''.join(random.choice(characters) for _ in range(password_length))
    generated_password_entry.config(state="normal")
    generated_password_entry.delete(0, tk.END)
    generated_password_entry.insert(0, password)
    generated_password_entry.config(state="readonly")

def reset_password():
    generated_password_entry.config(state="normal")
    generated_password_entry.delete(0, tk.END)
    generated_password_entry.config(state="readonly")

def accept_password():
    root.destroy()

root = tk.Tk()
root.geometry("800x700")
root.title("Password Generator")

canvas = tk.Canvas(root, width=800, height=700, bg="#1A1A1A")  # Updated background color
canvas.create_text(400, 70, text="Password Generator", fill="#FFD700", font=("Bold", 40))  # Updated font color

canvas.create_rectangle(80, 120, 700, 450, fill="#353535")  # Updated background color

labels = [
    ("Enter Username:", 220),
    ("Password Length:", 280),
    ("Generated Password:", 370)
]

entries = {}

for i, (label_text, y_pos) in enumerate(labels):
    label = tk.Label(canvas, text=label_text, font=("Times New Roman", 15), bg="#353535", fg="#FFD700")  # Updated font and background colors
    label.place(x=120, y=y_pos)
    entry = tk.Entry(canvas, font=("Times New Roman", 15), width=33, border=3)
    entry.place(x=300, y=y_pos)
    entries[f'entry{i+1}'] = entry

length_entry = entries['entry2']
generated_password_entry = entries['entry3']
generated_password_entry.config(state="readonly")

buttons = [
    ("Generate", generate_password),
    ("Accept", accept_password),
    ("Reset", reset_password)
]

for i, (button_text, command) in enumerate(buttons):
    button = tk.Button(canvas, text=button_text, height=2 if i == 0 else 1, width=10,
                       bg="#FFD700", fg="#1A1A1A", font=("Times New Roman", 15), borderwidth=3, command=command)  # Updated font and background colors
    button.place(x=150 + i * 150, y=500 if i == 0 else 510)

canvas.pack()

root.mainloop()
