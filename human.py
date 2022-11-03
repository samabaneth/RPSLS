from player import Player

class Human(Player):
    def __init__(self, score):
        super().__init__(self)

    
    def choose_gesture(self):

        user_input = int(input('Enter 0 to select "Rock", 1 to select "Paper" ect...  '))
        self.gesture = self.gestures_list[user_input]
        