from random import randrange
from commons.validateUserInput import validateUserInput
from game.gameProcess import buildGame

rangeByDifficulty = {
    1: range(1, 21),
    2: range(1, 13),
    3: range(1, 6)
}


def playAlone():
    optionSelected = False
    while not optionSelected:
        optionSelected = validateUserInput([1, 3], 4)
    gessNumber = randrange(1, 1000)
    if optionSelected == 1:
        rangeNumberAttempts = rangeByDifficulty[optionSelected]
        return buildGame(gessNumber, rangeNumberAttempts)
    elif optionSelected == 2:
        rangeNumberAttempts = rangeByDifficulty[optionSelected]
        return buildGame(gessNumber, rangeNumberAttempts)
    elif optionSelected == 3:
        rangeNumberAttempts = rangeByDifficulty[optionSelected]
        return buildGame(gessNumber, rangeNumberAttempts)


def playWithPartner(gessNumber):
    optionSelected = False
    while not optionSelected:
        optionSelected = validateUserInput([1, 3], 4)
    if optionSelected == 1:
        rangeNumberAttempts = rangeByDifficulty[optionSelected]
        return buildGame(gessNumber, rangeNumberAttempts)
    elif optionSelected == 2:
        rangeNumberAttempts = rangeByDifficulty[optionSelected]
        return buildGame(gessNumber, rangeNumberAttempts)
    elif optionSelected == 3:
        rangeNumberAttempts = rangeByDifficulty[optionSelected]
        return buildGame(gessNumber, rangeNumberAttempts)
