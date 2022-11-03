from player import Player
import random
class AI(Player):
    def __init__(self, gesture):
        super().__init__(gesture)
    
    def ai_gesture(self):
        self.gesture = self.gestures_list
        ai_player = random.choice(self.gestures_list)

        print('AI played: '+ ai_player)