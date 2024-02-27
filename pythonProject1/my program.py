"""
guess a number between 1-9 (show the solution when not collate
and show the compression when collate)
"""
import colorsys
import turtle


def guess_number():
    import random

    
    print("Number Guessing Game\nguess a number between 1-9")
    x = random.randrange(9)
    while True:
        a = int(input("Your Guess NUNBER: "))
        if a != x:
            if x > a:
                print("try higher NUMBER")
            if x < a:
                print("try lower NUMBER")

            if a == x:
                print("congratulation YOU WON!!!\nrandom number IS: ", x)
                break
        else:
            pass


"""
The Output: "Random Password: ------"
"""


def password_generator():
    import random
    nb = [1, 2, 3, 4, 5, 7, 8, 9, 0]
    rd = random.sample(nb, 6)
    print("Random Password: ", rd)


"""
Rock Paper Scissor GAME
"""


def RPSC_game():
    print("wining rule as follows:\nR VS P -> P win\nR VS SC -> R win\nP VS SC -> SC win\nIf two is the same -> Equal")
    print("Enter choice\n1. Rock\n2. Paper\n3. Scissor")
    rs = "ROCK"
    pr = "PAPER"
    sp = "SCISSOR"

    n, N = "n", "N"
    y, Y = "y", "Y"
    while True:
        import random
        u = int(input("User turn: "))
        if u == 1:
            print("User choice: ", rs)

        elif u == 2:
            print("User choice: ", pr)

        elif u == 3:
            print("User choice: ", sp)

        print("Now is computer turn....")
        cpt = random.randint(1, 3)
        if cpt == 1:
            print("Computer choice: ", rs)
        elif cpt == 2:
            print("Computer choice: ", pr)
        elif cpt == 3:
            print("Computer choice: ", sp)

        if u == cpt:
            print(u, "VS", cpt, "\n<==", u, "=", cpt, "==>", "<==Equal!!==>")
        elif u == 1 and cpt == 2:
            print(rs, "VS", pr, "\n<==", pr, "win", rs, "==>" "<==Computer WIN!!==>")
        elif u == 1 and cpt == 3:
            print(rs, "VS", sp, "\n<==", rs, "win", sp, "==>" "<==User WIN!!==>")
        elif u == 2 and cpt == 3:
            print(pr, "VS", sp, "\n<==", sp, "win", pr, "==>" "<==Computer WIN!!==>")
        elif u == 2 and cpt == 1:
            print(pr, "VS", rs, "\n<==", pr, "win", rs, "==>" "<==User WIN!!==>")
        elif u == 3 and cpt == 1:
            print(sp, "VS", rs, "\n<==", rs, "win", sp, "==>" "<==Computer WIN!!==>")
        elif u == 3 and cpt == 2:
            print(sp, "VS", pr, "\n<==", sp, "win", pr, "==>" "<==User WIN!!==>")
        io = str(input("Do you want to play again? (Y/N)"))
        print(io)
        if io == n or io == N:
            print("Thanks For Playing")
            break
        if io == y or io == Y:
            continue


"""
Hangman Game (guess the word)
"""


def hangman_game():
    print("Guessing Word Game")
    print("* * * * *\nWord have 5 letters\nTotal turn: 6")
    try:
        while True:
            a = [str(input("Enter your guess: "))]
            print(a)
            m, o, u, s, e = ["m", "o", "u", "s", "e"]
            if a == m:
                return

            else:
                print("still 5 turn")

    except FileNotFoundError:
        print("Not Find Your File")


"""
count down program "date time" module (copy in youtube)
"""


def count_down():
    import threading
    import time
    import tkinter as tk
    from win10toast import ToastNotifier
    from playsound import playsound

    class countdown_timer:

        def __init__(self):
            self.root = tk.Tk()
            self.root.geometry("500*400")
            self.root.title("Time Count Down")

            self.time_entry = tk.Entry(self.root, font=('Times New Roman', 40))
            self.time_entry.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

            self.start_button = tk.Button(self.root, font=("Time New Roman", 30), text="Start",
                                          command=self.start_thread)
            self.start_button.grid(row=1, column=0, padx=5, pady=5)

            self.stop_button = tk.Button(self.root, font=("Time New Roman", 30), text="Stop", command=self.stop)
            self.stop_button.grid(row=1, column=0, padx=5, pady=5)

            self.time_label = tk.Label(self.root, font=("Time New Roman", 30), text="time 00:00:00")
            self.time_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

            self.stop_loop = False
            self.root.mainloop()

        def start_thread(self):
            t = threading.Thread(target=self.start)
            t.start()

        def start(self):
            self.stop_loop = False
            hour, minutes, seconds = 0, 0, 0
            string_split = self.time_entry.get().split(":")
            if len(string_split) == 3:
                hour = int(string_split[0])
                minutes = int(string_split[1])
                seconds = int(string_split[2])
            elif len(string_split) == 2:
                minutes = int(string_split[0])
                seconds = int(string_split[1])
            elif len(string_split) == 1:
                seconds = int(string_split[0])
            else:
                print("Invalid time format")
                return

            full_second = hour * 3600 + minutes * 60 + seconds

            while full_second > 0 and not self.stop_loop:
                full_second -= 1
                minutes, seconds = divmod(full_second, 60)
                hour, minutes = divmod(minutes, 60)

                self.time_label.config(text=f"Time: {hour: 02d}: {minutes: 02d}: {seconds}")
                self.root.update()
                time.sleep(1)
            if not self.stop_loop:
                toast = ToastNotifier()
                toast.show_toast("Countdown Timer", "Time is up!", duration=10)

        def stop(self):
            self.stop_loop = True
            self.time_label.config(text="time 00:00:00")


"""
count down program (date time "from you tube")
"""


def new_year_countdown_timer():
    from datetime import timedelta, datetime
    import time

    print("\n=> NEW YEAR COUNTDOWN TIMER <= ")
    print("Exit By: CTRL + C\n")

    try:
        while True:
            datetime_now = datetime.today()
            datetime_now_tst = int(datetime_now.timestamp())
            new_year_datetime = datetime(year=datetime_now.year + 1, month=1, day=1, hour=0, minute=0, second=0)
            new_year_datetime_tst = int(new_year_datetime.timestamp())
            remaining_time_seconds = new_year_datetime_tst - datetime_now_tst

            remaining_time = timedelta(seconds=remaining_time_seconds)
            remaining_days = remaining_time.days
            remaining_second = remaining_time.seconds

            remaining_minute, remaining_second = divmod(remaining_second, 60)
            remaining_hour, remaining_minute = divmod(remaining_minute, 60)

            if remaining_days:
                if remaining_days > 1:
                    remaining_days = '{} day'.format(remaining_days)
                else:
                    remaining_days = '{} day'.format(remaining_days)
            else:
                remaining_days = ''

            if remaining_hour:
                if remaining_hour > 1:
                    remaining_hour = ', {} hour'.format(remaining_hour)
                else:
                    remaining_hour = ', {} hour'.format(remaining_hour)
            else:
                remaining_hour = ''

            if remaining_minute:
                if remaining_minute > 1:
                    remaining_minute = ', {} minute'.format(remaining_minute)
                else:
                    remaining_minute = ', {} minute'.format(remaining_minute)
            else:
                remaining_minute = ''

            if remaining_second:
                if remaining_second > 1:
                    remaining_second = ', {} minute'.format(remaining_second)
                else:
                    remaining_second = ', {} minute'.format(remaining_second)
            else:
                remaining_second = ''

            space = '                                             '
            print('\rTime Remaining: {}{}{}{}'.format(remaining_days,
                                                      remaining_hour,
                                                      remaining_minute,
                                                      remaining_second,
                                                      space), end='')
            time.sleep(0.5)

    except KeyboardInterrupt:
        exit()

"""
turtle in python 'copy code from youtub
"""
# from turtle import *
#
# bgcolor('black')
# speed(0)
# hideturtle()
# for i in range(120):
#     color('red')
#     circle(i*0.8)
#     right(3)
#     forward(3)
#
# done()


"""

"""


