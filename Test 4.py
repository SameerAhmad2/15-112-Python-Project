import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))

a = pygame.sprite.Sprite()
a.image = pygame.Surface((20, 100))
a.image.set_colorkey((0, 0, 0))
a.image.fill((0, 255, 0))
a.rect = a.image.get_rect()
a.rect.topleft = (100, 100)
# Use the original image for rotation and never modify it.
a.orig_image = a.image

a_group = pygame.sprite.Group()
a_group.add(a)
position1 = (a.rect.centerx, a.rect.centery)

clock = pygame.time.Clock()  # Use a clock to limit the framerate.
angle = 0

while True:
    # Increase the angle.
    angle = (angle + 45) % 360

    screen.fill((255,255,255))
    a_group.draw(screen)
    pygame.draw.rect(screen, (0,0,0), (100,100,20,100), 1)
    pygame.draw.circle(screen, (0,0,255), position1, 1)

    orig_center = a.rect.center  # Save original center of sprite.
    # Rotate using the original image.
    a.image = pygame.transform.rotate(a.orig_image, angle)
    # Get the new rect and set its center to the original center.
    a.rect = a.image.get_rect(center=orig_center)

    pygame.display.update()
    if pygame.event.get(pygame.QUIT):
        break
    clock.tick(1)  # Framerate is 1 FPS.

pygame.quit()
