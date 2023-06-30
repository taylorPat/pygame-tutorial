import pathlib
import sys
import pygame

pygame.init()

GAME_HEIGHT = 800
GAME_WIDTH = 400
GROUND_ZERO = 300
screen = pygame.display.set_mode((GAME_HEIGHT, GAME_WIDTH))
pygame.display.set_caption("Runner")

sky_surface = pygame.image.load(pathlib.Path('app/assets/graphics/Sky.png'))
ground_surface = pygame.image.load(pathlib.Path('app/assets/graphics/ground.png'))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, GROUND_ZERO))
    pygame.display.update()
