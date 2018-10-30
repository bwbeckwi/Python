class Game:
    def __init__(self, newPlayerName):
        self.playerName = newPlayerName
        self.playerHand = "NA"
        self.botHand = "NA"
        self.winner = "No winner yet"
        print("New instance of game class for " + self.playerName)

    def runGame(self):
        if ((self.playerHand == 'rock' or self.playerHand == 'Rock') and self.botHand == 1):
            self.winner = 'You win'
        elif ((self.playerHand == 'rock' or self.playerHand == 'Rock') and self.botHand == 2):
            self.winner = 'You tie.'
        elif ((self.playerHand == 'rock' or self.playerHand == 'Rock') and self.botHand == 3):
            self.winner = 'You lose.'
        elif ((self.playerHand == 'paper' or self.playerHand == 'Paper') and self.botHand == 1):
            self.winner = 'You lose.'
        elif ((self.playerHand == 'paper' or self.playerHand == 'Paper') and self.botHand == 2):
            self.winner = 'You win!'
        elif ((self.playerHand == 'paper' or self.playerHand == 'Paper') and self.botHand == 3):
            self.winner = 'You tie.'
        elif ((self.playerHand == 'scissors' or self.playerHand == 'Scissors') and self.botHand == 1):
            self.winner = 'You tie.'
        elif ((self.playerHand == 'scissors' or self.playerHand == 'Scissors') and self.botHand == 2):
            self.winner = 'You lose.'
        elif ((self.playerHand == 'scissors' or self.playerHand == 'Scissors') and self.botHand == 3):
            self.winner = 'You win!'
        else:
            self.winner = 'INVALID input, try again'

def main():
    myGame = Game('Kevin')

    print(myGame.playerName)
    print(myGame.playerHand)
    print(myGame.botHand)
    print(myGame.winner)

    myGame.playerHand = 'paper'
    myGame.botHand = 1 #Scissors
    myGame.runGame()
    print(myGame.winner)

    otherGame = Game('Zibzo')
    otherGame.runGame()
    print(otherGame.winner)


main()