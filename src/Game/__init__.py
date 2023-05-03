from random import choice
from colorama import init, Fore
init()

class Game():
    def __init__(self):
        self.wordlist = []
        self.game_word = ""
        self.word_guessed = False
        self.game_status = True

    def setup(self):
        wordlist = []
        with open("../storage/wordlist.txt", encoding="utf-8") as f:
            for line in f.readlines():
                line = line.strip()
                if line: wordlist.append(line)

        self.wordlist = wordlist
    
    def new_game(self):
        game_word = choice(self.wordlist)
        self.game_word = game_word
        print ("Game Word:", game_word)
    
    def get_word_guessed(self):
        return self.word_guessed

    def get_game_status(self):
        return self.game_status
    
    def get_game_word(self):
        return self.game_word
    
    def check_guess(self, guess):
        response = ""

        if guess == self.game_word:
            self.game_status = False
            self.word_guessed = True

        game_word_char_occurrences = {}
        for char in self.game_word:
            if char in game_word_char_occurrences:
                game_word_char_occurrences[char] += 1
            else:
                game_word_char_occurrences[char] = 1

        for i in range (len(guess)):
            if guess[i] not in game_word_char_occurrences:
                response += guess[i] + "R,"
            
            else:
                if (guess[i] == self.game_word[i]) and (game_word_char_occurrences[guess[i]] > 0):
                    response += guess[i] + "G,"
                    game_word_char_occurrences[guess[i]] -= 1
                
                elif game_word_char_occurrences[guess[i]] > 0:
                    response += guess[i] + "Y,"
                    game_word_char_occurrences[guess[i]] -= 1
            
                else:
                    response += guess[i] + "R,"
        
        response = response[:-1]

        return response


    
    def format_response(self, response):
        formatted_response = Fore.WHITE + "" + Fore.WHITE
        
        response_pairs = response.split(",")

        for pair in response_pairs:
            if pair[1] == "G":
                formatted_response += Fore.GREEN + pair[0] + Fore.WHITE

            elif pair[1] == "Y":
                formatted_response += Fore.YELLOW + pair[0] + Fore.WHITE
            
            elif pair[1] == "R":
                formatted_response += Fore.RED + pair[0] + Fore.WHITE
        
        return formatted_response
    
    def gameboard(self, player_guesses):
        gameboard_text = []

        for guess in player_guesses:
            formatted_guess = ""

            guess_pairs = guess.split(",")
            for pair in guess_pairs:
                if pair[1] == "G":
                    formatted_guess += Fore.GREEN + pair[0] + Fore.WHITE + " "

                elif pair[1] == "Y":
                    formatted_guess += Fore.YELLOW + pair[0] + Fore.WHITE + " "
                
                elif pair[1] == "R":
                    formatted_guess += Fore.RED + pair[0] + Fore.WHITE + " "
            
            gameboard_text.append(formatted_guess)

        gameboard = Fore.MAGENTA + "}==========={" + Fore.WHITE

        for text in gameboard_text:
            gameboard += Fore.MAGENTA + f"\n| {text}" + Fore.MAGENTA + "|" + Fore.WHITE
        
        gameboard += Fore.MAGENTA + "\n}==========={" + Fore.WHITE

        print (gameboard)


