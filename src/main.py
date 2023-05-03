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
    
    if game.get_word_guessed():
        print (Fore.YELLOW + f"\n[>] Congratulations! You have guessed the correct word in {6 - player.get_remaining_guesses()} guesses!" + Fore.WHITE)
    
    else:
        print (Fore.YELLOW + f"\n[>] Sorry! You ran out of guesses. The correct word was {game.get_game_word()}." + Fore.WHITE)


if __name__ == "__main__":
    main()