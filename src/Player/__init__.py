

class Player():
    def __init__(self, initGame):
        self.game = initGame
        self.remaining_guesses = 6
        self.player_guesses = []
    
    def get_remaining_guesses(self):
        return self.remaining_guesses
    
    def get_player_guesses(self):
        return self.player_guesses
    
    def make_guess(self, guess):
        response = self.game.check_guess(guess)
        self.player_guesses.append(response)
        self.remaining_guesses -= 1
