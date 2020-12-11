import pygame

#definir la classe qui va gerer le projectile du joueur

class Projectile(pygame.sprite.Sprite): #héritage qui nous permet de prendre la classe comment élément graphique du jeu

    #definir le ocnstructeur
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load('im/laser.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 100
        self.rect.y = player.rect.y + 0
        self.origin_image = self.image
        self.angle = 0


    def rotate(self):
        #faire tourner le projo en deplacement
        self.angle += 8
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center = self.rect.center)


    def remove(self):
        self.player.all_projectile.remove(self)


    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        #verifier si le projectile entre en collision avec le monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            #supprimer le projectile
            self.remove()
            # infliger des degats
            monster.damage(self.player.attack) #le monstre subit des degats selon les attacks

        #verifier si notre projectile n'est plus present sur l'ecran
        if self.rect.x > 1080:
            #supprimer le projo
            self.remove()
            print("projo supprimé")




