import pygame
import sys

from classes.consts import FPS_LEFT_MARGIN, FPS_TEXT_COLOR, FPS_TEXT_FONT, FPS_TEXT_SIZE, FPS_TOP_MARGIN, PLAYER_1_LEFT_MARGIN, PLAYER_TEXT_COLOR, PLAYER_TEXT_FONT, PLAYER_TEXT_SIZE, PLAYER_TOP_MARGIN, PLAYER_2_LEFT_MARGIN, TIME_LEFT_MARGIN, TIME_TEXT_COLOR, TIME_TEXT_FONT, TIME_TEXT_SIZE, TIME_TOP_MARGIN
from classes.player import Player


def place_text(window: pygame.Surface, text: str, text_size: int, text_color: tuple, text_font_name: str, text_center_position: tuple):
    text_font: pygame.font.Font = pygame.font.SysFont(
        text_font_name, size=text_size)
    text_surface: pygame.Surface = text_font.render(
        text, True, text_color).convert_alpha()
    text_rect: pygame.Rect = text_surface.get_rect(
        center=text_center_position)
    window.blit(text_surface, text_rect)


def place_fps(window: pygame.Surface, fps: float):
    text_font: pygame.font.Font = pygame.font.SysFont(
        FPS_TEXT_FONT, size=FPS_TEXT_SIZE)
    text_surface: pygame.Surface = text_font.render(
        f'FPS: {fps:.0f}', True, FPS_TEXT_COLOR).convert_alpha()
    text_rect: pygame.Rect = text_surface.get_rect(
        left=FPS_LEFT_MARGIN, bottom=FPS_TOP_MARGIN)
    window.blit(text_surface, text_rect)


def place_time(window: pygame.Surface, time: int):
    text_font: pygame.font.Font = pygame.font.SysFont(
        TIME_TEXT_FONT, size=TIME_TEXT_SIZE)
    text_surface: pygame.Surface = text_font.render(
        f'TIME: {time}', True, TIME_TEXT_COLOR).convert_alpha()
    text_rect: pygame.Rect = text_surface.get_rect(
        left=TIME_LEFT_MARGIN, bottom=TIME_TOP_MARGIN)
    window.blit(text_surface, text_rect)


def place_player_info(window: pygame.Surface, players: list[Player]):
    text_font: pygame.font.Font = pygame.font.SysFont(
        PLAYER_TEXT_FONT, size=PLAYER_TEXT_SIZE)
    for n, player in enumerate(players):
        text_surface: pygame.Surface = text_font.render(
            f'Player {n+1} - Health: {player.health} - Score: {player.score}', True, PLAYER_TEXT_COLOR).convert_alpha()
        text_rect: pygame.Rect = text_surface.get_rect(
            left=PLAYER_1_LEFT_MARGIN if n == 0 else PLAYER_2_LEFT_MARGIN, top=PLAYER_TOP_MARGIN)
        window.blit(text_surface, text_rect)


def quit_game():
    pygame.quit()
    sys.exit()
