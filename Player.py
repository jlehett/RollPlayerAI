import json
import random

class Player:
    def __init__(self):
        self.attributes = {
            'str': {
                'dice': [None for _ in range(3)],
                'totalNoBonus': 0,
                'bonus': 0,
            },
            'dex': {
                'dice': [None for _ in range(3)],
                'totalNoBonus': 0,
                'bonus': 0,
            },
            'con': {
                'dice': [None for _ in range(3)],
                'totalNoBonus': 0,
                'bonus': 0,
            },
            'int': {
                'dice': [None for _ in range(3)],
                'totalNoBonus': 0,
                'bonus': 0,
            },
            'wis': {
                'dice': [None for _ in range(3)],
                'totalNoBonus': 0,
                'bonus': 0,
            },
            'cha': {
                'dice': [None for _ in range(3)],
                'totalNoBonus': 0,
                'bonus': 0,
            },
        }

    """
        Update the totals for all attributes.
    """
    def updateDiceTotals(self):
        for attribute in self.attributes:
            totalNoBonus = 0
            for dice in self.attributes[attribute]['dice']:
                if not dice:
                    break
                totalNoBonus += dice[1]
            self.attributes[attribute]['totalNoBonus'] = totalNoBonus

    """
        Construct the player's dice string for printing.
    """
    def getPlayerDiceString(self):
        constantStrings = {
            'spacer': '   ',
            'blank':  '        ',
            'white':  'WHITE ',
            'black':  'BLACK ',
            'green':  'GREEN ',
            'blue':   'BLUE  ',
            'red':    'RED   ',
            'purple': 'PURPLE',
            'gold':   'GOLD  ',
        }
        attributes = ['str', 'dex', 'con', 'int', 'wis', 'cha']
        totalString = ''
        for attribute in attributes:
            attributeString = '  ' + "{:<4}".format(str(self.attributes[attribute]['totalNoBonus'] + self.attributes[attribute]['bonus']))
            attributeString += attribute.upper() + ': '
            bonus = self.attributes[attribute]['bonus']
            if bonus != 0:
                if bonus > 0:
                    attributeString += '+'
                attributeString += str(bonus)
            else:
                attributeString += '  '
            attributeString += ' '
            attributeDice = self.attributes[attribute]['dice']
            for diceIndex in range(3):
                if attributeDice[diceIndex]:
                    attributeString += constantStrings[attributeDice[diceIndex][0]] + ' ' + str(attributeDice[diceIndex][1])
                else:
                    attributeString += constantStrings['blank']
                if diceIndex != 2:
                    attributeString += constantStrings['spacer']
            attributeString += '\n'
            totalString += attributeString
        return totalString

    """
        Place the dice in the open column furthest to the left.
    """
    def placeDice(self, attribute, dice):
        diceList = self.attributes[attribute]['dice']
        for i in range(3):
            if not diceList[i]:
                diceList[i] = dice
                self.updateDiceTotals()
                return

    def placeInitialDice(self, dice):
        attributeMap = {
            1: 'str',
            2: 'dex',
            3: 'con',
            4: 'int',
            5: 'wis',
            6: 'cha'
        }
        while len(dice) > 0:
            print('\nStarting Dice: ')
            print(dice)
            print(self.getPlayerDiceString())
            diceIndex = int(input('Select dice index (1-' + str(len(dice)) + '): '))
            placeIndex = int(input('Select place index (1-6): '))
            diceChoice = dice[diceIndex-1]
            self.placeDice(attributeMap[placeIndex], diceChoice)
            dice.remove(diceChoice)

    """
        Have the player take a turn given the dice pool.
    """
    def playerTurn(self, dice):
        attributeMap = {
            1: 'str',
            2: 'dex',
            3: 'con',
            4: 'int',
            5: 'wis',
            6: 'cha'
        }
        print('Available Dice:')
        print(dice)
        print(self.getPlayerDiceString())
        diceIndex = int(input('Select dice index (1-' + str(len(dice)) + '): '))
        placeIndex = int(input('Select place index (1-6): '))
        diceChoice = dice[diceIndex-1]
        self.placeDice(attributeMap[placeIndex], diceChoice)

    """
        Allow the player to create a character.
    """
    def pickCharacter(self):
        raceChoice = input('Please select a race: ')
        self.selectRace(raceChoice)
        self.getRandomBackstory()
        self.getRandomClass()
        print('\nYou are a [' + self.backstory['name'].upper() + '] [' + self.characterClass['name'].upper() + '] [' + self.race.upper() + ']')
        print('\nYour attribute goals are:')
        print('\t' + self.getAttributeGoalString('str'))
        print('\t' + self.getAttributeGoalString('dex'))
        print('\t' + self.getAttributeGoalString('con'))
        print('\t' + self.getAttributeGoalString('int'))
        print('\t' + self.getAttributeGoalString('wis'))
        print('\t' + self.getAttributeGoalString('cha'))
        print('\nYour backstory goals are:')
        print(self.getBackstoryGoalString())

    """
        Helper function that will construct a backstory goal string to
        display for a specified attribute.
    """
    def getBackstoryGoalStringForAttribute(self, attribute):
        # Define constants
        constantStrings = {
            'spacer': '   ',
            'blank':  '      ',
            'white':  'WHITE ',
            'black':  'BLACK ',
            'green':  'GREEN ',
            'blue':   'BLUE  ',
            'red':    'RED   ',
            'purple': 'PURPLE',
            'gold':   'GOLD  ',
        }
        # Define the unique attribute string
        goalColor = self.backstory['data'][attribute]['color']
        goalColorString = constantStrings[goalColor]
        goalPosition = self.backstory['data'][attribute]['position']
        goalString = attribute.upper() + ': ' + constantStrings['spacer']
        if goalPosition == 1:
            goalString += goalColorString
        else:
            goalString += constantStrings['blank']
        goalString += constantStrings['spacer']
        if goalPosition == 2:
            goalString += goalColorString
        else:
            goalString += constantStrings['blank']
        goalString += constantStrings['spacer']
        if goalPosition == 3:
            goalString += goalColorString
        else:
            goalString += constantStrings['blank']
        return goalString

    """
        Create the whole backstory goal string for printing to a user.
    """
    def getBackstoryGoalString(self):
        # Define separate attribute strings
        return  '\t' + self.getBackstoryGoalStringForAttribute('str')  \
            + '\n\t' + self.getBackstoryGoalStringForAttribute('dex') \
            + '\n\t' + self.getBackstoryGoalStringForAttribute('con') \
            + '\n\t' + self.getBackstoryGoalStringForAttribute('int') \
            + '\n\t' + self.getBackstoryGoalStringForAttribute('wis') \
            + '\n\t' + self.getBackstoryGoalStringForAttribute('cha')
        

    """
        Construct an attribute goal string for printing to a user.
    """
    def getAttributeGoalString(self, attribute):
        attributeGoalString = attribute.upper() + ': ' + str(self.characterClass['data'][attribute]['min'])
        if (self.characterClass['data'][attribute]['max'] == 99):
            attributeGoalString += '+'
        elif (self.characterClass['data'][attribute]['max'] != self.characterClass['data'][attribute]['min']):
            attributeGoalString += '-' + str(self.characterClass['data'][attribute]['max'])
        stars = ''.join(['*' for _ in range(self.characterClass['data'][attribute]['stars'])])
        attributeGoalString = "{:<15}".format(attributeGoalString)
        attributeGoalString += stars
        return attributeGoalString

    """
        Set the player's race (in all lowercase) to set the
        bonuses for the player.
    """
    def selectRace(self, race):
        self.race = race
        with open('./assets/race.json') as f:
            allRaceObj = json.load(f)
        raceObj = allRaceObj[race]
        for key, value in raceObj.items():
            self.attributes[key]['bonus'] = value

    """
        Grab random backstory for the player.
    """
    def getRandomBackstory(self):
        with open('./assets/backstory.json') as f:
            allBackstoryObj = json.load(f)
        allBackstoryKeys = list(allBackstoryObj.keys())
        backstoryKey = random.choice(allBackstoryKeys)
        self.backstory = {
            'name': backstoryKey,
            'data': allBackstoryObj[backstoryKey]
        }

    """
        Grab random class for the player.
    """
    def getRandomClass(self):
        with open('./assets/class.json') as f:
            allClassObj = json.load(f)
        allClassKeys = list(allClassObj.keys())
        classKey = random.choice(allClassKeys)
        self.characterClass = {
            'name': classKey,
            'data': allClassObj[classKey]
        }