from cards import *

class Game:

    def __init__(self):
        self.player1 = ""
        self.player2 = ""
        self.start_game()

    def register(self):
        self.player1 = Player(input("Player 1 - Enter name: "))
        self.player2 = Player(input("Player 2 - Enter name: "))

    def start_game(self):
        self.register()

game1 = Game()