from tkinter import *


window = Tk()  # window setup
window.minsize(height=300, width=500)
window.title("password manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=250, width=250)  # bg-image
logo_img = PhotoImage(file="password logo.png")
canvas.create_image(125, 125, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website")  # labels start
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
password_label = Label(text="password")
password_label.grid(row=3, column=0)

window.mainloop()
