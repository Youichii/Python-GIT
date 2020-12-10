import pygame
from player import Player
from monster import Monster



#classe du jeu
class Game():
    def __init__(self):

        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.monster = Monster(self)
        self.all_monsters = pygame.sprite.Group()
        self.all_players.add(self.player)
        self.pressed = {}
        self.spawn_monster() #appel de la methode


    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster) #ajoute un monstre au groupe de monstres





