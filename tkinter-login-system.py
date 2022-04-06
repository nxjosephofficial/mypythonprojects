import tkinter as tk

interface = tk.Tk()
interface.title("Program")
interface.geometry("300x200")
a1 = "nxjoseph"
a2 = "12345"

user = tk.Label(text="User:")
user.place(x=10,y=10)

y = tk.StringVar()
user_login = tk.Entry(textvariable=y)
user_login.place(x=45,y=10)

password = tk.Label(text="Password:")
password.place(x=10,y=35)

x = tk.StringVar()
pw_login = tk.Entry(textvariable=x)
pw_login.place(x=75,y=35)

true_false = tk.Label(font="Verdana 30 bold")
true_false.place(x=100,y=95)

def login():
    user = y.get()
    pw = x.get()
    print(user,"\n"+pw)
    if user == a1 and pw == a2:
        print("True")
        true_false.config(text="True",fg="green")
    else:
            print("False")
            true_false.config(text="False",fg="red")


button = tk.Button(text="Log In",command=login)
button.place(x=200,y=60)


interface.mainloop()
