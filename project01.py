import tkinter as tk
from tkinter import messagebox

#function

def add_task():
    task=entry.get()
    if task!="":

        listbox.insert(tk.END,task)

        entry.delete(0,tk.End)

    else:
        messagebox.showwaring("warning",'task cannot be empty!')

def remove_task():
    try:
        selected=listbox.curselection()[0]
        listbox.delete(selected)
    except IndexError:
        messagebox.showwaring("warning","Please select a task to remove!")
def update_task():
    try:
        selected=listbox.curselection()[0]
        new_task=entry.get()
        if new_task!="":
            listbox.delete(selected)
            listbox.insert(selected, new_task)
            entry.delete(0,tk.END)
        else:
          messagebox.showwaring("Warning","updatedtask cannot be empty!")
    except ImportError:
        messagebox.showwarning("Warning","please select a task to update!")

def exit_app():
     root.destroy()

#GUI Setup
root=tk.Tk()
root.title("To-Do list App")
root.geometry("400x400")
root.config(bg="#f5f5f5")
#input fild

entry=tk.Entry(root,width=30,font=("Arial",14))
entry.pack(pady=10)

#buttons

btn_frame=tk.Frame(root,bg="#f5f5f5")
btn_frame.pack(pady=5)

tk.Button(btn_frame,text="Add Task",width=10,command=add_task).grid(row=0,column = 0,padx=5)

tk.Button(btn_frame,text="remove Task",width=10,command=remove_task).grid(row=0,column=1,padx=5)
tk.Button(btn_frame,text="updatetask",width=10,command = update_task).grid(row=0,column=2,padx=5)

tk.Button(root, text="Exit",width=10,command=exit_app).pack(pady=5)
#task list

listbox =tk.Listbox(root,width=40,height=10,font=("Arial",12))
listbox.pack(pady=10)

root.mainloop()

