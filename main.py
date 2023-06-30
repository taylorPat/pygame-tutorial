import pathlib
import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")

sky_surface = pygame.image.load(pathlib.Path('app/assets/graphics/Sky.png'))
ground_surface = pygame.image.load(pathlib.Path('app/assets/graphics/ground.png'))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(sky_surface, (0, 10))
    screen.blit(ground_surface, (0, 300))
    pygame.display.update()
