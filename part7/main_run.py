from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

ALPHABET = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
SYMBOLS = ('!','!','$','%','&','(' ')','*','+','-','.','/')
NUMBERS = ("0","1","2","3","4","5","6","7","8","9")

def main():
  # ---------------------------- PASSWORD SEARCH ON FILE BASED WEBSITE THAT ON FILE WITH PASSWORDS.TXT ------------------------------- #
  def search():
    website = website_entry.get()

    try:
      with open('part7/passwords.json', 'r') as f:
        data = json.load(f)
    except FileNotFoundError:
      messagebox.showerror(title="Error", message="File not found")
    else:
      if website in data:
        email = data['email']
        password = data['password']
        messagebox.showinfo(title=website, message=f"Email/Username: {email}\nPassword: {password}")
      else:
        messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
  
  # ---------------------------- PASSWORD GENERATOR ------------------------------- #

  # Generates a random password
  def generate_password():
    # Generates random letters
    password_letters = [random.choice(ALPHABET) for _ in range(random.randint(8,10))]

    # Generates random symbols
    password_symbols = [random.choice(SYMBOLS) for _ in range(random.randint(2,4))]
    
    # Generates random numbers
    password_numbers = [random.choice(NUMBERS) for _ in range(random.randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

  # ---------------------------- SAVE PASSWORD ------------------------------- #

  def save():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    """ To acopolate same website with different data we need to do:
    new_data = {
    website: {
      "website_name": website,
      'email': email, 
      'password': password
    } change the add/update and in the search as well
    1. let's say data.json file exist but we have deleted all entries inside that file. now when we try to add new entries it will show json.decoder.JSONDecodeError 
2. same json.decoder.JSONDecodeError  error will appear when data.json file exist and user hit search button without writing anything inside the website_entry box."""
    new_data = {
      website: 
      {'email': email, 
       'password': password
      }
    }

    if website != '' and email != '' and password != '':
      try:
        with open('part7/passwords.json', 'r') as f:
          data = json.load(f)
      except FileNotFoundError:
        #creating new file
        with open('part7/passwords.json', 'w') as f:
          json.dump(new_data, f, indent=4)
      else:
        #updating old data with new data
        data.update(new_data)
        with open('part7/passwords.json', 'w') as f:
          #savind updated data
          json.dump(data, f, indent=4)
      finally:
        messagebox.showinfo(title="Password Saved", message=f"Password Saved Successfully\nWebsite: {website}\nEmail: {email}\nPassword: {password}")
        website_entry.delete(0,END)
        password_entry.delete(0,END)
      
    else:
      messagebox.showerror(title='Error', message='Please fill out all the fields')


  # ---------------------------- UI SETUP ------------------------------- #

  window = Tk()
  window.title("Password Manager")
  window.config(padx=50, pady=50, bg="white")

  canvas = Canvas(height=200, width=200, bg="white", highlightthickness=0)
  logo_img = PhotoImage(file="part7/logo.png")
  canvas.create_image(100,100, image=logo_img)
  canvas.grid(row=0, column=1)

  #Labels
  website_label = Label(text="Website:", bg="white")
  website_label.grid(row=1,column=0)

  email_username_label = Label(text="Email/Username:", bg="white")
  email_username_label.grid(row=2,column=0)

  password_label = Label(text="Password:", bg="white")
  password_label.grid(row=3,column=0)

  #Entries
  website_entry = Entry(width=21, highlightthickness=0)
  website_entry.grid(row=1,column=1, sticky='w')
  website_entry.focus()

  email_username_entry = Entry(width=35, highlightthickness=0)
  email_username_entry.grid(row=2,column=1, columnspan=2, sticky="w")
  email_username_entry.insert(0, 'dario@email.com')

  password_entry = Entry(width=21, highlightthickness=0)
  password_entry.grid(row=3,column=1, sticky="w")

  #Buttons
  generate_password_button = Button(text="Generate Password", command=generate_password, bg="white")
  generate_password_button.grid(row=3,column=2, sticky="w")

  add_button = Button(text="Add", command=save, width=36, bg="white")
  add_button.grid(row=4,column=1, columnspan=2, sticky="w")

  search_button = Button(text="Search", command=search, bg='white')
  search_button.grid(row=1,column=2, sticky="w")

  window.mainloop()