from deck import Deck
from players import *

def main():
    deck = Deck()
    deck.CreateDeck()

    deck.DistributeCards(deck.river)

main()