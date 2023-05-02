from random import choice


class Game():
    def __init__(self):
        self.wordlist = []
        self.game_word = ""

    def setup(self):
        wordlist = []
        with open("../../storage/wordlist.txt", encoding="utf-8") as f:
            for line in f.readlines():
                line = line.strip()
                if line: wordlist.append(line)

        self.wordlist = wordlist
    
    def new_game(self):
        game_word = choice(self.wordlist)
        self.game_word = game_word

    


        
        
        




