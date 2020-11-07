#!/usr/bin/env python3

import pygame
import time
import sys
from datetime import datetime
from tkinter import *
import playsound
import threading
import calculate_time


hour, minute, ampm = "0", "0", 0
width, hight = 300, 200
stop, kill, flip = False, False, False
count, count2 = 10000, 100000


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
    playsound.playsound(r"/home/agmui/Desktop/pyImages/sempai.mp3", True)
    playsound.playsound(r"/home/agmui/Desktop/pyImages/sempai_2.mp3", True)


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

    timer(h, m, s)
    text(H, M, S)


class window:
    def __init__(self):
        self.kill = False

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
            Label(root, text="Input AM or PM", bg="gray", fg="white", font="none 12 bold").place(x=160, y=30)
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
        root.geometry(str(width) + "x" + str(hight))

    def labels(self):
        Label(root, text="Input next class time: ", bg="gray", fg="white", font="none 20 bold").place(x=5, y=0)
        Label(root, text=":", bg="gray", fg="white", font="none 12 bold").place(x=100, y=47)

    def inputs(self):
        click = window()
        textentry_hour = Entry(root, width=5, bg="white")
        textentry_hour.place(x=60, y=50)
        textentry_minute = Entry(root, width=5, bg="white")
        textentry_minute.place(x=118, y=50)
        ampm = IntVar()
        Radiobutton(root, activebackground="gray", activeforeground="white", text="AM", variable=ampm,
                    selectcolor="gray", value=1, command=lambda: click.button_Click(ampm.get()), bg="gray",
                    fg="white", font="none 12 bold").place(x=200, y=50)
        Radiobutton(root, activebackground="gray", activeforeground="white", text="PM", variable=ampm,
                    selectcolor="gray", value=2, command=lambda: click.button_Click(ampm.get()), bg="gray",
                    fg="white", font="none 12 bold").place(x=200, y=80)
        Button(root, text="SUBMIT", width=6,
               command=lambda: click.click(textentry_hour.get(), textentry_minute.get())).place(x=25, y=100)
        help = window()
        Button(root, text="QUIT", width=6,
               command=lambda: help.kill_()).place(x=240, y=170)

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
    flip, stop = False, False
    if kill:
        kill = False
        break

    pygame.init()
    clock = pygame.time.Clock()  # FPS stuff
    crashed = False
    GD = pygame.display.set_mode((2048, 1080))
    GD = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    pygame.draw.rect(GD, (100, 100, 100), (0, 0, 2048, 1080))

    while not crashed:  # makes window not buggy
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    alarm = False

        pygame.draw.rect(GD, (100, 100, 100), (0, 0, 2048, 1080))

        if stop:
            t1 = threading.Thread(target=play_sound)

            count += 1
            if count >= 85:
                t1.start()
                count = 0
            flip = not flip
            flash_screen(flip)

        display()

        if quit_button(20, 20, 100, 50):
            break

        pygame.display.update()
        clock.tick(60)
        time.sleep(0.1)

    pygame.quit()
quit()
