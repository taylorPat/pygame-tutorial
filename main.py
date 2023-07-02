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

snail = Snail(
    imagePath=pathlib.Path("app/assets/graphics/snail/snail1.png"),
    relPlacement=(600, GROUND_ZERO),
    velocity=1,
    rerun=True,
)

player_surf = pygame.image.load(
    pathlib.Path("app/assets/graphics/Player/player_walk_1.png")
)
player_rect = player_surf.get_rect(midbottom=(80, GROUND_ZERO))

if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, GROUND_ZERO))
        screen.blit(text_surface, (300, 50))
        screen.blit(snail.surface, (snail.move_x, snail.y))
        screen.blit(player_surf, player_rect)
        pygame.display.update()
