from player import Player
import random
class AI(Player):
    def __init__(self, score) -> None:
        super().__init__(score)
    
    def ai_gesture(self):
        self.gesture = self.gestures_list
        self.ai_player = random.choice(self.gestures_list)

        print('AI played: '+ self.ai_player)
