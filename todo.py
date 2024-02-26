import tkinter as tk
from tkinter import ttk, messagebox
import json

# Encryption and decryption functions
def encrypt(data, key):
    encrypted = bytearray(data.encode())
    for i in range(len(encrypted)):
        encrypted[i] ^= key
    return encrypted.decode()

def decrypt(data, key):
    decrypted = bytearray(data.encode())
    for i in range(len(decrypted)):
        decrypted[i] ^= key
    return decrypted.decode()

# Functions for data persistence
def save_tasks(tasks, key):
    # Encrypt tasks data and write to file
    encrypted_tasks = encrypt(json.dumps(tasks), key)
    with open('tasks.json', 'w') as file:
        file.write(encrypted_tasks)

def load_tasks(key):
    try:
        # Read encrypted tasks data from file and decrypt
        with open('tasks.json', 'r') as file:
            encrypted_tasks = file.read()
            decrypted_tasks = decrypt(encrypted_tasks, key)
            return json.loads(decrypted_tasks)
    except FileNotFoundError:
        return []

# Function to add a task to the list
def add_task():
    task = task_entry.get()
    if task:
        # Insert task into listbox and save tasks
        task_listbox.insert(tk.END, task)
        tasks.append(task)
        save_tasks(tasks, encryption_key)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to remove the selected task from the list
def remove_task():
    try:
        # Remove selected task from listbox and save tasks
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
        del tasks[selected_index]
        save_tasks(tasks, encryption_key)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Application title
app_title = "Dardino's Amazing Todo App!"

# Encryption key
encryption_key = 42

# Create the root window
root = tk.Tk()
root.title(app_title)
root.resizable(False, False)

# Create a container frame
container_frame = tk.Frame(root, padx=30, pady=30)
container_frame.pack(fill=tk.BOTH, expand=True)

# Application heading
app_heading = tk.Label(container_frame, text=app_title, font=("Arial", 16, "bold"))
app_heading.pack(pady=(0, 20))

# Entry widget for adding tasks
task_entry = ttk.Entry(container_frame, style='Pad.TEntry')
task_entry.pack(pady=(0, 10), fill=tk.BOTH)
task_entry.focus_set()

# Button to add tasks
add_button = tk.Button(container_frame, text="Add Task", width=30, command=add_task)
add_button.pack()

# Listbox to display tasks
task_listbox = tk.Listbox(container_frame)
task_listbox.pack(pady=10, fill=tk.BOTH)

# Button to remove selected task
remove_button = tk.Button(container_frame, text="Remove Selected Task", width=30, command=remove_task)
remove_button.pack()

# Load tasks from file on startup
tasks = load_tasks(encryption_key)
for task in tasks:
    task_listbox.insert(tk.END, task)

# Function to handle keyboard events
def handle_enter(event):
    if event.widget in (task_entry, add_button):
        add_task()
    elif event.widget == remove_button:
        remove_task()

# Bind Enter key to add_task function and Control+Q to quit the application
root.bind("<Return>", handle_enter)
root.bind("<Control-q>", lambda event: root.destroy())

# Function to center the window on the screen
def center_window(window):
    screen_width, screen_height = window.winfo_screenwidth(), window.winfo_screenheight()
    window_width, window_height = window.winfo_reqwidth(), window.winfo_reqheight()
    x_coord = (screen_width - window_width) // 2
    y_coord = (screen_height - window_height) // 2
    window.geometry(f"+{x_coord}+{y_coord}")

# Center the root window
center_window(root)

# Set the application icon
root.iconbitmap("favicon.ico")

# Start the Tkinter event loop
root.mainloop()