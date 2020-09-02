import random

from Player import Player
from DiceBag import DiceBag

class Game:
    def __init__(self):
        self.players = []
        self.numPlayers = 0
        self.diceBag = DiceBag()
        self.round = 0

    def createNewGame(self, numPlayers):
        self.players = [Player() for _ in range(numPlayers)]
        self.numPlayers = len(self.players)
        self.diceBag.initializeBag()
        self.round = 0

    def startGame(self):
        # Players should first create a character
        for player in self.players:
            player.pickCharacter()
        # Players should grab 6 dice from the bag, roll them, and place these dice as they like on their board.
        for player in self.players:
            startingDice = self.diceBag.drawDice(6)
            print('\n')
            player.placeInitialDice(startingDice)

    def doRound(self):
        # Grab dice from the dice bag, stored in an array with entries as:
        # (color, number)
        dice = self.diceBag.drawDice(self.numPlayers + 1)
        # Iterate through the list of players, selecting the first
        # player for the round, as appropriate
        playersInOrderList = self.players[self.round % self.numPlayers : self.numPlayers] \
                             + self.players[0 : self.round % self.numPlayers]
        for player in playersInOrderList:
            player.playerTurn(dice)
        # Increase the round tracker by 1
        self.round += 1


if __name__ == '__main__':
    game = Game()
    game.createNewGame(1)
    game.startGame()
    for i in range(5):
        game.doRound()
    