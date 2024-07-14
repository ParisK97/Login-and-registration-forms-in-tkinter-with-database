import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import database
import service_command as sc
import registration_page as rp

root = tk.Tk()

def main() ->None:
    global canvas
    
    root.geometry('925x500+300+200')
    root.resizable(False, False)
    root.configure(bg = '#fff')
    
    canvas = tk.Canvas(root, 
                bg = '#fff', 
                width = 850, 
                height = 450, 
                border = 0, 
                highlightthickness = 0)
    canvas.place(y = 45, x = 50)

    home_labels()
    home_buttons()

    home_entry_boxes()
    home_events()

    root.mainloop()

# home page image
img = ImageTk.PhotoImage(Image.open('login_and_registration_forms/login.jpg'))

def home_labels() ->None:
    label = tk.Label(canvas, image = img, bg = 'white')
    label.place(y = 50, x = 50)

    question = tk.Label(canvas,
                text = "Don't have an account?",
                bg = 'white', 
                fg = 'black',
                font = ('aerial', 10))
    question.place(y = 330, x = 510)

    signin_label = tk.Label(canvas,
                        text = 'Sign in',
                        fg = '#24A0ED',
                        bg = 'white',
                        font =('aerial', 15, 'bold'))
    signin_label.place(y = 120, x = 560)


def home_buttons() ->None:

    sign_in_button = tk.Button(canvas,
                            text = 'Sign in',
                            fg = 'White',
                            bg = '#24A0ED',
                            font = ('aerial', 12, 'bold'), 
                            padx = 120, pady = 5, 
                            highlightthickness = 0, 
                            border = 0,
                            command = lambda: sign_in(database.retrive_data()))
    sign_in_button.place(y = 285, x = 460)

    sign_up_button = tk.Button(canvas, 
                            text = 'Sign up', 
                            fg = '#24A0ED', 
                            bg = 'white', 
                            font = ('aerial', 10), 
                            border = 0, 
                            activebackground = 'white', 
                            activeforeground = 'blue',
                            command = rp.main)
    sign_up_button.place(y = 330, x = 660)


def home_entry_boxes() ->None:
    global username
    global password

    username = tk.Entry(canvas,
                    width = 57,
                    bg = 'white',
                    fg = 'gray',
                    highlightthickness = 0,
                    border = 0)
    username.place(y = 185, x = 435)
    username.insert(0, 'Username')
    canvas.create_line(435, 205, 781, 205, fill = 'black') # line underneth username entry box

    password = tk.Entry(canvas, 
                    width = 57, 
                    bg = 'white', 
                    fg = 'gray', 
                    border = 0, 
                    highlightthickness = 0)
    password.place(y = 238, x = 435)
    password.insert(0, 'Password')
    canvas.create_line(435, 256, 781, 256, fill = 'black') # line underneth password entry box


def on_enter(event) -> None:
    username.delete(0, 'end')

def on_leave(event) -> None:
    if username.get() == '':
        username.insert(0, 'Username')
    

def on_enter_p(event) -> None:
    password.delete(0, 'end')


def on_leave_p(event) -> None:
    if password.get() == '':
        password.insert(0, 'Password')


def home_events() ->None:
    username.bind('<FocusIn>', on_enter)
    username.bind('<FocusOut>', on_leave)

    password.bind('<FocusIn>', on_enter_p)
    password.bind('<FocusOut>', on_leave_p)


def valid_user(data: list):
    data = database.retrive_data()

    for i in data:
        if username.get() and password.get() in i:
            return True
        else:
            return False
    

def sign_in(user_credential) ->None:
    data = valid_user(database.retrive_data())

    if data == True:
        sc.main()
    else:
        messagebox.showerror('Error', 'Invalid username/ password')
    

if __name__ == '__main__':
    main()