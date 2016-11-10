import pygame
pygame.init()

display_width = 1000
display height = 820

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("RaceNesh")
clock = pygame.time.Clock()

#GameLoop Time

crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygsme.QUIT:
            crashed = True

        print (event)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
