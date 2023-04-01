import pygame

pygame.init()

WIDTH = 760
HEIGHT = 800
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
timer = pygame.time.Clock()

run = True

while run:
    timer.tick(FPS)
    screen.fill('white')
    pygame.draw.circle(screen, 'black', (300, 300), 15, 0)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if (290, 290) <= pygame.mouse.get_pos() <= (310, 310):
                    print('Yes')
        

    pygame.display.update()

pygame.quit()