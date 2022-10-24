from random import randrange
from .gameProcess import buildGame
from commons.color import color_text, rgb

rangeByDifficulty = {
    1: range(1, 21),
    2: range(1, 13),
    3: range(1, 6)
}

def playAlone():    
    optionSelected = int(input(color_text('\nEscoja una de las opciones entre 1 y 3: ', rgb.MAGENTA)))
    gessNumber = randrange(1, 1000)
    while optionSelected not in range(1, 4):
        print(color_text('\nOpción inválida \n', rgb.RED))
        optionSelected = int(input(color_text('\nEscoja una de las opciones entre 1 y 3: ', rgb.MAGENTA)))
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
    optionSelected = int(input(color_text('\nJugador #2: Escoja una de las opciones entre 1 y 3: ', rgb.MAGENTA)))    
    while optionSelected not in range(1, 4):
        print(color_text('\nOpción inválida \n', rgb.RED))
        optionSelected = int(input(color_text('\nEscoja una de las opciones entre 1 y 3: ', rgb.MAGENTA)))
    if optionSelected == 1:        
        rangeNumberAttempts = rangeByDifficulty[optionSelected]
        return buildGame(gessNumber, rangeNumberAttempts)
    elif optionSelected == 2:
        rangeNumberAttempts = rangeByDifficulty[optionSelected]
        return buildGame(gessNumber, rangeNumberAttempts)
    elif optionSelected == 3:
        rangeNumberAttempts = rangeByDifficulty[optionSelected]
        return buildGame(gessNumber, rangeNumberAttempts)