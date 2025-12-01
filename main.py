import pygame

pygame.init()


screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("PYTHON 93 GAME")

icon = pygame.image.load('images/img_1.png')
pygame.display.set_icon(icon)

running = True
while running:

    # screen.fill('Red')

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                screen.fill("Blue")
            elif event.key == pygame.K_s:
                screen.fill("Red")
