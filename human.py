from player import Player

class Human(Player):
    def __init__(self, gesture):
        super().__init__(gesture)
        self.score = 3
    
    def throw_gesture(self, gesture):
        pass