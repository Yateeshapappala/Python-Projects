import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.delete(selected_task_index)

root = tk.Tk()
root.title("To-Do List")

tasks_listbox = tk.Listbox(root, height=10, width=50, selectmode=tk.SINGLE)
tasks_listbox.pack(padx=10, pady=10)

entry = tk.Entry(root, width=30)
entry.pack(padx=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

root.mainloop()
