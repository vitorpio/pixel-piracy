import pygame
from classes.consts import PLAYER_SHOOT_EVENT, PLAYER_MAX_POSITIONS, PLAYER_SPEED
from classes.entity import Entity


class Player (Entity):

    def __init__(self, file_name: str, position: tuple, movement_keys: list, shoot: dict):
        super().__init__(file_name, position)
        self.movement_keys = movement_keys
        self.shoot = shoot
        self.speed = PLAYER_SPEED
        self.health = 3
        self.score = 0
        self.last_time_shoot = 0

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[self.movement_keys[0]] and self.rect.top > PLAYER_MAX_POSITIONS[0]:
            self.rect.centery -= self.speed
        if pressed_key[self.movement_keys[1]] and self.rect.right < PLAYER_MAX_POSITIONS[1]:
            self.rect.centerx += self.speed
        if pressed_key[self.movement_keys[2]] and self.rect.bottom < PLAYER_MAX_POSITIONS[2]:
            self.rect.centery += self.speed
        if pressed_key[self.movement_keys[3]] and self.rect.left > PLAYER_MAX_POSITIONS[3]:
            self.rect.centerx -= self.speed
        if pressed_key[self.shoot['KEY']] and\
                pygame.time.get_ticks() - self.last_time_shoot > self.shoot['DELAY']:
            pygame.event.post(pygame.event.Event(
                PLAYER_SHOOT_EVENT,
                {'player': self})
            )
            self.last_time_shoot = pygame.time.get_ticks()
