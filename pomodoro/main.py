from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
my_timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(my_timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    tick.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Break")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="Break")
    else:
        count_down(work_sec)
        timer.config(text="Work")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    caount_sec = count % 60
    if caount_sec == 0:
        caount_sec == "00"
    canvas.itemconfig(timer_text, text=f"{count_min}:{caount_sec}")
    if count > 0:
        global my_timer
        my_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        tick.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=GREEN)


timer = Label(text="Timer", bg=GREEN, font=(FONT_NAME, 20, "bold"))
start_button = Button(text="START", fg=GREEN, bg=GREEN,
                      highlightbackground=GREEN, command=start_timer)
reset_button = Button(text="RESET", fg=GREEN, bg=GREEN,
                      highlightbackground=GREEN, command=reset_timer)
tick = Label(bg=GREEN, font=(FONT_NAME, 20, "bold"))


canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(column=2, row=2)
timer.grid(column=2, row=1)
start_button.grid(column=1, row=3)
reset_button.grid(column=3, row=3)
tick.grid(column=2, row=4)


window.mainloop()