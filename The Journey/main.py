import pygame
import math
from game import Game
from player import Player
from monster import Monster



def begin_game():
    psdo = input("Entrez un pseudo:")
    if psdo:

        pygame.init()

        # generer la fenetre du jeu
        pygame.display.set_caption("SPACE GAME- Player: ")
        screen = pygame.display.set_mode((1080, 620))
        background = pygame.image.load('im/bg1.jpg')

        #importer et charger la banière
        banner = pygame.image.load('im/project.png')
        banner = pygame.transform.scale(banner, (250, 250))
        banner_rect = banner.get_rect()
        banner_rect.x = screen.get_width()/2.77 #math.ceil
        banner_rect.y =screen.get_height() / 4.7

        #importer et charger un bouton pour lancer la partie
        play_button = pygame.image.load('im/button.png')
        play_button = pygame.transform.scale(play_button, (400, 150))
        play_button_rect = play_button.get_rect()
        play_button_rect.x = screen.get_width() / 3.33
        play_button_rect.y = screen.get_height() / 2


        #charger le joueuer
        player = Player

        #charger jeu
        game = Game()

        #charger monstre
        monster = Monster





        running = True

        #boucle tant que cette condition est vraie

        while running:
            #appliquer arriere plan
            screen.blit(background, (0,-400))

            #verifier si le jeu a commencé
            if game.is_playing:
                #declencher les instructions
                game.update(screen)
            #verifier si le jeu n'a pas commencé
            else:
                #ajouter l'ecran de bienvenue
                screen.blit(banner, banner_rect)
                screen.blit(play_button, play_button_rect)


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
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    #verifier si la souris est en collision avec le bouton joué
                    if play_button_rect.collidepoint(event.pos):
                        #mettre le jeu en mode lancé
                        game.start()

print(begin_game())
