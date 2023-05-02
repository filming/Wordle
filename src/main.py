from Game import Game
from Player import Player

from colorama import init, Fore
init()

def main():
    game = Game()
    game.setup()
    game.new_game()

    player = Player(game)

    print ("[*] Welcome To Wordle! [*]")

    while (player.get_remaining_guesses() > 0) and (game.get_game_status()):
        guess = input("\n[?] Enter a word: ").lower()

        if len(guess) != 5:
            print(Fore.RED + "[!] Your guess must be exactly 5 characters long!\n" + Fore.WHITE)

        elif not guess.isalpha():
            print(Fore.RED + "[!] Your guess must only contain alphabetical characters!\n" + Fore.WHITE)

        else:   
            player.make_guess(guess)
            game.gameboard(player.get_player_guesses())


if __name__ == "__main__":
    main()