import pygame

from classes.consts import FINAL_SCORE_FONT_SIZE, FINAL_SCORE_OFFSET, FINAL_SCORE_OPTION_OFFSET, FINAL_SCORE_OPTION_SPACE_BETWEEN, FINAL_SCORE_OPTIONS, FINAL_SCORE_SELECTED_TEXT_COLOR, FINAL_SCORE_SPACE_BETWEEN, FINAL_SCORE_TEXT_COLOR, FINAL_SCORE_TEXT_FONT, GAME_OVER_FONT_SIZE, GAME_OVER_OFFSET, GAME_OVER_TEXT_COLOR, MENU_BACKGROUND, MENU_OPTIONS, WINDOW_SIZE
from classes.utils import place_text, quit_game


class FinalScore:
    menu_option = 0

    def __init__(self, window: pygame.Surface, game_mode: str, player_score: list[int]):
        self.window = window
        self.surface = pygame.image.load(
            MENU_BACKGROUND).convert_alpha()
        self.rect = self.surface.get_rect(left=0, top=0)
        self.game_mode = game_mode
        self.player_score = player_score

    def run(self):
        # TODO Score Music

        self.window.blit(self.surface, self.rect)

        self.show_score()
        self.reload_final_score_options()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if self.menu_option < len(FINAL_SCORE_OPTIONS) - 1:
                            self.menu_option += 1
                        else:
                            self.menu_option = 0
                        self.reload_final_score_options()
                    elif event.key == pygame.K_UP:
                        if self.menu_option > 0:
                            self.menu_option -= 1
                        else:
                            self.menu_option = len(FINAL_SCORE_OPTIONS) - 1
                        self.reload_final_score_options()
                    elif event.key == pygame.K_RETURN:
                        return FINAL_SCORE_OPTIONS[self.menu_option]
            pygame.display.flip()

    def show_score(self):
        place_text(self.window,
                   f'GAME OVER',
                   GAME_OVER_FONT_SIZE,
                   GAME_OVER_TEXT_COLOR,
                   FINAL_SCORE_TEXT_FONT,
                   (WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2 + GAME_OVER_OFFSET))
        if self.game_mode == MENU_OPTIONS[2]:
            place_text(self.window,
                       f'PLAYER 1 + PLAYER 2 - SCORE: {sum(self.player_score)}',
                       FINAL_SCORE_FONT_SIZE,
                       FINAL_SCORE_TEXT_COLOR,
                       FINAL_SCORE_TEXT_FONT,
                       (WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2 + FINAL_SCORE_OFFSET))
        else:
            for position, score in enumerate(self.player_score):
                place_text(self.window,
                           f'PLAYER {position+1} - SCORE: {score}',
                           FINAL_SCORE_FONT_SIZE,
                           FINAL_SCORE_TEXT_COLOR,
                           FINAL_SCORE_TEXT_FONT,
                           (WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2 + FINAL_SCORE_OFFSET + (FINAL_SCORE_SPACE_BETWEEN * position)))

    def reload_final_score_options(self):
        for position, option in enumerate(FINAL_SCORE_OPTIONS):
            place_text(self.window,
                       option,
                       FINAL_SCORE_FONT_SIZE,
                       FINAL_SCORE_TEXT_COLOR if position != self.menu_option else FINAL_SCORE_SELECTED_TEXT_COLOR,
                       FINAL_SCORE_TEXT_FONT,
                       (WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2 + FINAL_SCORE_OPTION_OFFSET + (FINAL_SCORE_OPTION_SPACE_BETWEEN * position)))
