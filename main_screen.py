import pygame as py, display


def main_screen():
    font = py.font.SysFont("comicsans", 64)
    font2 = py.font.SysFont("comicsans", 32)
    text = font.render("Bird Shooter!!", True, display.white)
    text_rect = text.get_rect()
    text_rect.center = (display.width/2, 150)
    bg = py.image.load('bg.jpg')
    run = True

    def start_button():
        button = py.Rect(0,0, 350,75)
        button.center = (display.width/2, 2*(display.height/3))
        py.draw.rect(display.display, display.white, button, 5, 10)
        button_text = font2.render("Press SPACE to start", True, display.white)
        button_text_rect = button_text.get_rect()
        button_text_rect.center = (display.width/2, 2*(display.height/3))
        display.display.blit(button_text, button_text_rect)
        pass


    while run:
        display.display.blit(bg, (0,0))
        display.display.blit(text, text_rect)

        start_button()

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

            elif event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                    display.running = True
                    run = False
        py.display.update()