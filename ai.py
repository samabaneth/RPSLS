from player import Player
import random
class AI(Player):
    def __init__(self, gesture):
        super().__init__(gesture)
    
    def ai_gesture(self):
        gestures_list = ["rock", "paper", "scissors", "lizard", "spock"]