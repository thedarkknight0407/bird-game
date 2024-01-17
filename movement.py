import pygame as py
import display
py.init()

#variables
move_bool = [False, False, False, False] #up,down,right,left
vel = 7
acc = 0
def movement(event):
    if event.type == py.KEYDOWN:
        if event.key == py.K_w:
            move_bool[0] = True
        elif event.key == py.K_s:
            move_bool[1] = True
        elif event.key == py.K_d:
            move_bool[2] = True
        elif event.key == py.K_a:
            move_bool[3] = True
    elif event.type == py.KEYUP:
        if event.key == py.K_w:
            move_bool[0] = False
        elif event.key == py.K_s:
            move_bool[1] = False
        elif event.key == py.K_d:
            move_bool[2] = False
        elif event.key == py.K_a:
            move_bool[3] = False

    for i in range(4):
        if move_bool[i]:
            if i == 0 and display.aim_y >= 35:
                display.aim_y -= vel
            elif i == 1 and display.aim_y <= 400:
                display.aim_y += vel
            elif i == 2 and display.aim_x <= 565:
                display.aim_x += vel
            elif i == 3 and display.aim_x >= 35:
                display.aim_x -= vel