from ai import AI
from human import Human

class Game:
    def __init__(self):
        self.player_one = Human(2) #None
        self.player_two = AI(2) # None
    
    def rules(self):
        print('Scissors decapitate Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock, and as it always has, rock crushes scissors')
    
    def choose_game_mode(self):
        pass

    def game(self):
        while self.player_one.score > 0 and self.player_two.score > 0:
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            if self.player_one.gesture == self.player_two.gesture:
                print("its a tie, keep playing")
            if (self.player_one.gesture == "rock" and self.player_two.gesture == "scissors") or (self.player_one.gesture == "rock" and self.player_two.gesture == "lizard") or (self.player_one.gesture == "lizard" and self.player_two.gesture == "spock"):
                self.player_one.score -= 1

    def winner(self):   
        pass

    def run_game(self):
        self.rules()
        self.choose_game_mode()
        self.game()
        

        
        
        
