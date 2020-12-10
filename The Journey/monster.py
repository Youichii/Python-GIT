import pygame


#créer une classe qui gère les monstres

class Monster(pygame.sprite.Sprite):

    def __init__(self, game):

        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pygame.image.load('im/robot-4.png')
        self.rect = self.image.get_rect()
        self.rect.x = 750
        self.rect.y = 450
        self.velocity = 2

    def damage(self, amount):
        #infliger les degats
        self.health -= amount

    def update_health_bar(self, surface):
        #definir une couleur pour la couleur de la jauge de vie
        bar_color = (111, 210, 46)
        #definir une couleur pour l'arriere plan de la jauge
        back_bar_color=(60, 63, 60)

        #definir la position de la jauge de vie ainsi que sa largeur et epaisseur
        bar_position = [self.rect.x + 10, self.rect.y -20, self.health, 5]
        #position de l'arriere plan de la jauge
        back_bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]


        #dessiner la bar de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)



    def forward(self):
        #le deplacement se fait que s'il n"y a pas de collision avec joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity


