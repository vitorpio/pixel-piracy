import pygame

from classes.consts import BACKGROUND_MOVE_EVENT, WINDOW_SIZE
from classes.entity import Entity


class Background(Entity):

    def __init__(self, file_name: str,  position: tuple, delay: int, total_frames: int):
        super().__init__(file_name, position)
        self.current_frame = 1
        self.total_frames = total_frames

        pygame.time.set_timer(BACKGROUND_MOVE_EVENT, delay)

    def move(self):
        if self.current_frame < self.total_frames:
            self.rect.centerx -= WINDOW_SIZE[0]
            self.current_frame += 1
        else:
            self.rect.left = 0
            self.current_frame = 1
