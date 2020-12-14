import pygame
from game import Game
import data_base


def begin_game():
    psdo = input("Entrez un pseudo:")

    pygame.init()

    # generer la fenetre du jeu
    pygame.display.set_caption("SPACE GAME- Player: ")
    screen = pygame.display.set_mode((1080, 620))
    background = pygame.image.load('im/bg1.jpg')

    # importer et charger la banière
    banner = pygame.image.load('im/project.png')
    banner = pygame.transform.scale(banner, (250, 250))
    banner_rect = banner.get_rect()
    banner_rect.x = screen.get_width() / 2.65  # math.ceil
    banner_rect.y = screen.get_height() / 4.7

    # importer et charger un bouton pour lancer la partie
    play_button = pygame.image.load('im/button.png')
    play_button = pygame.transform.scale(play_button, (400, 150))
    play_button_rect = play_button.get_rect()
    play_button_rect.x = screen.get_width() / 3.25
    play_button_rect.y = screen.get_height() / 2

    # importer et charger les 2 boutons restart
    save_button = pygame.image.load('im/save.png')
    save_button_rect = save_button.get_rect()
    save_button_rect.x = screen.get_width() / 1.3
    save_button_rect.y = screen.get_height() / 1.5

    rest_button = pygame.image.load('im/arrows.png')
    rest_button_rect = rest_button.get_rect()
    rest_button_rect.x = screen.get_width() / 5.3
    rest_button_rect.y = screen.get_height() / 1.5

    # charger le joueuer

    # charger jeu
    game = Game()

    running = True

    # boucle tant que cette condition est vraie

    while running:
        # appliquer arriere plan
        screen.blit(background, (0, -400))

        # verifier si le jeu a commencé
        if game.is_playing and game.is_playing != "transition":
            # declencher les instructions
            game.update(screen)

        # verifier si le jeu n'a pas commencé

        elif game.is_playing == "transition":
            font = pygame.font.Font(None, 30)
            save_score = font.render("Save score & Restart ?", True, (255, 255, 255))
            just_retry = font.render("Don't save & Restart ?", True, (255, 255, 255))
            current_score = pygame.font.Font(None, 36).render("You scored " + str(game.score.local_score) + " points", True, (255, 255, 255))
            screen.blit(current_score, (410, 50))
            screen.blit(just_retry, (125, 485))
            screen.blit(save_score, (750, 485))
            screen.blit(banner, banner_rect)
            screen.blit(rest_button, rest_button_rect)
            screen.blit(save_button, save_button_rect)

        else:
            # ajouter l'ecran de bienvenue
            screen.blit(banner, banner_rect)
            screen.blit(play_button, play_button_rect)

        # mettre à jour l'ecran
        pygame.display.flip()

        # si le joueur ferme cette fenetre
        for event in pygame.event.get():
            # verifier que l'evenet est fermeture de fene
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                print("Fermeture. Aurevoir ")
                print("Vous avez: " + str(game.score.best_score) + " points")
                # print(score.store_score())

            # si joueur lache une touche du clavier
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True

                # detecter si la touche espace est enclenchée
                if event.key == pygame.K_SPACE:
                    game.player.launch_projectile()
            elif event.type == pygame.KEYUP:  # touche plus utilisée
                game.pressed[event.key] = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # verifier si la souris est en collision avec le bouton joué
                if play_button_rect.collidepoint(event.pos) and not game.is_playing:
                    # mettre le jeu en mode lancé
                    game.start()
                elif rest_button_rect.collidepoint(event.pos) and game.is_playing == "transition":
                    game.start()
                elif save_button_rect.collidepoint(event.pos) and game.is_playing == "transition":
                    game.start()
                    data_base.save_to_db(psdo, game.score.local_score)


begin_game()
