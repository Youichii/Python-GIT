import pygame

class Score:
    def __init__(self, game):
        self.points = 0
        self.your_points = []
        #self.player = player
        self.game = game
        #self.monster = monster



    def store_score(self):
        self.your_points += self.game.score.points
        print(self.your_points)

    """def update_score(self):

        #quand le jeu commence
        if self.game.start():
            self.points = 0
        #si le monstre n'a plus de point de vie
        elif self.game.monster.damage(self) :
            self.points += 1
            self.your_points += self.points
        #si le joueur n'a plus de point de vie
        elif self.game.player.damage():
            self.points = 0
    """



