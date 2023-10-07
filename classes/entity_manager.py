
import itertools

from classes.consts import WINDOW_SIZE
from classes.enemy import Enemy
from classes.enemy_shoot import EnemyShoot
from classes.entity import Entity
from classes.player import Player
from classes.player_shoot import PlayerShoot


class EntityManager:

    @staticmethod
    def verify_collisions(players: list[Player],
                          player_shoots: list[PlayerShoot],
                          enemies: list[Enemy],
                          enemy_shoots: list[EnemyShoot]):

        EntityManager.__remove_entities_out_of_screen(player_shoots)
        EntityManager.__remove_entities_out_of_screen(enemy_shoots)

        for (player_shoot, enemy) in itertools.product(player_shoots, enemies):
            if EntityManager.__verify_collision_entities(player_shoot, enemy):
                player_shoot.player.score += 1
                player_shoots.remove(player_shoot)
                enemies.remove(enemy)

        for (enemy_shoot, player) in itertools.product(enemy_shoots, players):
            if EntityManager.__verify_collision_entities(enemy_shoot, player):
                enemy_shoots.remove(enemy_shoot)
                player.health -= 1

        for (player, enemy) in itertools.product(players, enemies):
            if EntityManager.__verify_collision_entities(player, enemy):
                player.health = 0
                enemies.remove(enemy)

    @staticmethod
    def __remove_entities_out_of_screen(entities: list[Entity]):
        for entity in entities:
            if EntityManager.__verify_collision_screen(entity):
                entities.remove(entity)

    @staticmethod
    def __verify_collision_screen(entity: Entity):
        return entity.rect.right < 0 or entity.rect.left > WINDOW_SIZE[1]

    @staticmethod
    def __verify_collision_entities(entity1: Entity, entity2: Entity):
        return entity1.rect.right > entity2.rect.left and\
            entity1.rect.left < entity2.rect.right and\
            entity1.rect.bottom > entity2.rect.top and\
            entity1.rect.top < entity2.rect.bottom
