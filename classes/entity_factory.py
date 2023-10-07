import random

import classes
from classes.background import Background
from classes.consts import WINDOW_SIZE, PLAYER_MAX_POSITIONS
from classes.enemy import Enemy
from classes.enemy_shoot import EnemyShoot
from classes.entity import Entity
from classes.player import Player
from classes.player_shoot import PlayerShoot


class EntityFactory:

    @staticmethod
    def get_entity(entity: dict) -> Entity:
        if entity['CLASS'] == classes.level.Level.__name__:
            return Background(entity['BACKGROUND_FILENAME'],
                              (0, 0),
                              int(1000/entity['BACKGROUND_FPS']),
                              entity['BACKGROUND_TOTAL_FRAMES'],)
        elif entity['CLASS'] == classes.player.Player.__name__:
            return Player(entity['FILENAME'], entity['POSITION'], entity['MOVEMENT_KEYS'], entity['SHOOT'])
        elif entity['CLASS'] == classes.enemy.Enemy.__name__:
            return Enemy(entity['FILENAME'], (WINDOW_SIZE[0] + entity['SIZE'][0], random.randint(PLAYER_MAX_POSITIONS[0], PLAYER_MAX_POSITIONS[2] - entity['SIZE'][1])), entity['SPEED'], entity['SHOOT'])
        elif entity['CLASS'] == classes.player_shoot.PlayerShoot.__name__:
            return PlayerShoot(entity['FILENAME'], entity['POSITION'], entity['SPEED'], entity['PLAYER'])
        elif entity['CLASS'] == classes.enemy_shoot.EnemyShoot.__name__:
            return EnemyShoot(entity['FILENAME'], entity['POSITION'], entity['SPEED'])
        else:
            raise NotImplemented()
