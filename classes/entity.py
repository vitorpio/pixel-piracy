import pygame

from abc import ABC, abstractmethod


class Entity(ABC):

    def __init__(self, file_name: str, position: tuple):
        self.surface = pygame.image.load(file_name)
        self.rect = self.surface.get_rect(left=position[0], top=position[1])

    @abstractmethod
    def move(self):
        pass
