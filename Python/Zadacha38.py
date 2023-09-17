import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3

# Подключаемся к базе данных (или создаем новую)
conn = sqlite3.connect('contacts.db')
cursor = conn.cursor()

# Создаем таблицу для контактов, если она еще не создана
cursor.execute('''
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT NOT NULL
);
''')
conn.commit()


def add_contact(name, phone):
    cursor.execute("INSERT INTO contacts (name, phone) VALUES (?, ?)", (name, phone))
    conn.commit()


def search_contact(name):
    cursor.execute("SELECT * FROM contacts WHERE name=?", (name,))
    return cursor.fetchone()


def delete_contact(name):
    cursor.execute("DELETE FROM contacts WHERE name=?", (name,))
    conn.commit()


def update_contact(name, new_name, new_phone):
    cursor.execute("UPDATE contacts SET name=?, phone=? WHERE name=?", (new_name, new_phone, name))
    conn.commit()


def show_all_contacts():
    cursor.execute("SELECT * FROM contacts")
    return cursor.fetchall()


def on_add():
    name = simpledialog.askstring("Add Contact", "Enter name:")
    phone = simpledialog.askstring("Add Contact", "Enter phone:")
    add_contact(name, phone)


def on_search():
    name = simpledialog.askstring("Search Contact", "Enter name to search:")
    contact = search_contact(name)
    if contact:
        messagebox.showinfo("Contact Found", f"Name: {contact[1]}, Phone: {contact[2]}")
    else:
        messagebox.showwarning("Not Found", "Contact not found!")


def on_delete():
    name = simpledialog.askstring("Delete Contact", "Enter name to delete:")
    delete_contact(name)


def on_update():
    name = simpledialog.askstring("Update Contact", "Enter name to update:")
    contact = search_contact(name)
    if contact:
        new_name = simpledialog.askstring("Update Contact", "Enter new name:", initialvalue=contact[1])
        new_phone = simpledialog.askstring("Update Contact", "Enter new phone:", initialvalue=contact[2])
        update_contact(name, new_name, new_phone)
    else:
        messagebox.showwarning("Not Found", "Contact not found!")


def on_show_all():
    contacts = show_all_contacts()
    contacts_str = "\n".join([f"{contact[1]}: {contact[2]}" for contact in contacts])
    messagebox.showinfo("All Contacts", contacts_str)


# Главное окно приложения
root = tk.Tk()
root.title("Телефонная книга")

btn_add = tk.Button(root, text="Добавить контакт", command=on_add)
btn_add.pack(pady=10)

btn_search = tk.Button(root, text="Поиск контакта", command=on_search)
btn_search.pack(pady=10)

btn_delete = tk.Button(root, text="Удалить контакт", command=on_delete)
btn_delete.pack(pady=10)

btn_update = tk.Button(root, text="Обновить контакт", command=on_update)
btn_update.pack(pady=10)

btn_show_all = tk.Button(root, text="Показать все контакты", command=on_show_all)
btn_show_all.pack(pady=10)

root.mainloop()

# Закрыть соединение с БД при выходе
conn.close()
