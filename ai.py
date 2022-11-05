from player import Player
import random
class AI(Player):
    def __init__(self, score):
        super().__init__(score)
    
    def choose_gesture(self):
        self.gesture = random.randint(self.gestures_list)
        print('AI played: '+ self.gesture)
