import random
from players import User

class Deck:
    deck: list = []
    suits: list = ["♠", "♡", "♢", "♣"]
    face_cards: list = ["A", "K", "Q", "J"]
    
    river: list = []
    hands: list = ["Royal Flush",
                   "Straight Flush",
                   "Four of a Kind",
                   "Full House",
                   "Flush",
                   "Straight",
                   "Three of a Kind",
                   "Two Pair",
                   "Pair",
                   "High Card"]

    pot = 0
    
    def __init__(self, cardAmount=54) -> None:
        self.cardAmount = cardAmount
    
    def CreateDeck(self):
        # Add the regular number cards
        for i in range(2, 10+1, 1):
            for x in range(len(self.face_cards)):
                self.deck.append(str(i) + self.suits[x-1])
        # Add the face cards
        for i in range(len(self.face_cards)):
            for x in range(0, 4, 1):
                self.deck.append(str(self.face_cards[i]) + self.suits[x-1])
    
    # Distribute cards to a recipient, can be river or players.
    def DistributeCards(self, recipient: User, cards):
        # Give a recipient [cards] cards from Deck.deck
        for _ in range(cards):
            randomCard = random.choice(self.deck)
            recipient.ReceiveCards(randomCard)
            self.deck.remove(randomCard)
    
    def DistributeRiver(self):
        for _ in range(3):
            randomCard = random.choice(self.deck)
            self.river.append(randomCard)
            self.deck.remove(randomCard)
            


