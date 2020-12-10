import pygame
from projectile import Projectile

#creer un class = joueur

class Player(pygame.sprite.Sprite):
    def __init__(self, game):

        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectile = pygame.sprite.Group()
        self.image = pygame.image.load('im/tank-2.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 450

    def launch_projectile(self):

        self.all_projectile.add(Projectile(self))


    def move_right(self):
        #si le joueuer n'est pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity


    def move_left(self):
        self.rect.x -= self.velocity
