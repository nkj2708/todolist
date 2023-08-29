import tkinter as tk
from tkinter import messagebox

#Function to create a new task
def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("You cannot enter empty task!")

#Fuction to remove a selected task
def remove_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        task_list.delete(selected_task_index)

#Function to clear all tasks
def clear_tasks():
    task_list.delete(0, tk.END)

#Function to save all tasks
def save_tasks():
    tasks = task_list.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

#Function to load the saved tasks
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                task_list.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

# Creating and configuring the main window
root = tk.Tk()
root.title("To-Do List")
root.configure(bg='blue')
root.geometry("500x700")

# Creating and placing the widgets

task_entry = tk.Entry(root, width=20, font=("Arial",15))
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task",font=("Arial",10),bg="orange", command=add_task)
add_button.pack(pady=10)

remove_button = tk.Button(root, text="Remove Task",font=("Arial",10),bg="orange", command=remove_task)
remove_button.pack(pady=10)

clear_button = tk.Button(root, text="Clear All",font=("Arial",10),bg="orange", command=clear_tasks)
clear_button.pack(pady=10)

save_button = tk.Button(root, text="Save Tasks",font=("Arial",10),bg="orange", command=save_tasks)
save_button.pack(pady=10)

load_button = tk.Button(root, text="Load Tasks",font=("Arial",10),bg="orange", command=load_tasks)
load_button.pack(pady=10)

task_list = tk.Listbox(root, width=40)
task_list.pack(pady=10)

# Load saved previous tasks when the program starts
load_tasks()

root.mainloop()
