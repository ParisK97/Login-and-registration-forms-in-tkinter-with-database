import tkinter as tk

def main() -> None:
    global root
    root = tk.Tk()
    root.geometry('870x500')
    root.resizable(False, False)
    root.configure(bg = '#d3d3d3')

    service_message()
    root.mainloop()


def service_message() -> None:
    label = tk.Label(root,
                text = 'Welcome user',
                bg = '#d3d3d3',
                fg = 'black',
                border = 0,
                highlightthickness = 0,
                font = ('aerial', 20, 'bold')
                )
    label.place(x = 340, y = 220)


if __name__ == '__main__':
    main()
