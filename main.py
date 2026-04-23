from tkinter import *

window = Tk()
window.minsize(height=300, width=500)
window.title("password manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=250, width=250)
logo_img = PhotoImage(file="password logo.png")
canvas.create_image(125, 125, image=logo_img)
canvas.pack()

window.mainloop()
