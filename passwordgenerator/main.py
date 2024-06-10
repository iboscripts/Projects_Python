from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

window = Tk()
window.minsize(width=600, height=600)
window.title("Password Manager")
window.config(padx=20, pady=20)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def cleaner():
    website_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()


def saving_information():
    website_info = website_entry.get()
    username_info = username_entry.get()
    password_info = password_entry.get()

    new_dict = {
        website_info: {
            "email": username_info,
            "password": password_info,
        }
    }

    if len(website_info) == 0 or len(username_info) == 0 or len(password_info) == 0:
        messagebox.askretrycancel(website_info, "something is missing, please fill in all fields")
    else:
        try:
            with open("information.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("information.json", "w") as file:
                json.dump(new_dict, file, indent=4)
        else:
            data.update(new_dict)
            with open("information.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            cleaner()


def find_password():
    try:
        with open("information.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="website", message="No data file found")
    else:
        entry = website_entry.get()
        if entry in data:
            email = data[entry]["email"]
            password = data[entry]["password"]
            messagebox.showinfo(title="Website", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="website", message="website cannot be found")


canvas = Canvas(width=200, height=350, highlightthickness=0)
img = PhotoImage(file="lock1.png")
canvas.create_image(100, 180, image=img)
canvas.grid(column=1, row=0, columnspan=2)

website = Label(text="Website: ")
username = Label(text="Email/Username: ")
password = Label(text="Password: ")
website_entry = Entry(width=22)
username_entry = Entry(width=40)
password_entry = Entry(width=22)
password_generator_button = Button(text="Generate Password", command=password_generator)
add_button = Button(text="Add", width=13, command=saving_information)
search_button = Button(text="Search", width=13, command=find_password)

website.grid(column=0, row=1)
username.grid(column=0, row=2)
password.grid(column=0, row=3)
website_entry.grid(column=1, row=1)
username_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)
password_generator_button.grid(column=2, row=3)
add_button.grid(column=2, row=4)
search_button.grid(column=2, row=1)

website_entry.focus()
# username_entry.insert(0, "furkan_cinko23@hotmail.com")

window.mainloop()
