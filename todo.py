import tkinter as tk
from tkinter import ttk, messagebox

# Function to add a task to the list
def add_task():
    task = task_entry.get()
    if task:
        # Insert the task into the listbox
        task_listbox.insert(tk.END, task)
        # Clear the task entry
        task_entry.delete(0, tk.END)
    else:
        # Show a warning if the task entry is empty
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to remove the selected task from the list
def remove_task():
    try:
        # Get the index of the selected task
        selected_index = task_listbox.curselection()[0]
        # Delete the selected task from the listbox
        task_listbox.delete(selected_index)
    except IndexError:
        # Show a warning if no task is selected
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Application title
app_title = "Dardino's Amazing Todo App!"

# Create the root window
root = tk.Tk()
root.title(app_title)
root.resizable(False, False)

# Padding for the frame
frame_padding = 30

# Create a container frame
container_frame = tk.Frame(root, padx=frame_padding, pady=frame_padding)
container_frame.pack(fill=tk.BOTH, expand=True)

# Application heading
app_heading = tk.Label(container_frame, text=app_title, font=("Arial", 16, "bold"))
app_heading.pack(pady=(0, 20))

# Configure custom styling for entry widget
style = ttk.Style()
style.configure('Pad.TEntry', padding='8 8 8 8', bordercolor="red")

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
    # Calculate coordinates to center the window
    x_coord = (screen_width - window_width) // 2
    y_coord = (screen_height - window_height) // 2
    # Set window position
    window.geometry(f"+{x_coord}+{y_coord}")

# Center the root window
center_window(root)

# Set the application icon
root.iconbitmap("favicon.ico")

# Start the Tkinter event loop
root.mainloop()