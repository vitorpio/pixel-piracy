import pygame

from classes.consts import ENEMY_SHOOT_EVENT
from classes.entity import Entity


class Enemy (Entity):

    def __init__(self, file_name: str, position: tuple, speed: float, shoot: dict):
        super().__init__(file_name, position)
        self.speed = speed
        self.shoot = shoot
        self.last_time_shoot = 0

    def move(self):
        self.rect.centerx -= self.speed

        if pygame.time.get_ticks() - self.last_time_shoot > self.shoot['DELAY']:
            pygame.event.post(pygame.event.Event(
                ENEMY_SHOOT_EVENT,
                {'enemy': self}))
            self.last_time_shoot = pygame.time.get_ticks()
