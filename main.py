import csv
from tkinter import *
from pandas import *
import random
BACKGROUND_COLOR = "#B1DDC6"
# ###########################
try:
    data = read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = read_csv("french_words.csv")
    
to_learn = data.to_dict(orient="records")
current_card = {}
   
def next_card():
    global current_card , flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"] , fill="black")
    canvas.itemconfig(card_background , image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English" , fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill = "white")
    canvas.itemconfig(card_background , image=card_back_img)
    
def is_known():
    to_learn.remove(current_card)
    data = DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)
    next_card()
    

window = Tk()
window.title("Flashcard Project")
window.config(padx=50 ,  pady=50 ,background=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800 , height=526)
card_front_img = PhotoImage(file="card_front.png")
card_back_img = PhotoImage(file="card_back.png")
card_background=canvas.create_image(400,263 ,image=card_front_img)
card_title=canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
card_word=canvas.create_text(400,263,text="",font=("Ariel",68,"bold"))
canvas.config(background=BACKGROUND_COLOR ,highlightthickness=0 ,)

canvas.grid(column=0, row=0,columnspan=2)


cross_image = PhotoImage(file="wrong.png")
unknown_button = Button(image=cross_image , highlightthickness=0, command = next_card)
unknown_button.grid(column=0, row=1 )

right_image = PhotoImage(file="right.png")
known_button = Button(image=right_image,highlightthickness=0, command= is_known)
known_button.grid(column=1, row=1)



next_card()

window.mainloop()