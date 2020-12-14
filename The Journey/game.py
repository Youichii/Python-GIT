import pygame
from player import Player
from monster import Monster
from score import Score




#classe du jeu
class Game():
    def __init__(self):

        #definir si notre jeu a commencé
        self.is_playing = False
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.score = Score(game=Game)
        self.all_players.add(self.player)
        self.monster = Monster(self)
        self.all_monsters = pygame.sprite.Group()
        self.all_players.add(self.player)
        self.pressed = {}

    #pour relancer le jeu avec les monstres quand on meurt
    def start(self):
        self.is_playing = True
        self.spawn_monster()  # appel de la methode
        #self.spawn_monster()
        self.score.points = 0

    def game_over(self):
        #remettre le jeu à 0
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False


    def update(self, screen):
        # appliquer image du joueur
        screen.blit(self.player.image, self.player.rect)

        #afficher le score
        font = pygame.font.Font(None, 30)
        scores =font.render("Monster kill: " + str(self.score.points), True, (255, 255, 255))
        screen.blit(scores, (0, 0))



        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        # recuperer les projectiles du joueeurs
        for projectile in self.player.all_projectile:
            projectile.move()

        # recuperer les monstres du jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # appliquer les images projectiles
        self.player.all_projectile.draw(screen)

        # appliquer ensemble des images des monstres
        self.all_monsters.draw(screen)



        # verifier si joueuer va a gauche u droite

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()


    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster) #ajoute un monstre au groupe de monstres





