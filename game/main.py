from random import randrange
from .gameProcess import buildGame

rangeByDifficulty = {
    1: range(1, 21),
    2: range(1, 13),
    3: range(1, 6)
}

def playAlone():    
    optionSelected = int(input('\nEscoja una de las opciones entre 1 y 3: '))
    gessNumber = randrange(1, 1000)
    while optionSelected not in range(1, 4):
        print('\nOpción inválida \n')
        optionSelected = int(input('\nEscoja una de las opciones entre 1 y 3: '))
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
    optionSelected = int(input('\nJugador #2: Escoja una de las opciones entre 1 y 3: '))    
    while optionSelected not in range(1, 4):
        print('\nOpción inválida \n')
        optionSelected = int(input('\nEscoja una de las opciones entre 1 y 3: '))
    if optionSelected == 1:        
        rangeNumberAttempts = rangeByDifficulty[optionSelected]
        return buildGame(gessNumber, rangeNumberAttempts)
    elif optionSelected == 2:
        rangeNumberAttempts = rangeByDifficulty[optionSelected]
        return buildGame(gessNumber, rangeNumberAttempts)
    elif optionSelected == 3:
        rangeNumberAttempts = rangeByDifficulty[optionSelected]
        return buildGame(gessNumber, rangeNumberAttempts)