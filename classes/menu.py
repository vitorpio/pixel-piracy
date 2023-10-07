import pygame

from classes.consts import GAME_TITLE, MENU_BACKGROUND, MENU_MUSIC, MENU_OPTION_FONT_SIZE, MENU_OPTIONS, MENU_OPTION_OFFSET, MENU_SELECTED_TEXT_COLOR, MENU_TEXT_COLOR, MENU_TEXT_FONT, MENU_TITLE_FONT_SIZE, MENU_TITLE_OFFSET, WINDOW_SIZE, MENU_OPTION_SPACE_BETWEEN
from classes.utils import place_text, quit_game


class Menu:
    menu_option = 0

    def __init__(self, window: pygame.Surface):
        self.window = window
        self.surface = pygame.image.load(
            MENU_BACKGROUND).convert_alpha()
        self.rect = self.surface.get_rect(left=0, top=0)

    def run(self):
        # TODO Menu music

        self.window.blit(self.surface, self.rect)
        place_text(self.window,
                   GAME_TITLE,
                   MENU_TITLE_FONT_SIZE,
                   MENU_TEXT_COLOR,
                   MENU_TEXT_FONT,
                   (WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2 + MENU_TITLE_OFFSET))
        self.reload_menu_options()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if self.menu_option < len(MENU_OPTIONS) - 1:
                            self.menu_option += 1
                        else:
                            self.menu_option = 0
                        self.reload_menu_options()
                    elif event.key == pygame.K_UP:
                        if self.menu_option > 0:
                            self.menu_option -= 1
                        else:
                            self.menu_option = len(MENU_OPTIONS) - 1
                        self.reload_menu_options()
                    elif event.key == pygame.K_RETURN:
                        return MENU_OPTIONS[self.menu_option]

            pygame.display.flip()

    def reload_menu_options(self):
        for pos, option in enumerate(MENU_OPTIONS):
            place_text(self.window,
                       option,
                       MENU_OPTION_FONT_SIZE,
                       MENU_TEXT_COLOR if pos != self.menu_option else MENU_SELECTED_TEXT_COLOR,
                       MENU_TEXT_FONT,
                       (WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2 + MENU_OPTION_OFFSET + MENU_OPTION_SPACE_BETWEEN * (pos + 1)))
