import pathlib

import pygame


class Static:
    def __init__(self, imagePath: pathlib.Path, position: tuple((int, int))) -> None:
        self.surface: pygame.Surface = pygame.image.load(imagePath).convert_alpha()
        self.position: tuple((int, int)) = position

    def set(self, screen: pygame.Surface):
        return screen.blit(self.surface, self.position)