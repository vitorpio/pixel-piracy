import pygame

from classes.level import Level
from classes.menu import Menu
from classes.consts import FINAL_SCORE_OPTIONS, FPS, LEVELS, MENU_OPTIONS, WINDOW_SIZE
from classes.score import FinalScore
from classes.utils import quit_game


class Game:

    def __init__(self) -> None:
        pygame.init()
        self.window = pygame.display.set_mode(WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        self.replay = False

    def run(self):
        while True:
            if not self.replay:
                menu = Menu(self.window)
                self.menu_option = menu.run()

            if self.menu_option == MENU_OPTIONS[3]:
                # TODO High Score window
                quit_game()
            elif self.menu_option == MENU_OPTIONS[4]:
                quit_game()
            else:
                level = Level(
                    self.window, LEVELS['1'], self.menu_option)
                player_score = level.run()

                final_score = FinalScore(
                    self.window, self.menu_option, player_score)
                final_score_option = final_score.run()
                if final_score_option == FINAL_SCORE_OPTIONS[2]:
                    quit_game()
                self.replay = final_score_option == FINAL_SCORE_OPTIONS[0]

            self.clock.tick(FPS)
