from app.constants import GAME_WIDTH


class Snail:
    def __init__(self, x: int, velocity: int, rerun: bool = False) -> None:
        self.x: int = x 
        self.velocity: int = velocity
        self.rerun: bool = rerun 
    
    @property
    def move_x(self):
        self.x -= self.velocity
        if self.x < 0 and self.rerun:
            self.x = GAME_WIDTH + 200
        return self.x