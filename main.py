import math
from tkinter import *

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
marks = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def reset_timer():
    global marks, reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(time_text, text="00:00")
    label_timer.config(text="Timer", fg=GREEN)
    label_timer.place(x=90, y=50)
    marks = ""
    label_item.config(text=marks)


def start_timer():
    global reps
    reps = reps + 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        count_down(work_sec)
        label_timer.config(text="Work", fg=GREEN)
        label_timer.place(x=100, y=50)

    elif reps == 8:
        count_down(long_break_sec)
        label_timer.config(text="Long Break", fg=RED)
        label_timer.place(x=30, y=50)

    elif reps == 2 or reps == 4 or reps == 6:
        count_down(short_break_sec)
        label_timer.config(text="Break", fg=RED)
        label_timer.place(x=90, y=50)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    min = math.floor(count / 60)
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"

    canvas.itemconfig(time_text, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        global marks
        if reps % 2 == 0:
            marks += "✅ "
            label_item.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Tomato Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=300, height=400, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(159, 250, image=img)
time_text = canvas.create_text(160, 260, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(row=0, column=0)

start = Button(text="Start", width=6, command=start_timer)
reset = Button(text="Reset", width=6, command=reset_timer)
start.place(y=350, x=0)
reset.place(y=350, x=260)

label_timer = Label(text="Timer", bg=YELLOW, font=(FONT_NAME, 35, "bold"), fg=GREEN)
label_timer.place(x=90, y=50)

label_item = Label(text="", bg=YELLOW, font=(FONT_NAME, 15, "bold"), fg=GREEN)
label_item.place(x=80, y=380)
window.mainloop()
