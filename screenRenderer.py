class ScreenRenderer:
    screenBuffer: list
    
    def __init__(self, width, height) -> None:
        self.screenBuffer = [['.' for _ in range(width)] for _ in range (height)]
    
    def Render(self):
        for x in range(len(self.screenBuffer)):
            for y in range(len(self.screenBuffer[0])):
                print(self.screenBuffer[x][y], end='')
            print()