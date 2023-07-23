import time
import os
from deck import Deck
from players import AIPlayer, Player
from screenRenderer import ScreenRenderer

def main():    
    screen = ScreenRenderer(15, 10)
    
    deck = Deck()
    deck.CreateDeck()
    
    players = [AIPlayer() for _ in range(4)]
    players.append(Player(deck))

    deck.DistributeRiver()
    print(deck.river)
    
    UPS = 10
    FPS = 10
    updateTime = 1 / UPS
    renderTime = 1 / FPS
    
    uDeltaTime = 0
    rDeltaTime = 0
    start_time = 0
    
    running = True
    while running:       
        current_time = time.time()
        # Update deltaTime
        uDeltaTime += (current_time - start_time)
        # Render deltaTime
        rDeltaTime += (current_time - start_time)
        start_time = current_time
        
        os.system("CLS")
        
        if uDeltaTime >= updateTime:
            uDeltaTime -= updateTime
        
        if rDeltaTime >= renderTime:
            #screen.Render()
            rDeltaTime -= renderTime

main()