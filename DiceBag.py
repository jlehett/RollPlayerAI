import random

class DiceBag:
    def __init__(self):
        self.bag = []

    def initializeBag(self):
        self.bag = ['white' for i in range(10)]     \
                   + ['black' for i in range(10)]   \
                   + ['green' for i in range(10)]   \
                   + ['blue' for i in range(10)]    \
                   + ['red' for i in range(10)]     \
                   + ['purple' for i in range(10)]  \
                   + ['gold' for i in range(10)]    \

    def drawDice(self, numDiceToDraw):
        random.shuffle(self.bag)
        drawnDiceColors = self.bag[:numDiceToDraw]
        rolledDice = []
        for i in range(len(drawnDiceColors)):
            rolledDice.append((drawnDiceColors[i], random.randint(1, 6)))
        return rolledDice