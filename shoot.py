import pygame as py, display

def check_hit():
    # aim_dim = [display.ring.topleft, display.ring.topright, display.ring.bottomleft, display.ring.right]
    try:
        for point in display.position_list:

            if display.ring.collidepoint(point[0], point[1]):
                display.position_list.pop(display.position_list.index(point))
                return True

            elif display.ring.collidepoint(point[0]+32, point[1]+32):
                display.position_list.pop(display.position_list.index(point))
                return True
    except:
        pass