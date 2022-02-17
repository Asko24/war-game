import random


class Card:

    def __init__(self, type, value):
        self.type = type
        self.value = value

    def show(self):
        return f"{self.value} {self.type}"


class Deck:

    def __init__(self):
        self.cards = []
        # self.possible_types = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.possible_types = ["♥", "♦", "♠", "♣"]
        self.build_deck()

    def build_deck(self):
        for type in self.possible_types:
            for value in range(1,14):
                self.cards.append(Card(type, value))

    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        for card in range(len(self.cards)-1, 0, -1):
            temp = random.randint(0, card)
            self.cards[card], self.cards[temp] = self.cards[temp], self.cards[card]

    def draw(self):
        return self.cards.pop()


class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []

    def take(self, deck):
        self.hand.append(deck.draw())
        return self

    def discard(self):
        return self.hand.pop()

    def show_hand(self):
        for card in self.hand:
            card.show()
