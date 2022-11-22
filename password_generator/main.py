from tkinter import *
from tkinter import messagebox
import random
import json
# generate password


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
               'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
               'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    number_of_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    number_of_symbols = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    number_of_numbers = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = number_of_letters + number_of_symbols + number_of_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)


# save data

def save_data():
    web = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {web: {"email": email,
                      "password": password},
                }

    if not web or not email or not password:
        messagebox.askquestion(title="missing info", message="Information must be added.")
    else:
        # messagebox.askyesno(title=web, message=f"These are the details entered: "
        #                                       f"\nEmail: {email} "
        #                                       f"\nPassword: {password} "
        #                                       f"\nIs it ok?")
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)
        finally:
            password_entry.delete(0, END)
            email_entry.delete(0, END)
            web_entry.delete(0, END)

# search function


def search_web_in_data():
    web = web_entry.get()
    try:
        with open("data.json", "r") as f:
            searched_data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="sorry there is no such a database.")
    else:
        if web in searched_data:
            email = searched_data[web]["email"]
            password = searched_data[web]["password"]
            messagebox.showinfo(title="Searched data", message=f"The email for searched web is : {email}" 
                        f"\nThe password for searched web is : {password} ")
        else:
            messagebox.showinfo(title="Searched data", message=f"Sorry, there is no entry with data you have provided.")

# gui

window = Tk()
window.title("Password manager")
window.config(pady=50, padx=50)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_text = Label(text="Website")
website_text.grid(column=0, row=1)
web_entry = Entry(width=16)
web_entry.focus()
web_entry.grid(column=1, row=1)
email_text = Label(text="Email/Username")
email_text.grid(column=0, row=2)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "xxxxxx@yyyy.yyy")
password_text = Label(text="Password")
password_text.grid(column=0, row=3)
password_entry = Entry(width=16)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(width=33, text="Add", command=save_data)
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text="Search", width=16, command=search_web_in_data)
search_button.grid(column=2, row=1)

window.mainloop()
