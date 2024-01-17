import pygame as py
import display

py.init()

#variables
font1 = py.font.SysFont("8514OEM", 40)
font2 = py.font.SysFont("8514OEM", 30)
def box(x,y):
    score_txt = font1.render("SCORE", True, display.white)
    time_txt = font2.render("TIME LEFT", True, display.white)

    score_box = py.draw.rect(display.display, display.white, py.Rect(x,y,250,50), 5, 15)
    timer_box = py.draw.rect(display.display, display.white, py.Rect(display.width-175, y, 150, 50), 5, 15)
    
    score_txt_rect = score_txt.get_rect()
    timer_txt_rect = time_txt.get_rect()
    score_txt_rect.center = (score_box.centerx, score_box.top - 15)
    timer_txt_rect.center = (timer_box.centerx, timer_box.top - 15)


    #score counter and timer
    score = font1.render(str(display.score), True, display.white)
    score_rect = score.get_rect()
    score_rect.center = score_box.center

    timer = font1.render(str(display.time_left//24), True, display.white)
    timer_rect = timer.get_rect()
    timer_rect.center = timer_box.center

    display.display.blit(score_txt, score_txt_rect)
    display.display.blit(time_txt, timer_txt_rect)
    display.display.blit(score, score_rect)
    display.display.blit(timer, timer_rect)
