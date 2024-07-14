import tkinter as tk
from tkinter import messagebox
import database

def main () -> None:
    global canvas
    root = tk.Tk()

    root.geometry('925x500+300+200')
    root.resizable(False, False)
    root.configure(bg = '#fff')

    # create a anvas and lay over the window
    canvas = tk.Canvas(root, bg = '#fff', width = 922, height = 497, border = 0, highlightthickness = 0)
    canvas.place(x = 0, y = 0)

    labels()
    buttons()
    entry_boxes()
    entry_boxes_data()

    root.mainloop()

def labels () -> None:
    font_0: tuple = ('aerial', 8, 'bold')

    line = canvas.create_line(0, 30, 925, 30, fill = '#d3d3d3')
    line_0 = canvas.create_line(313, 445, 618.5, 445, fill = '#d3d3d3')

    paris_label = tk.Label(canvas, text = 'Paris', font = ('aerial', 10, 'bold'), bg = 'white')
    paris_label.place(x = 10, y = 5)

    account_label = tk.Label(canvas, text = 'Create your account', font = ('aerial', 15, 'bold'), bg = 'white')
    account_label.place(x = 360, y = 80)

    label_2 = tk.Label(canvas,
                    text = 'Create an account to view and manage your profile.',
                    font = ('aerial', 9, 'bold'), bg = 'white', fg = '#d3d3d3')
    label_2.place(x = 315, y = 105)

    username_label = tk.Label(canvas, text = 'Username', font = font_0, bg = 'white')
    username_label.place(x = 310, y = 130)

    email_label = tk.Label(canvas, text = 'Email', font = font_0, bg = 'white')
    email_label.place(x = 310, y = 181)

    name_label = tk.Label(canvas, text = 'Name', font = font_0, bg = 'white')
    name_label.place(x = 310, y = 232)

    password_label = tk.Label(canvas, text = 'Password', font = font_0, bg = 'white')
    password_label.place(x = 310, y = 283)

    confirm_password_label = tk.Label(canvas, text = 'Confirm password', font = font_0, bg = 'white')
    confirm_password_label.place(x = 310, y = 334)
    

def buttons () -> None:
    create_account_button = tk.Button(canvas, 
                                text = 'Create account',
                                fg = 'White', 
                                bg = '#24A0ED', 
                                font = ('aerial', 12, 'bold'),
                                padx = 91, 
                                pady = 3, 
                                highlightthickness = 0, border = 0, command = lambda: create_account(valid_information(entry_boxes_data())))
    create_account_button.place(x = 313, y = 395)

    r = tk.BooleanVar()
    r_button = tk.Radiobutton(canvas,
                        text = "Don't email me about product updates.",
                        variable = r, 
                        value = True, 
                        bg = 'white', activebackground = 'white')
    r_button.place(x = 308, y = 455)

def entry_boxes() -> None:
    global username
    username = tk.Entry(canvas, width = 50, border = 1.5)
    username.place(x = 313, y = 148)

    global email
    email = tk.Entry(canvas, width = 50, border = 1.5)
    email.place(x = 313, y = 200)

    global name
    name = tk.Entry(canvas, width = 50, border = 1.5)
    name.place(x = 313, y = 252)

    global password
    password = tk.Entry(canvas, width = 50, border = 1.5)
    password.place(x = 313, y = 304)

    global confirm_password
    confirm_password = tk.Entry(canvas, width = 50, border = 1.5)
    confirm_password.place(x = 313, y = 356)

def entry_boxes_data()-> tuple[str, str, str, str, str]:
    data = (username.get(), email.get(), name.get(), password.get(), confirm_password.get())

    return data

def valid_information(data: tuple) -> bool:
    data = entry_boxes_data()

    for i in database.retrive_data():
        if username.get() in i:
            messagebox.showerror('Error', 'Username already exists.') # Checking if the provide username already exists
            return False
    if '' in data:
        messagebox.showerror('Error', 'Please complete all fields.') # Checking if all fields are completed
        return False
    if data [-1] != data[-2]:
        messagebox.showerror('Error', "password don't match.")
        return False
    if len(data [-1]) < 8:
        messagebox.showerror('Error', "password must be greater than 8")
        return False

def create_account(valid_user: bool) -> None:
    valid_user = valid_information(entry_boxes_data())
    data = entry_boxes_data()

    if valid_user == None:
        messagebox.showinfo('info', 'Account created. Thank you for signing up.')
        database.insert_data(data)
    else:
        valid_user # this will show the error message

if __name__ == '__main__':
    main()
    



