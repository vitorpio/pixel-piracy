from classes.entity import Entity
from classes.player import Player


class PlayerShoot (Entity):

    def __init__(self, file_name: str, position: tuple, speed: float, player: Player):
        super().__init__(file_name, position)
        self.speed = speed
        self.player = player

    def move(self):
        self.rect.centerx += self.speed
