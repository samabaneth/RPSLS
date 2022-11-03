from player import Player

class Human(Player):
    def __init__(self, gesture):
        super().__init__(gesture)

    
    def throw_gesture(self):
        player = input('Pick: rock, paper, scissors, lizard, spock')