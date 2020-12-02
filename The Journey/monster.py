import pygame


#créer une classe qui gère les monstres

class Monster(pygame.sprite.Sprite):

    def __int__(self):

        super().__int__()
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()


