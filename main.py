from tkinter import *


window = Tk()  # window setup
window.minsize(height=300, width=500)
window.title("password manager")
window.config(padx=40, pady=40)
window.resizable(False, False)

canvas = Canvas(height=200, width=200, highlightthickness=0)  # bg-image
logo_img = PhotoImage(file="password logo.png")
logo_img = logo_img.subsample(2, 2)
canvas.create_image(125, 125, image=logo_img)
canvas.grid(column=0, row=0, columnspan=3, pady=(0, 20))

website_label = Label(text="Website:")  # labels start
website_label.grid(row=1, column=0, sticky="e", pady=5)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="e", pady=5)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="e", pady=5)

website_entry = Entry(width=35)  # entries start
website_entry.grid(row=1, column=1, columnspan=2, pady=5, sticky="w")
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, pady=5, sticky="w")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, pady=5, sticky="w")

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2, padx=5, pady=5)
add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2, pady=10)

window.mainloop()
