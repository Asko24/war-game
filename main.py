from cards import *

class Game:

    def __init__(self):
        self.player1 = ""
        self.player2 = ""
        self.game_deck = []
        self.game_started = False

    def register(self):
        # self.player1 = Player(input("Player 1 - Enter name: "))
        # self.player2 = Player(input("Player 2 - Enter name: "))
        self.player1 = Player("1_Jas") # for testing purposes
        self.player2 = Player("2_Agatka") # for testing purposes

    def prepare_hands(self):
        self.game_deck = Deck()
        self.game_deck.shuffle()

        for i in range (0, len(self.game_deck.cards)):
            if i % 2 == 0:
                self.player1.hand.append(self.game_deck.cards[i])
            else:
                self.player2.hand.append(self.game_deck.cards[i])

        #check if players hands are equal
        assert len(self.player1.hand)  == len(self.player1.hand) == int(len(self.game_deck.cards)/2), "players hands are not equal!"

    def play(self):
        while self.game_started is not False:
            if len(self.player1.hand) == 0 or len(self.player1.hand) == 0:
                self.end_game()
            else:
                self.player1.hand.pop() #test

    def start_game(self):
        print("♥ ♦ ♠ ♣ GAME STARTED! ♣ ♠ ♦ ♥")
        self.register()
        self.prepare_hands()
        self.game_started = True

    def end_game(self):
        self.game_started = False
        print("♥ ♦ ♠ ♣ GAME ENDED! ♣ ♠ ♦ ♥")
        if len(self.player1.hand) == 0 and len(self.player2.hand) != 0:
            print(f"{self.player2.name} has won!")
        elif len(self.player1.hand) != 0 and len(self.player2.hand) == 0:
            print(f"{self.player1.name} has won!")
        else:
            print("Something weird has happen, fix your code!")

########## TESTING AREA ###########

game1 = Game()
game1.start_game()
game1.play()
