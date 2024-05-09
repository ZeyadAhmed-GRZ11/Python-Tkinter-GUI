import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo



def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        showinfo(title='Information', message=','.join(record))

def add_entry():
    Name = name_entry.get()
    Age = age_entry.get()
    Email = email_entry.get()
    if Name and Age and Email:
        tree.insert('', 'end', values=(Name, Age, Email))
        name_entry.delete(0, 'end')
        age_entry.delete(0, 'end')
        email_entry.delete(0, 'end')

def delete_entry():
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item)

def reset_data():
    tree.delete(*tree.get_children())

root = tk.Tk()
root.title("Insert Data")

tree = ttk.Treeview(root, columns=('Name','Age','Email'),show="headings", height=20)
tree.heading('Name', text='Name')
tree.heading('Age', text='Age')
tree.heading('Email', text='Email')
tree.bind('<<TreeviewSelect>>', item_selected)     
tree.pack()

Labels = Label(root, text="Name:")
Labels.pack()
name_entry = tk.Entry(root)
name_entry.pack()

Labels = Label(root, text="Age:")
Labels.pack()
age_entry = tk.Entry(root)
age_entry.pack()

Labels = Label(root, text="Email:")
Labels.pack()
email_entry = tk.Entry(root)
email_entry.pack()

add_button = tk.Button(root, text='Add Entry', command=add_entry)
add_button.pack()

delete_button = tk.Button(root, text='Delete Selected', command=delete_entry)
delete_button.pack()

reset_button = tk.Button(root, text='Reset Data', command=reset_data)
reset_button.pack()   

Scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=Scrollbar.set)


root.mainloop()