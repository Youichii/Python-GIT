import pygame
from game import Game
from player import Player



pygame.init()

# generer la fenetre du jeu
pygame.display.set_caption("Comet fall game- Player: ")
screen = pygame.display.set_mode((1080, 620))
background = pygame.image.load('assets/bg.jpg')

#charger le joueuer
player = Player()

#charger jeu
game = Game()


running = True

#boucle tant que cette condition est vraie

while running:
    #appliquer arriere plan
    screen.blit(background, (0,-400))

    #appliquer image du joueur
    screen.blit(game.player.image, game.player.rect)

    #recuperer les projectiles du joueeurs
    for projectile in game.player.all_projectile:
        projectile.move()

    #recuperer les monstres du jeu
    for monster in game.all_monsters:
        monster.forward()

    #appliquer les images projectiles
    game.player.all_projectile.draw(screen)

    #appliquer ensemble des images des monstres
    game.all_monsters.draw(screen)

    #verifier si joueuer va a gauche u droite

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()


    #mettre à jour l'ecran
    pygame.display.flip()
    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # verifier que l'evenet est fermeture de fene
        if event.type == pygame.QUIT:
            running  = False
            pygame.quit()
            print("Fermeture. Aurevoir " )

        # si joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detecter si la touche espace est enclenchée
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
        elif event.type == pygame.KEYUP:  #touche plus utilisée
            game.pressed[event.key] = False


