import pathlib
import sys
import pygame

from app.constants import GAME_HEIGHT, GAME_WIDTH, GROUND_ZERO
from app.snail import Snail

pygame.init()


screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Runner")
test_font = pygame.font.Font(pathlib.Path("app/assets/font/Pixeltype.ttf"), 50)

sky_surface = pygame.image.load(pathlib.Path("app/assets/graphics/Sky.png"))
ground_surface = pygame.image.load(pathlib.Path("app/assets/graphics/ground.png"))
text_surface = test_font.render("My game", False, "Black")

snail_surface = pygame.image.load(pathlib.Path("app/assets/graphics/snail/snail1.png"))
snail_x_pos = 600
snail = Snail(x=snail_x_pos, velocity=4, rerun=True)

if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, GROUND_ZERO))
        screen.blit(text_surface, (300, 50))
        screen.blit(snail_surface, (snail.move_x, 250))
        pygame.display.update()


