from functools import cached_property
import pathlib

import pygame
from app.constants import GAME_WIDTH


class Snail:
    def __init__(
        self,
        imagePath: pathlib.Path,
        relPlacement: tuple,
        velocity: int,
        relPlacementStr: str = "midbottom",
        rerun: bool = False,
    ) -> None:
        self.imagePath: pathlib.Path = imagePath
        self.relativePlacement = {relPlacementStr: relPlacement}
        self.velocity: int = velocity
        self.rerun: bool = rerun

    @property
    def surface(self):
        return pygame.image.load(self.imagePath).convert_alpha()

    @cached_property
    def rectangle(self):
        return self.surface.get_rect(**self.relativePlacement)

    
    @property
    def x(self):
        return self.rectangle.x
    
    @property
    def y(self):
        return self.rectangle.y

    @property
    def move_x(self):
        self.rectangle.x -= self.velocity
        if self.rectangle.right < 0 and self.rerun:
            self.rectangle.left = GAME_WIDTH
        return self.rectangle.x