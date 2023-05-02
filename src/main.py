from Game import Game



def main():
    game = Game()
    game.setup()
    game.new_game()


    guess = input("[?] Enter a word: ")
    response = game.make_guess(guess)





if __name__ == "__main__":
    main()