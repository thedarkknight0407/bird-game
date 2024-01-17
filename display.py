import pygame as py, graphics, random, shoot, main_screen, end_screen
from movement import *
py.init()

#Variables
clock = py.time.Clock
width = 600
height = 600
display = py.display.set_mode((width,height))
running = False
score = 0
time_left = 2880 #in ms
clock = py.time.Clock()
last_update = py.time.get_ticks()
cooldown = 100
frame = 0
position_list = []
color_list = []
#bg
bg = py.image.load("bg.png")
bird_img = [
    [
    py.image.load("assests/blue_bird/  (1).png"),
    py.image.load("assests/blue_bird/  (2).png"),
    py.image.load("assests/blue_bird/  (3).png"),
    py.image.load("assests/blue_bird/  (4).png"),
    py.image.load("assests/blue_bird/  (5).png"),
    py.image.load("assests/blue_bird/  (6).png"),
    py.image.load("assests/blue_bird/  (7).png"),
    py.image.load("assests/blue_bird/  (8).png")
],
[
    py.image.load("assests/green_bird/1.png"),
    py.image.load("assests/green_bird/2.png"),
    py.image.load("assests/green_bird/3.png"),
    py.image.load("assests/green_bird/4.png"),
    py.image.load("assests/green_bird/5.png"),
    py.image.load("assests/green_bird/6.png"),
    py.image.load("assests/green_bird/7.png"),
    py.image.load("assests/green_bird/8.png")    
],
[
    py.image.load("assests/red_bird/1.png"),
    py.image.load("assests/red_bird/2.png"),
    py.image.load("assests/red_bird/3.png"),
    py.image.load("assests/red_bird/4.png"),
    py.image.load("assests/red_bird/5.png"),
    py.image.load("assests/red_bird/6.png"),
    py.image.load("assests/red_bird/7.png"),
    py.image.load("assests/red_bird/8.png")    
]]

cloud = py.image.load('assests/clod.png')
py.transform.scale2x(cloud)
#colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
cyan = "cyan"
lime = "lime"
#Shapes

aim_x = width/2
aim_y  = (height/3)
ring = py.Rect

def aim(x,y):
    global ring
    ring = py.draw.circle(display, red, (x,y), 30, 5)
    py.draw.circle(display, red, ring.center, 5)

#game play variables
bird_count = 2

main_screen.main_screen()

#functions

#creates a list with random positions
for i in range(200):
    position_list.append([random.randrange(600,700), random.randrange(0,400,20), random.randint(0,2)])
    # color_list.append(random.randint(0,2))

print(color_list)

def bird(current_time, x, y, color):
    global last_update, frame, bird_count
    if current_time - last_update >= cooldown:
        frame += 1
        last_update = current_time
        if frame >= 8:
            frame = 0
    bird = bird_img[color][frame]
    bird.set_colorkey(white)
    display.blit(bird, (x, y))
    return bird

#Loop
while running and time_left != 0:
    
    #timer initiation
    # timer.game_timer()

    #setting bg and graphics
    display.fill(white)
    display.blit(bg, (-15,375))
    graphics.box(25, height - 75)
    display.blit(cloud, (50,75))
    display.blit(cloud, (350,200))
    #drawing birds
    # display.blit(disk.draw_bird(), (50,50))
    current_time = py.time.get_ticks()
    for i in range(bird_count + 1):
        try:
            birdie = bird(current_time, position_list[i][0], position_list[i][1], position_list[i][2])
            
        except:
            print('game has ended')
        if position_list[i][0] >= -64:
            position_list[i][0] -= 5
        elif position_list[i][0] <= -64:
            bird_count -= 1
            position_list.pop(i)

    #check for birds
    if bird_count < 0:
        bird_count = random.randint(0,2)
        birdie = None




    
    #Drawing the aim
    aim(aim_x, aim_y)

    #Event handling
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        movement(event)

        if event.type == py.KEYDOWN:
            if event.key == py.K_SPACE and shoot.check_hit():
                score += 1 
                
                bird_count -= 1


    
    py.display.update()
    time_left -= 1
    clock.tick(24)
    
end_screen.end_screen()