from cards import *


class Game:

    def __init__(self):
        self.player1 = ""
        self.player2 = ""
        self.game_deck = []
        self.game_started = False
        self.player1_table = []
        self.player2_table = []
        self.moves_counter = 0
        self.wars_counter = 0

    def register(self):
        self.player1 = Player(input("Player 1 - Enter name: "))
        self.player2 = Player(input("Player 2 - Enter name: "))

    def prepare_hands(self):
        self.game_deck = Deck()
        self.game_deck.shuffle()

        for i in range(0, len(self.game_deck.cards)):
            if i % 2 == 0:
                self.player1.hand.append(self.game_deck.cards[i])
            else:
                self.player2.hand.append(self.game_deck.cards[i])
        # check if players hands are equal
        assert len(self.player1.hand) == len(self.player1.hand) == int(len(self.game_deck.cards)/2), "players hands are not equal!"

    def play(self):
        while self.game_started is not False:
            self.moves_counter += 1
            if len(self.player1.hand) == 0 or len(self.player2.hand) == 0:
                self.end_game()
            else:
                self.war()

    def war(self):
        if len(self.player1.hand) > 0 and len(self.player2.hand) > 0:
            self.player1_table.append(self.player1.discard())
            self.player2_table.append(self.player2.discard())

        print(f"Cards on the table {len(self.player1_table)} {len(self.player2_table)}")
        print(f"Cards left on hands {len(self.player1.hand)} {len(self.player2.hand)}")
        print(self.player1_table[-1].value, self.player2_table[-1].value)

        if self.player1_table[-1].value == self.player2_table[-1].value:
            print("--- WAR! ---")
            self.wars_counter += 1
            # When one of the players has not enough cards to continue the war
            if len(self.player1.hand) <= 1:
                print(f"{self.player1.name} has not enough cards to continue the war!\n")
                self.player2_table += self.player1_table
                for card in range(len(self.player2_table) - 1, -1, -1):
                    self.player2.hand = [self.player2_table[card]] + self.player2.hand
                self.player1_table = []
                self.player2_table = []
            elif len(self.player2.hand) <= 1:
                print(f"{self.player2.name} has not enough cards to continue the war!\n")
                self.player1_table += self.player2_table
                for card in range(len(self.player1_table) - 1, -1, -1):
                    self.player1.hand = [self.player1_table[card]] + self.player1.hand
                self.player1_table = []
                self.player2_table = []
            else:
                # Add additional card
                self.player1_table.append(self.player1.discard())
                self.player2_table.append(self.player2.discard())
                # Continue the war!
                self.war()

        elif self.player1_table[-1].value > self.player2_table[-1].value:
            print(f">>> {self.player1.name} wins!\n")
            self.player1_table += self.player2_table
            for card in range(len(self.player1_table)-1, -1, -1):
                self.player1.hand = [self.player1_table[card]] + self.player1.hand
            self.player1_table = []
            self.player2_table = []

        elif self.player2_table[-1].value > self.player1_table[-1].value:
            print(f">>> {self.player2.name} wins!\n")
            self.player2_table += self.player1_table
            for card in range(len(self.player2_table) - 1, -1, -1):
                self.player2.hand = [self.player2_table[card]] + self.player2.hand
            self.player1_table = []
            self.player2_table = []

    def start_game(self):
        print("♥ ♦ ♠ ♣ GAME STARTED! ♣ ♠ ♦ ♥")
        self.register()
        self.prepare_hands()
        self.game_started = True
        self.play()

    def end_game(self):
        self.game_started = False
        print(f"♥ ♦ ♠ ♣ GAME ENDED! ♣ ♠ ♦ ♥")
        print(f"Cards left | {self.player1.name}: {len(self.player1.hand)}  {self.player2.name}: {len(self.player2.hand)}")
        if len(self.player1.hand) == 0 and len(self.player2.hand) == len(self.game_deck.cards):
            print(f"{self.player2.name} has won the game!")
        elif len(self.player1.hand) == len(self.game_deck.cards) and len(self.player2.hand) == 0:
            print(f"{self.player1.name} has won the game!")
        else:
            print("Something weird has happen, fix your code!")
        print(f"(game ended with {self.moves_counter} moves | there were {self.wars_counter} wars!)")


# TESTING AREA
testgame = Game()
testgame.start_game()
