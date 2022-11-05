from player import Player

class Human(Player):
    def __init__(self, score):
        super().__init__(score)

    
    def choose_gesture(self):
        user_input = int(input('Enter 0 to select "Rock", 1 to select "Paper", 2 to select "Scissors", 3 to select "Lizard", or 4 to select "Spock"'))
        self.gesture = self.gestures_list[user_input]
        print('You played: ' + self.gesture)
        