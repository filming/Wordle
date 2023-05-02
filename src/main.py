from Game import Game
from Player import Player

from colorama import init, Fore
init()

def main():
    game = Game()
    game.setup()
    game.new_game()

    player = Player(game)

    print (Fore.LIGHTCYAN_EX + "[*]" + Fore.MAGENTA + " Welcome To Wordle! " + Fore.LIGHTCYAN_EX + "[*]" + Fore.WHITE)
    
    while (player.get_remaining_guesses() > 0) and (game.get_game_status()):
        guess = input(Fore.LIGHTCYAN_EX + "\n[?] Enter a word: " + Fore.WHITE).lower()

        if len(guess) != 5:
            print(Fore.RED + "[!] Your guess must be exactly 5 characters long!\n" + Fore.WHITE)

        elif not guess.isalpha():
            print(Fore.RED + "[!] Your guess must only contain alphabetical characters!\n" + Fore.WHITE)

        else:   
            player.make_guess(guess)
            game.gameboard(player.get_player_guesses())


if __name__ == "__main__":
    main()