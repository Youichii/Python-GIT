import pygame
import random


#créer une classe qui gère les monstres

class Monster(pygame.sprite.Sprite):

    def __init__(self, game):

        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load('im/robot-4.png')
        self.rect = self.image.get_rect()
        self.rect.x = 950 # + random.randint(0, 300)
        self.rect.y = 450
        self.velocity = 1 #=random.randint(1, 3)


    def damage(self, amount):
        #infliger les degats
        self.health -= amount

        #Si son nouveau nombre de point de vie est >= 0
        if self.health <= 0:
            # Reapparaitre comme un nouveau monstre
            self.rect.x = 1000 # + random.randint(0, 300)
            # self.velocity = random.randint(1, 3)
            self.health = self.max_health
            self.game.score.points +=1

    def update_health_bar(self, surface):

        #dessiner la bar de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface,(111, 210, 46), [self.rect.x + 10, self.rect.y -20, self.health, 5])



    def forward(self):
        #le deplacement se fait que s'il n"y a pas de collision avec joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity

        #si le monstre est en collision avec le joueur
        else:
            self.game.player.damage(self.attack)


