import tkinter as tk
from tkinter import messagebox
import json
import os

CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save contacts to file
def save_contacts():
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

# Add or update contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    if name:
        contacts[name] = {'Phone': phone, 'Email': email}
        save_contacts()
        refresh_contact_list()
        messagebox.showinfo("Success", f"Contact '{name}' added/updated.")
    else:
        messagebox.showwarning("Input Error", "Name is required.")

# Delete contact
def delete_contact():
    name = name_entry.get()
    if name in contacts:
        del contacts[name]
        save_contacts()
        refresh_contact_list()
        messagebox.showinfo("Deleted", f"Contact '{name}' deleted.")
    else:
        messagebox.showerror("Error", "Contact not found.")

# Display contact info in entry fields
def display_contact(event):
    name = contact_listbox.get(contact_listbox.curselection())
    if name in contacts:
        name_entry.delete(0, tk.END)
        name_entry.insert(0, name)
        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, contacts[name]['Phone'])
        email_entry.delete(0, tk.END)
        email_entry.insert(0, contacts[name]['Email'])

# Refresh the listbox
def refresh_contact_list():
    contact_listbox.delete(0, tk.END)
    for name in contacts:
        contact_listbox.insert(tk.END, name)

# GUI Setup
root = tk.Tk()
root.title("Contact Management System")

contacts = load_contacts()

# Input fields
tk.Label(root, text="Name").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Phone").grid(row=1, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1)

tk.Label(root, text="Email").grid(row=2, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)

# Buttons
tk.Button(root, text="Add / Update", command=add_contact).grid(row=3, column=0)
tk.Button(root, text="Delete", command=delete_contact).grid(row=3, column=1)

# Contact list
tk.Label(root, text="Contacts").grid(row=4, column=0)
contact_listbox = tk.Listbox(root)
contact_listbox.grid(row=5, column=0, columnspan=2)
contact_listbox.bind('<<ListboxSelect>>', display_contact)

refresh_contact_list()
root.mainloop()
