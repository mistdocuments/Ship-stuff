import random
import turtle
import tkinter as tk
import psutil

STARS = {
    "Proxima Centauri": [4.25],
    "Alpha Centauri": [4.36],
    "Barnard's Star": [5.97],
    "Wolf 359": [7.79],
    "Lalande 21185": [8.30],
    "Sirius": [8.61],
    "Luyten 726-8": [8.74],
    "Ross 154": [9.58],
    "Ross 248": [10.3],
    "Epsilon Eridani": [10.4],
    "Lacaille 9352": [10.7],
    "Luyten's Star": [12.2],
    "Procyon": [11.4],
    "61 Cygni A": [11.4],
    "Struve 2398": [11.5],
    "Groombridge 34": [11.6],
}

t = turtle


def move_up():
    t.setheading(90)
    t.forward(5)


def move_down():
    t.setheading(270)
    t.forward(5)


def move_left():
    t.setheading(180)
    t.forward(5)


def move_right():
    t.setheading(0)
    t.forward(5)


current_state = False


def toggle_state():
    global current_state
    if current_state:
        t.down()
    else:
        t.up()
    current_state = not current_state


def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)


def access_battery():
    battery = psutil.sensors_battery()

    print("Battery percentage : ", battery.percent)
    print("Power plugged in : ", battery.power_plugged)

    print("Battery left : ", convertTime(battery.secsleft))


def access_paper():
    win = turtle.Screen()
    

    win.onkey(move_up, "w")
    win.onkey(move_down, "s")
    win.onkey(move_left, "a")
    win.onkey(move_right, "d")
    win.onkey(toggle_state, " ")
    win.listen()
    win.mainloop()


def plot_course():
    for index, dest in enumerate(STARS.keys()):
        print(index + 1, "-", dest)
    shipdest = int(input("Enter index number: ")) - 1
    destname = list(STARS.keys())[shipdest]
    lightyears = STARS[destname][0]
    print(f"{destname} - ({lightyears} Lightyears away) ")


def admin_access():
    admin_window = tk.Tk()
    admin_window.title("Admin Access")
    admin_window.configure(bg="Black")
    admin_window.geometry("100x100")
    admin_window.attributes('-topmost', True)
    admin_window.focus_force()

    battery_button = tk.Button(admin_window, text="Battery",
                               fg="Green", 
                               command=access_battery)

    paper_button = tk.Button(admin_window, text="Paper",
                             fg="Green", 
                             command=access_paper) 

    plot_course_button = tk.Button(admin_window, text="Plot Course",
                                   fg="Green", 
                                   command=plot_course)

    battery_label = tk.Label(admin_window, text="")

    battery_button.pack()
    paper_button.pack()
    plot_course_button.pack()
    battery_label.pack()

    admin_window.mainloop()


def user_access():
    print("Access denied.")


name = input("User: ")

if name == "Admin":
    admin_access()
else:
    user_access()