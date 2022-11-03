from player import Player

class Human(Player):
    def __init__(self, score):
        super().__init__(self)

    
    def throw_gesture(self):
        self.player = input('Pick:' + self.gestures_list)

        