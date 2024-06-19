from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
window.title("Flashy")
# window.minsize()

canvas = Canvas(width=800, height=526, highlightthickness=0)
my_image = PhotoImage(file="./images/card_back.png")
canvas.create_image(400, 263, image=my_image)
# second_image = PhotoImage(file="./images/card_front.png")
# canvas.create_image(800, 526, image=second_image)
canvas.grid()


window.mainloop()
