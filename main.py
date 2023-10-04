from tkinter import *
from tkinter import messagebox
from RndPassword import Random_Pass
import json
#import random



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

Generator = Random_Pass()

def Generate_Pass():
    password=Generator.Generate()
    pass_entry.insert(0,password)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #

datas=[]

def getting_data():
    website=web_entry.get()
    mail=user_entry.get()
    password=pass_entry.get()
    
    if website !="" and mail !="" and password!="":
        is_ok=messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {mail}\nPassword: {password}\nIs it okay to save")
        
        if is_ok:
            new_data={
                website: {
                    "email": mail,
                    "password": password
                }
            }
            try:
                with open("datas.json","r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("datas.json","w") as file:
                    json.dump(new_data,file,indent= 4)
            else:
                data.update(new_data)
                
                with open("datas.json","w") as file:
                    json.dump(data, file, indent=4)
            finally:
                web_entry.delete(0,END)
                pass_entry.delete(0,END)
                
            
    else:
        messagebox.showwarning(title="Warning",message="Make sure not to left any field empty!")
        
        
def find_password():
    web_search=web_entry.get()
    try:
        with open("datas.json","r") as file:
            loaded_file=json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="File not found")
    
    try:
        searched_pass=loaded_file[web_search]["password"]
        messagebox.showinfo(title=web_search, message=f"Website: {web_search}\nPassword: {searched_pass}")
    except KeyError:
        messagebox.showinfo(title="Error",message="Website not found")
    

    
    
    
    
        
    

# ---------------------------- UI SETUP ------------------------------- #



window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(height=200,width=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

web_label=Label(text="Website:")
web_label.grid(column=0,row=1)

user_label=Label(text="Email/Username:")
user_label.grid(column=0,row=2)

pass_label=Label(text="Password:")
pass_label.grid(column=0,row=3)

web_entry=Entry(width=21)
web_entry.grid(column=1,row=1,columnspan=2)
web_entry.focus()

web_button=Button(text="search",command=find_password)
web_button.grid(column=2,row=1)

user_entry=Entry(width=35)
user_entry.grid(column=1,row=2,columnspan=2)
user_entry.insert(END,"venox306@gmail.com")

pass_entry=Entry(width=21)
pass_entry.grid(column=1,row=3)

pass_button=Button(text="Generate password",command=Generate_Pass)
pass_button.grid(column=2,row=3)

add_button=Button(text="Add",width=36,command=getting_data)
add_button.grid(column=1,row=4,columnspan=2)

window.mainloop()