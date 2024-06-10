from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Your Dictionary")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

datas = pandas.read_csv("Book1.csv")
learn = datas.to_dict(orient="records")

wrong_words = []
right_word = []

def new_word():
    global current_card
    current_card = random.choice(learn)
    canvas.itemconfig(word_text, text=current_card["English"])
    canvas.itemconfig(word_title, text="Word")

def flip_card():
    canvas.itemconfig(image, image=card_back_img)
    canvas.itemconfig(word_text, text=current_card["Definition"])
    canvas.itemconfig(word_title, text="Definition")
    window.after(5000, switch_to_front)

def switch_to_front():
    canvas.itemconfig(image, image=card_front_img)
    new_word()

def known_word():
    right_word.append(current_card)
    pandas.DataFrame(right_word).to_csv("known_word.csv")
    new_word()

def words_to_learn():
    wrong_words.append(current_card)
    pandas.DataFrame(wrong_words).to_csv("words_to_learn.csv")
    flip_card()

right_button_img = PhotoImage(file="images/right.png")
right_button_button = Button(image=right_button_img, highlightthickness=0, bd=0, command=known_word)
right_button_button.grid(column=1, row=1)

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, bd=0, command=words_to_learn)
wrong_button.grid(column=0, row=1)

star_button = Button(text="Click to Start", command=new_word, bd=0, highlightthickness=0, padx=5, pady=5)
star_button.grid(column=0, row=2, columnspan=2)

canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
image = canvas.create_image(400, 263, image=card_front_img)
word_title = canvas.create_text(400, 100, text="Welcome", font=("Helvetica", 40, "bold"), fill="black", width=600, anchor='n')
word_text = canvas.create_text(400, 300, text="Are You Ready?", font=("Arial", 20, "bold"), fill="black", width=600, anchor='n')
canvas.grid(column=0, row=0, columnspan=2)

window.mainloop()
