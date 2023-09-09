from tkinter import *

first_number = second_number = operator = None

def get_digit(digit):
    current = result_label["text"]
    new = current + str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text="")

def get_operator(op):
    global first_number, operator
    first_number = int(result_label["text"])
    operator = op
    result_label.config(text="")

def get_result():
    global first_number, second_number, operator
    second_number = int(result_label["text"])

    if operator == "+":
        result_label.config(text=str(first_number + second_number))
    elif operator == "-":
        result_label.config(text=str(first_number - second_number))
    elif operator == "*":
        result_label.config(text=str(first_number * second_number))
    else:
        if second_number == 0:
            result_label.config(text="Error")
        else:
            result_label.config(text=str(round(first_number / second_number, 2)))

root = Tk()

root.title("Calculator")

root.geometry("280x400")
root.resizable(0, 0)
root.configure(background="#363636")  # Updated background color

result_label = Label(root, text="", bg="#363636", fg="#A2FF86")  # Updated font and background colors
result_label.grid(row=0, column=0, columnspan=5, pady=(50, 25), sticky="w")
result_label.config(font=("Times New Roman", 30, "bold"))

buttons = [
    ("7", "#1B6B93", "#A2FF86"),
    ("8", "#1B6B93", "#A2FF86"),
    ("9", "#1B6B93", "#A2FF86"),
    ("+", "#4FC0D0", "#164B60"),
    ("4", "#1B6B93", "#A2FF86"),
    ("5", "#1B6B93", "#A2FF86"),
    ("6", "#1B6B93", "#A2FF86"),
    ("-", "#4FC0D0", "#164B60"),
    ("1", "#1B6B93", "#A2FF86"),
    ("2", "#1B6B93", "#A2FF86"),
    ("3", "#1B6B93", "#A2FF86"),
    ("*", "#4FC0D0", "#164B60"),
    ("C", "#4FC0D0", "#164B60"),
    ("0", "#1B6B93", "#A2FF86"),
    ("=", "#4FC0D0", "#164B60"),
    ("/", "#4FC0D0", "#164B60")
]

row_num = 1
col_num = 0

for text, bg_color, fg_color in buttons:
    button = Button(root, text=text, bg=bg_color, fg=fg_color, width=6, height=2, command=lambda t=text: button_click(t))
    button.grid(row=row_num, column=col_num)
    button.config(font=("Times New Roman", 14))
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

def button_click(text):
    if text.isdigit() or text == ".":
        get_digit(text)
    elif text in ["+", "-", "*", "/"]:
        get_operator(text)
    elif text == "C":
        clear()
    elif text == "=":
        get_result()

root.mainloop()
