
import pygame
import random

from classes.consts import BACKGROUND_MOVE_EVENT, ENEMY_1, ENEMY_2, ENEMY_SHOOT_EVENT, ENEMY_SHOOT_OFFSET, FPS, MENU_OPTIONS, NEW_NEMEY_EVENT, PLAYER_1, PLAYER_SHOOT_EVENT, PLAYER_2, PLAYER_SHOOT_OFFSET
from classes.enemy import Enemy
from classes.enemy_shoot import EnemyShoot
from classes.entity_factory import EntityFactory
from classes.entity_manager import EntityManager
from classes.player import Player
from classes.player_shoot import PlayerShoot
from classes.utils import place_fps, place_time, quit_game, place_player_info


class Level:

    def __init__(self, window: pygame.Surface, level: dict, game_mode: str):
        self.window = window
        self.name = level['NAME']
        self.music = level['MUSIC']
        self.game_mode = game_mode
        self.level_enemies = [ENEMY_1, ENEMY_2]
        self.enemy_spawn_delay = level['ENEMY_SPAWN_DELAY']

        self.background = EntityFactory.get_entity(level)
        self.players: list[Player] = [EntityFactory.get_entity(PLAYER_1)]
        self.enemies: list[Enemy] = []
        self.playes_shoots: list[PlayerShoot] = []
        self.enemy_shoots: list[EnemyShoot] = []
        if self.game_mode in [MENU_OPTIONS[1], MENU_OPTIONS[2]]:
            self.players.append(EntityFactory.get_entity(PLAYER_2))

        self.clock = pygame.time.Clock()
        self.level_started_ticks = pygame.time.get_ticks()

        pygame.time.set_timer(NEW_NEMEY_EVENT, self.enemy_spawn_delay)

    def run(self) -> list[int]:
        # Level music
        pygame.mixer_music.load(self.music)
        pygame.mixer_music.set_volume(0.1)
        pygame.mixer_music.play(-1)

        while True:

            # Detect Events
            for event in pygame.event.get():
                if event.type == BACKGROUND_MOVE_EVENT:
                    self.background.move()

                if event.type == NEW_NEMEY_EVENT:
                    enemy = random.choice(self.level_enemies)
                    self.enemies.append(EntityFactory.get_entity(enemy))

                if event.type == PLAYER_SHOOT_EVENT:
                    player = event.dict['player']
                    shoot = player.shoot
                    self.playes_shoots.append(EntityFactory.get_entity(
                        {**shoot,
                         'POSITION': (player.rect.centerx + PLAYER_SHOOT_OFFSET[0],
                                      player.rect.centery + PLAYER_SHOOT_OFFSET[1]),
                         'PLAYER': player},),
                    )

                if event.type == ENEMY_SHOOT_EVENT:
                    enemy = event.dict['enemy']
                    shoot = enemy.shoot
                    self.enemy_shoots.append(EntityFactory.get_entity(
                        {**enemy.shoot,
                         'POSITION': (enemy.rect.centerx - ENEMY_SHOOT_OFFSET[0],
                                      enemy.rect.centery - ENEMY_SHOOT_OFFSET[1],)})
                    )

                if event.type == pygame.QUIT:
                    quit_game()

            # Draw entities
            self.window.blit(
                source=self.background.surface, dest=self.background.rect)
            for entity in [player for player in self.players if player.health] + self.enemies + self.playes_shoots + self.enemy_shoots:
                entity.move()
                self.window.blit(source=entity.surface, dest=entity.rect)
            place_fps(self.window, self.clock.get_fps())
            place_time(self.window, int(
                (pygame.time.get_ticks() - self.level_started_ticks)/1000))

            place_player_info(self.window, self.players)

            # Detect collisions
            EntityManager.verify_collisions(
                [player for player in self.players if player.health], self.playes_shoots, self.enemies, self.enemy_shoots)

            # Check if all players are dead
            if all([not player.health for player in self.players]):
                pygame.mixer_music.stop()
                return [player.score for player in self.players]

            pygame.display.flip()

            self.clock.tick(FPS)
