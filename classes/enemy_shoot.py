from classes.entity import Entity


class EnemyShoot (Entity):

    def __init__(self, file_name: str, position: tuple, speed: float):
        super().__init__(file_name, position)
        self.speed = speed

    def move(self):
        self.rect.centerx -= self.speed
