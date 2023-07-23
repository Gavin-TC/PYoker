import time

class User:
    chips = 100
    bet = 0
    cards: list = []

    deckObj = None

    def __init__(self, deckObj):
        self.deckObj = deckObj

    def ReceiveCard(self, card):
        self.cards.append(card)

    def Check(self):
        pass

    def Call(self, bet):
        if self.chips - bet < 0:
            difference = (self.chips - bet) + bet
            self.chips -= difference
        else:
            self.bet += bet
            self.chips -= bet

    def Raise(self, raiseAmount):
        pass

    def Fold(self):
        pass

class AIPlayer(User):
    '''
    Riskiness is a value between 0-100 which will determine how risky
    this AI will play. 50 is the default value.
    '''
    riskiness = 50

    # Is it the AI's current turn?
    turn = False

    state: str
    states: list = ["All-In", "Call", "Bet", "Raise", "Fold", "Waiting"]

    currentHand: str = None

    def __init__(self, riskiness = 50):
        self.riskiness = 50
        self.state = self.states[-1]

    '''
    The AI will make a decision based on the river
    and it's options (call, check, raise, fold)
    '''
    def Think(self, river: list, options: list):
        self.EvaluateHand()

        # Sleep 1 second so decision isn't instant.
        time.sleep(1)

    def EvaluateHand(self):
        pass


class Player(User):
    pass