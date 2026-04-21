import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import psutil
import string
import random
import pyperclip
import shutil 
import os
import json

PATH = None
FILE = 'notes.json'

folders_categories = {
    'Images' : ['.jpeg', '.jpg', '.png', '.gif', '.bmp', '.svg'],
    'Docs' : ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.md'],
    'Videos' : ['.mp4', '.mov', '.avi', '.mkv', '.flv'],
    'Music' : ['.mp3', '.wav', '.acc', '.flac'],
    'Archives' : ['.zip', '.rar', '.tar', '.gz', '.7z'],
    'Programs' : ['.exe', '.msi', '.sh', '.app', '.deb'],
    'Python' : ['.py', '.ipynb']
}


def gen_pass():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    random_string = ''.join(random.choices(characters, k=16))

    password = random_string
    pyperclip.copy(password)
    messagebox.showinfo('Password copied to clipboard.')

def org_files():
    PATH = filedialog.askdirectory()

    if not PATH:
        return

    for file in os.listdir(PATH):
        file_path = os.path.join(PATH, file)

        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(file)
        ext = ext.lower()

        moved = False

        for folder, extensions in folders_categories.items():
            if ext in extensions:
                destination_folder = os.path.join(PATH, folder)

                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)

                shutil.move(file_path, os.path.join(destination_folder, file))
                moved = True
                break

        if not moved:
            others_folder = os.path.join(PATH, "Others")

            if not os.path.exists(others_folder):
                os.makedirs(others_folder)

            shutil.move(file_path, os.path.join(others_folder, file))

    messagebox.showinfo("Done", "Files organized successfully")


def fetch_notes():
    if os.path.exists(FILE) and os.path.getsize(FILE) > 0:
        with open(FILE, 'r') as file:
            return json.load(file)
    return []

notes = fetch_notes()

def save_notes():
    global notes

    new_text = text_area.get("1.0", tk.END).strip()

    if not new_text:
        messagebox.showwarning("Empty", "Note is empty")
        return
    
    new_note = {"note": new_text}
    notes.append(new_note)

    with open(FILE, 'w') as file:
        json.dump(notes, file, indent=4)

    text_area.delete("1.0", tk.END)
    messagebox.showinfo("Saved", "Note saved successfully")
    

root = tk.Tk()
root.title('Developer Productivity Dashboard')
root.geometry('500x500')

top_frame = tk.Frame(root, pady=10)
top_frame.pack()

cpu_label = tk.Label(top_frame, text='CPU:', font=('Arial', 10, 'bold'))
cpu_label.grid(row=0, column=0, padx=5)

cpu_value = tk.Label(top_frame, width=6)
cpu_value.grid(row=0, column=1, padx=5)

ram_label = tk.Label(top_frame, text='RAM:', font=('Arial', 10, 'bold'))
ram_label.grid(row=0, column=2, padx=10)

ram_value = tk.Label(top_frame, width=6)
ram_value.grid(row=0, column=3, padx=5)


def show_cpu():
    CPU = psutil.cpu_percent()
    cpu_value.config(text=f"{CPU}%")
    root.after(2000, show_cpu)

def show_ram():
    RAM = psutil.virtual_memory().percent
    ram_value.config(text=f"{RAM}%")
    root.after(2000, show_ram)

show_cpu()
show_ram()

btn_frame = tk.Frame(root, pady=10)
btn_frame.pack()

gen_pass_btn = tk.Button(btn_frame, text='Generate Password', width=20, command=gen_pass)
gen_pass_btn.grid(row=0, column=0, padx=5, pady=5)

org_files_btn = tk.Button(btn_frame, text='Organize Files', width=20, command=org_files)
org_files_btn.grid(row=0, column=1, padx=5, pady=5)


notes_frame = tk.Frame(root, pady=10)
notes_frame.pack()

notes_label = tk.Label(notes_frame, text='Notes:', font=('Arial', 10, 'bold'))
notes_label.pack(anchor='w')

text_area = tk.Text(notes_frame, height=10, width=50, wrap=tk.WORD)
text_area.pack()

save_btn = tk.Button(notes_frame, text='Save Notes', command=save_notes)
save_btn.pack(pady=5)

root.mainloop()