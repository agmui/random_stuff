#!/usr/bin/env python3
#import desktop_file
import os
import pygame
from datetime import datetime
from tkinter import *
import playsound
import threading
import calculate_time
from PIL import Image, ImageTk
import time

hour, minute, ampm = "0", "0", 0
width, height = 600, 450  # tkinter window
stop, kill, flip = False, False, False
count, count2 = 10000, 100000
sound1 = os.path.join("assets_and_sounds", "sempai.mp3")
sound2 = os.path.join("assets_and_sounds", "sempai_2.mp3")
schedule = pygame.image.load(os.path.join("assets_and_sounds", "schedule.png"))


def text(hour, minute, sec):
    font = pygame.font.SysFont(None, 40)
    img = font.render(str(hour) + ":" + str(minute) + ":" + str(sec), True, (255, 255, 255))
    GD.blit(img, (2048 / 2, 1080 / 2 + 50))


def timer(hour, minute, sec):
    global stop
    font = pygame.font.SysFont(None, 70)
    if hour == 0:
        img = font.render(str(minute) + ":" + str(sec), True, (255, 255, 255))
        if minute == 0:
            img = font.render(str(sec), True, (255, 255, 255))
            if sec == 0:
                img = font.render(str(sec), True, (255, 255, 255))
                stop = True
    elif stop:
        img = font.render("0", True, (255, 255, 255))
    else:
        img = font.render(str(hour) + ":" + str(minute) + ":" + str(sec), True, (255, 255, 255))

    GD.blit(img, (2048 / 2, 1080 / 2))


def play_sound():
    playsound.playsound(sound1, True)
    playsound.playsound(sound2, True)


def flash_screen(flip_):
    # time.sleep(0.5)
    if flip_:
        pygame.draw.rect(GD, (100, 100, 100), (0, 0, 2048, 1080))
    else:
        pygame.draw.rect(GD, (255, 0, 0), (0, 0, 2048, 1080))


def quit_button(x, y, width, hight):
    pygame.draw.rect(GD, (0, 0, 0), (x, y, width, hight), 7)
    pygame.draw.rect(GD, (255, 0, 0), (x, y, width, hight))
    mouse_x, mouse_y = pygame.mouse.get_pos()
    press, _, _ = pygame.mouse.get_pressed()
    if x + width > mouse_x > x and y + hight > mouse_y > y:
        pygame.draw.rect(GD, (255, 100, 100), (x, y, width, hight))
        if press == 1:
            return True
        else:
            return False


def display():
    now = datetime.now()
    H, M, S = now.strftime("%H"), now.strftime("%M"), now.strftime("%S")
    if int(H) > 12:
        H = int(H) - 12
    elif int(H) == 0:
        H = 12



    h, m, s = calculate_time.calcutate(ampm, hour, minute)
    #h, m, s = 0, 0, 0  # ts
    if int(H) > 12 and int(M) > 5:
        h = 12
        m = 40
    elif int(H) > 10 and int(M) > 20:
        h = 10
        m = 45
    timer(h, m, s)
    text(H, M, S)


class window:
    def __init__(self):
        self.kill = False
        self.load = Image.open("assets_and_sounds/schedule.png")
        self.img = ImageTk.PhotoImage(self.load)  # os.path.join("assets_and_sounds", "schedule.png"))

    def click(self, textentry_hour, textentry_minute):
        global hour, minute
        hour = textentry_hour
        minute = textentry_minute
        try:
            int(hour)
        except:
            hour = "0"
        try:
            int(minute)
        except:
            minute = "0"

        if ampm == 0:
            Label(root, text="Input AM or PM", bg="gray", fg="white", font="none 12 bold").place(x=150, y=50)
        else:
            root.destroy()

    def kill_(self):
        global kill
        kill = True
        self.kill = True
        root.destroy()

    def button_Click(self, val):
        global ampm
        ampm = val

    def create_Window(self):
        root.geometry(str(width) + "x" + str(height))

    def labels(self):
        Label(root, text="Input next class time: ", bg="gray", fg="white", font="none 26 bold").place(x=5, y=0)
        Label(root, text=":", bg="gray", fg="white", font="none 12 bold").place(x=100, y=47)
        Label(root, image=self.img).place(x=20, y=170)

    def inputs(self):
        click = window()
        textentry_hour = Entry(root, width=5, bg="gray")
        textentry_hour.place(x=60, y=50)
        textentry_minute = Entry(root, width=5, bg="gray")
        textentry_minute.place(x=120, y=50)
        ampm = IntVar()
        Radiobutton(root, activebackground="gray", activeforeground="white", text="AM", variable=ampm,
                    selectcolor="gray", value=1, command=lambda: click.button_Click(ampm.get()), bg="gray",
                    fg="white", font="none 12 bold").place(x=280, y=40)
        Radiobutton(root, activebackground="gray", activeforeground="white", text="PM", variable=ampm,
                    selectcolor="gray", value=2, command=lambda: click.button_Click(ampm.get()), bg="gray",
                    fg="white", font="none 12 bold").place(x=280, y=70)
        Button(root, text="SUBMIT", width=7, height=2,
               command=lambda: click.click(textentry_hour.get(), textentry_minute.get())).place(x=270, y=110)
        help = window()
        Button(root, text="QUIT", width=7, height=2, bg="#FF3232",
               command=lambda: help.kill_()).place(x=25, y=110)

    def main(self):
        root.configure(bg="gray")
        main_ = window()
        main_.create_Window()
        main_.labels()
        main_.inputs()
        root.mainloop()


while True:
    root = Tk(className="Timer")
    run = window()
    run.main()
    flip, stop, alarm = False, False, False
    if kill:
        kill = False
        break

    pygame.init()
    clock = pygame.time.Clock()  # FPS stuff
    crashed = False
    GD = pygame.display.set_mode((2048, 1200))
    GD = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    pygame.draw.rect(GD, (100, 100, 100), (0, 0, 2048, 1080))

    while not crashed:  # makes window not buggy
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    alarm = True

        pygame.draw.rect(GD, (100, 100, 100), (0, 0, 2048, 1200))
        GD.blit(pygame.transform.rotozoom(schedule, 0, 2),
                (GD.get_width() - pygame.transform.rotozoom(schedule, 0, 2).get_width(), 0))

        if stop:
            t1 = threading.Thread(target=play_sound, daemon=True)

            count += 1
            if count >= 85:
                t1.start()
                count = 0
            flip = not flip
            flash_screen(flip)

        display()

        if quit_button(20, 20, 100, 50) or alarm:
            break

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
