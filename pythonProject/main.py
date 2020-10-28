import pygame
import random
import math
from pygame import mixer


def play_again():
    #  Initialization
    pygame.init()

    #  Create screen
    screen = pygame.display.set_mode((1000, 800))  # (x, y)

    #  Title
    pygame.display.set_caption("The Journey")

    #  Game Icon (check at flaticon.com)
    icon = pygame.image.load("map.png")
    pygame.display.set_icon(icon)

    #  Background Music
    mixer.music.load("background_music.mp3")
    mixer.music.play(-1)

    #  Level
    level_font = pygame.font.Font("freesansbold.ttf", 30)
    character_level = 1
    level_x = 850
    level_y = 10

    def show_level(x, y):
        level = level_font.render("LVL : " + str(character_level), True, (100, 200, 100))
        screen.blit(level, (x, y))

    #  Score
    score_value = 0
    font = pygame.font.Font("freesansbold.ttf", 32)
    text_x = 400
    text_y = 10

    #  Game Over
    font_end = pygame.font.Font("freesansbold.ttf", 60)
    text_end_x = 330
    text_end_y = 300
    restart_x = 75
    restart_y = 400

    def end_game(x, y):
        game_over = font_end.render("Game Over!", True, (0, 0, 0))
        screen.blit(game_over, (x, y))

    def restart_leave(x, y):
        restart = font_end.render("Press R to restart or L to leave", True, (0, 0, 0))
        screen.blit(restart, (x, y))

    #  Best Score
    # best_score = 0

    # def is_better_score(x, y):
    #    if y > x:
    #        return y
    #    return x

    #  Level up
    level_needed = [10, 20, 50, 75, 100]
    normal_speed = 1.5

    def show_score(x, y):
        score = font.render("Your Score : " + str(score_value), True, (255, 255, 255))  # True is for antialiasing
        screen.blit(score, (x, y))

    #  Life
    life_img = []
    life_x = []
    life_y = []
    nbr_life = 3
    for i in range(nbr_life):
        life_img.append(pygame.image.load("coeur.png"))
        life_x.append(10 + (35 * i))
        life_y.append(5)

    def life(x, y):
        for lifes in range(nbr_life):
            screen.blit(life_img[lifes], (x, y))

    #  Background
    background = pygame.image.load("Sea.jpg")

    # Function generate random number
    def rand_number(nbr):
        return random.randint(50, nbr)

    #  Creating main Character and its position
    character_img = pygame.image.load("octopus.png")
    character_x = 500
    character_y = 350
    character_change_x = 0
    character_change_y = 0

    #  Adding meduse
    enemy_meduse_img = pygame.image.load("meduse.png")
    meduse_x = random.choice([0, 1000])
    meduse_y = rand_number(800)
    meduse_change_x = 0.5
    meduse_change_y = 0.5

    #  Adding shark
    enemy_shark_img = pygame.image.load("shark.png")
    shark_x = 0
    shark_y = rand_number(850)
    shark_change_x = 1

    #  Adding enemies crabs
    enemy_img = []
    enemy_x = []
    enemy_y = []
    enemy_change_y = []
    enemy_change_x = []
    nbr_enemies = 15

    for i in range(nbr_enemies):
        enemy_img.append(pygame.image.load("crab.png"))
        enemy_x.append(random.choice([0, 1000]))
        enemy_y.append(rand_number(800))
        enemy_change_y.append(random.choice([-0.3, -0.5, -0.7, -1]))
        enemy_change_x.append(random.choice([-0.3, -0.5, -0.7, -1]))

    #  Display enemies and character
    def enemy(x, y):
        for number in range(nbr_enemies):
            screen.blit(enemy_img[number], (int(x), int(y)))

    def meduse(x, y):
        screen.blit(enemy_meduse_img, (int(x), int(y)))

    def shark(x, y):
        screen.blit(enemy_shark_img, (int(x), int(y)))

    def player(x, y):
        screen.blit(character_img, (int(x), int(y)))

    #  Collisions detection
    def collision(x1, y1, x2, y2):
        distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
        if distance <= 35:
            return True
        return False

    #  Collision Shark
    def collision_shark(x1, y1, x2, y2):
        distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
        if distance <= 60:
            return True
        return False

    #  Collision Meduse
    def collision_meduse(x1, y1, x2, y2):
        distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
        if distance <= 60:
            return True
        return False

    #  Loop until exit is pressed
    running = True
    while running:

        #  Background
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # checking key pressed for actions
        # noinspection PyUnboundLocalVariable
        if event.type == pygame.KEYDOWN:  # KEYDOWN = pressing any key
            if event.key == pygame.K_UP:
                character_change_y = -normal_speed
            if event.key == pygame.K_DOWN:
                character_change_y = normal_speed
            if event.key == pygame.K_LEFT:
                character_change_x = -normal_speed
            if event.key == pygame.K_RIGHT:
                character_change_x = normal_speed
        if event.type == pygame.KEYUP:  # KEYUP = releasing a key
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_change_x = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                character_change_y = 0

        # Setting map boundaries
        if character_x <= 0:
            character_x = 0
        elif character_x >= 935:
            character_x = 935
        if character_y <= 0:
            character_y = 0
        elif character_y >= 735:
            character_y = 735

        for i in range(nbr_enemies):
            enemy_x[i] += enemy_change_x[i]
            enemy_y[i] += enemy_change_y[i]

        character_x += character_change_x
        character_y += character_change_y

        # Bouncing enemies when they touch boundaries
        for i in range(nbr_enemies):
            if enemy_y[i] >= 780:
                enemy_y[i] = 780
                enemy_change_y[i] *= -1
                enemy_change_x[i] *= random.choice([-1, 1])
            elif enemy_y[i] <= 0:
                enemy_y[i] = 0
                enemy_change_y[i] *= -1
                enemy_change_x[i] *= random.choice([-1, 1])
            if enemy_x[i] >= 970:
                enemy_x[i] = 970
                enemy_change_x[i] *= -1
                enemy_change_y[i] *= random.choice([-1, 1])
            elif enemy_x[i] <= 0:
                enemy_x[i] = 0
                enemy_change_x[i] *= -1
                enemy_change_y[i] *= random.choice([-1, 1])

        #  Spawning enemies crabs
        for i in range(nbr_enemies):
            enemy(enemy_x[i], enemy_y[i])

        #  Collisions
        for i in range(nbr_enemies):
            is_collision = collision(enemy_x[i], enemy_y[i], character_x + 20, character_y + 20)
            if is_collision:
                enemy_y[i] = rand_number(775)
                enemy_x[i] = random.choice([0, 1000])
                score_value += 1
                killing_crab = mixer.Sound("Eating.wav")
                killing_crab.play()

        is_collision_shark = collision_shark(shark_x + 150, shark_y + 30, character_x, character_y)
        if is_collision_shark:
            character_x = 0
            character_y = 0
            nbr_life -= 1
            shark_bite = mixer.Sound("Bite.wav")
            shark_bite.play()

        is_collision_meduse = collision_meduse(meduse_x, meduse_y + 20, character_x, character_y)
        if is_collision_meduse:
            character_x = 0
            character_y = 0
            nbr_life -= 1
            meduse_shock = mixer.Sound("Shock.wav")
            meduse_shock.play()

        #  Meduse movement
        meduse_x += meduse_change_x
        meduse_y += meduse_change_y
        if meduse_x >= 1100 or meduse_x <= -100:
            meduse_change_x *= -1
            meduse_change_y *= random.choice([-1, 1])
            meduse_y = rand_number(750)
        elif meduse_y >= 850 or meduse_y <= -100:
            meduse_change_y *= -1
            meduse_change_x *= random.choice([-1, 1])
            meduse_x = rand_number(700)

        #  Shark movement
        shark_x += shark_change_x
        if shark_x >= 1000:
            shark_x = -600
            shark_y = rand_number(750)

        # spawning character and lifes
        for i in range(nbr_life):
            life(life_x[i], life_y[i])
        player(character_x, character_y)
        show_score(text_x, text_y)

        #  Lvl up
        for i in level_needed:
            if score_value == i:
                character_level += 1
                level_up = mixer.Sound("levelup.wav")
                level_up.play()
                level_needed.remove(i)
                if score_value == 10:
                    character_img = pygame.image.load("poulpe10.png")
                    nbr_enemies = 10
                    shark_change_x = 2.5
                    meduse_change_x = 1
                    meduse_change_y = 1
                if score_value == 20:
                    character_img = pygame.image.load("poulpe20.png")
                if score_value == 50:
                    character_img = pygame.image.load("poulpe50.png")
                    nbr_enemies = 5
                if score_value == 75:
                    character_img = pygame.image.load("poulpe75.png")
                if score_value == 100:
                    character_img = pygame.image.load("poulpe100.png")

        # Game Over
        if nbr_life <= 0:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    play_again()
                elif event.key == pygame.K_l:
                    pygame.quit()
            nbr_enemies = 0
            end_game(text_end_x, text_end_y)
            restart_leave(restart_x, restart_y)
        if nbr_life > 0:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    pygame.quit()

        #  Showing level
        show_level(level_x, level_y)

        #  Spawn creatures
        shark(shark_x, shark_y)
        meduse(meduse_x, meduse_y)

        pygame.display.update()


play_again()
