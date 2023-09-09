from tkinter import *
from tkinter import messagebox

def CreateTask():
    task = entry.get()
    if task:
        lb.insert(END, task)
        entry.delete(0, END)
    else:
        messagebox.showwarning("WARNING", "Please enter the task.")

def DeleteTask():
    selected_task = lb.curselection()
    if selected_task:
        lb.delete(selected_task)
    else:
        messagebox.showwarning("WARNING", "Please select a task to delete.")

def EditTask():
    selected_task = lb.curselection()
    if selected_task:
        selected_task_index = selected_task[0]
        edited_task = entry.get()
        if edited_task:
            lb.delete(selected_task_index)
            lb.insert(selected_task_index, edited_task)
            entry.delete(0, END)
        else:
            messagebox.showwarning("WARNING", "Please enter the edited task.")
    else:
        messagebox.showwarning("WARNING", "Please select a task to edit.")

root = Tk()
root.geometry("800x650")
root.title("To-Do List")
root.config(bg="#333333")

frame = Frame(root, bg="#333333")
frame.pack()

heading = Label(frame, text="To-Do List", font=("Helvetica", "28"), pady="18", fg="#FFFFFF", bg="#333333")
heading.pack()

lb = Listbox(frame, width="40", height="11", font=("Helvetica", "14"), fg="#333333", bg="#E0E0E0", bd=2)
lb.pack(fill=BOTH, padx=20, pady=(0, 10))

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=Y)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

entry = Entry(root, font=("Helvetica", "16"))
entry.pack(pady=10)

button_frame = Frame(root, bg="#333333")
button_frame.pack(pady=20)

button_style = {"font": ("Helvetica", "15"), "padx": 20, "pady": 10, "bd": 0, "highlightthickness": 0}

AddTask = Button(button_frame, text="Add Task", bg="#59C2AF", fg="#FFFFFF", command=CreateTask, **button_style)
AddTask.pack(fill=BOTH, expand=True, side=LEFT)

EditTask = Button(button_frame, text="Edit Task", bg="#F9A828", fg="#FFFFFF", command=EditTask, **button_style)
EditTask.pack(fill=BOTH, expand=True, side=LEFT)

DelTask = Button(button_frame, text="Delete Task", bg="#E94F37", fg="#FFFFFF", command=DeleteTask, **button_style)
DelTask.pack(fill=BOTH, expand=True, side=LEFT)

Exit = Button(button_frame, text="Exit", bg="#777777", fg="#FFFFFF", command=root.destroy, **button_style)
Exit.pack(fill=BOTH, expand=True, side=LEFT)

root.mainloop()
