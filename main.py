import json
from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():


    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '*', '+']

    nr_letters = random.randint(1, 3)
    nr_symbols = random.randint(2, 3)
    nr_numbers = random.randint(2, 3)

    password_letters=[random.choice(letters) for _ in  range(nr_letters)]
    password_symbol=[random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers=[random.choice(numbers) for _ in range(nr_numbers)]

    password_list=password_numbers+password_symbol+password_letters


    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    # for char in password_list:
    #     password += char

    password_entry.insert(0,password)





# ---------------------------- SAVE PASSWORD ------------------------------- #





def add_password():
    global website

    website=web_input.get()
    emaill=email.get()
    passwordd=password_entry.get()
    new_data={
        website:{
            "email":emaill,
            "password":passwordd,
        }
    }



    if len(website)==0 or len(emaill)==0 or len(passwordd) == 0:
        messagebox.showinfo(title="Oops",message="you left some input empty")
    else:
        messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail:{emaill}\nPassword: {passwordd}\n is it ok to save?")
        try:
            with open("data.json","r") as data_file:

                data=json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(data,data_file,indent=4)

        else:
            data.update(new_data)

            with open("data.json","w") as data_file:
                json.dump(data,data_file,indent=4)

        finally:


            web_input.delete(0,END)

            password_entry.delete(0,END)

def find_password():
    website=web_input.get()
    try:
        with open("data.json") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No File Found")
    else:

        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title="web detail",message=f"Email :{email}\n password :{password}\n Is it ok to save?")
        else:
            messagebox.showinfo(title="Error",message="no such file found")


# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password-App")
window.config(padx=50,pady=50,bg="white")

# my_pass=Label(text="My Pass")
# my_pass.grid(column=1,row=0)

canvas=Canvas(width=200,height=200,bg="White")
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,112,image=logo_img)
canvas.grid(column=1,row=1)

web=Label(text="website",bg="white")
web.grid(column=0,row=2)
web_input=Entry(width=35)
web_input.grid(column=1,row=2)
web.focus()
Email_user=Label(text="Email/Username :",bg="white")
Email_user.grid(column=0,row=3)
email=Entry(width=35)
email.grid(column=1,row=3)
# email.insert(0,"yarasfand@gmail.com")
Password=Label(text="Password :",bg="white")
Password.grid(column=0,row=4)
password_entry=Entry(width=30)
password_entry.grid(column=1,row=4)

search=Button(text="Search",command=find_password)
search.grid(column=2,row=2)

generate_button=Button(text="Generate Password",bg="white",command=generate_password)
generate_button.grid(column=2,row=4)

Add_button=Button(text="Add",fg="Black",bg="white",width=36,command=add_password)
Add_button.grid(column=1,row=5,columnspan=2)
window.mainloop()