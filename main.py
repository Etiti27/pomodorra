from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
repo = 0
canel = None



# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global repo

    repo += 1
    if repo % 8 == 0:
        count_down(math.floor(LONG_BREAK_MIN * 30))
        title.config(text='long break'.upper(), fg=RED)
    elif repo % 2 == 0:
        count_down(math.floor(SHORT_BREAK_MIN * 30))
        title.config(text='short break'.upper(), fg=PINK)
    else:
        count_down(math.floor(WORK_MIN * 30))
        title.config(text='Work time'.upper(), fg=GREEN)
        # is_done.config(text='✓',)
        mark = ""
        session = math.floor(repo/2)
        for _ in range(session):
            mark += "✓"
        is_done.config(text=mark)



def reset():
    window.after_cancel(canel)
    title.config(text='timer'.title(), fg=GREEN)
    canvas.itemconfig(timer_text, text='00:00', fill='white', font=(FONT_NAME, 40, 'bold'))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minutes = math.floor(count / 60)
    count_second = count % 60
    global canel
    if count >= 0:
        canel = window.after(1000, count_down, count - 1)
        if count_second < 10:
            count_second = f'0{count_second}'
        canvas.itemconfig(timer_text, text=f'{count_minutes}:{count_second}')
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('pomodoro')
window.config(padx=20, pady=50, bg=YELLOW)
pomodoro_img = PhotoImage(file='tomato.png')
canvas = Canvas(width=200, height=226, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 90, image=pomodoro_img)
timer_text = canvas.create_text(100, 116, text='00:00', fill='white', font=(FONT_NAME, 40, 'bold'))

title = Label(text='timer'.title(), font=(FONT_NAME, 40, 'normal'), bg=YELLOW, fg=GREEN)

start_button = Button(text='start', fg='#37d3ff', bg=YELLOW, bd=10, highlightbackground=YELLOW, borderwidth=4,
                      command=start_timer)

reset_button = Button(text='reset', fg='#37d3ff', bg=YELLOW, bd=10, highlightbackground=YELLOW, borderwidth=4,
                      command=reset)

is_done = Label(font=(FONT_NAME, 40, 'normal'), bg=YELLOW, fg=GREEN)

canvas.grid(row=2, column=2)
title.grid(row=1, column=2)
start_button.grid(row=3, column=1)
reset_button.grid(row=3, column=3)
is_done.grid(row=4, column=2)
window.mainloop()
