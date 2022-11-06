from ai import AI
from human import Human

class Game:
    def __init__(self):
        self.player_one = AI(2) or Human(2)
        self.player_two = AI(2) or Human(2)
    
    def rules(self):
        print('\nWelcome to the game, here are the rules: Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock, and as it always has, rock crushes scissors.\n')
    
    def choose_game_mode(self):
        user_input = input('Enter 1 for one player, 2 for two players, or 3 to spectate')
        if user_input == '1':
            self.player_one = Human(2)
            self.player_two = AI(2)
            print('you chose single player mode')
        elif user_input == '2':
            self.player_one == Human(2)
            self.player_two == Human(2)
            print('you chose two player mode')
        elif user_input == '3':
            self.player_one == AI(2)
            self.player_two == AI(2)
            print('you chose to spectate')     

    def game(self):
        while self.player_one.score > 0 and self.player_two.score > 0:
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            if self.player_one.gesture == self.player_two.gesture:
                print("its a tie, keep playing")
            elif (self.player_one.gesture == "rock" and self.player_two.gesture == "scissors") or (self.player_one.gesture == "rock" and self.player_two.gesture == "lizard") or (self.player_one.gesture == "lizard" and self.player_two.gesture == "spock") or (self.player_one.gesture == "scissors" and self.player_two.gesture == "paper") or (self.player_one.gesture == "paper" and self.player_two.gesture == "rock") or (self.player_one.gesture == "lizard" and self.player_two.gesture == "spock") or (self.player_one.gesture == "spock" and self.player_two.gesture == "scissors") or (self.player_one.gesture == "scissors" and self.player_two.gesture == "lizard") or (self.player_one.gesture == "lizard" and self.player_two.gesture == "paper") or (self.player_one.gesture == "paper" and self.player_two.gesture == "spock") or (self.player_one.gesture == "spock" and self.player_two.gesture == "rock"):
                self.player_two.score -= 1
                print('\nPlayer one, you win this round!\n')
            else:
                self.player_one.score -= 1
                print('\nPlayer two, you win this round!\n')

    def winner(self):   
        if self.player_one.score <= 0:
            print('\nSorry, you lost.\n')
        if self.player_two.score <= 0:
            print('\nCongratulations, you win the game!\n')

    def run_game(self):
        self.rules()
        self.choose_game_mode()
        self.game()
        self.winner()
        

        
        
        
