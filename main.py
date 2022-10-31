# Adivina el Número
# El juego consiste en adivinar un número entre 1 y 1000, puede ser de uno o dos participantes.

from commons.menu import printMenu, printSubMenu, printGameTitle, menuOptions
from commons.validateUserInput import validateUserInput, validateUserTwoGessNumber
from game.main import playAlone, playWithPartner
from game.saveGameToFile import saveGameToFile
from game.statistics import showStatistics
from commons.color import color_text, rgb


def beginGame():
    printGameTitle()
    printMenu()

    optionSelected = False
    while not optionSelected:
        optionSelected = validateUserInput([1, 4], 5)

    if optionSelected == 1:
        print(f'\n{color_text(menuOptions[optionSelected], rgb.BLUE)}')
        printSubMenu()
        result = playAlone()
        print(f'\n{result}\n')
        saveGameToFile(result)

        beginGame()
    elif optionSelected == 2:
        print(f'\n{color_text(menuOptions[optionSelected], rgb.BLUE)}')
        gessNumber = False
        while not gessNumber:
            gessNumber = validateUserTwoGessNumber()
        printSubMenu()
        result = playWithPartner(gessNumber)
        print(f'\n{result}\n')
        saveGameToFile(result)

        beginGame()
    elif optionSelected == 3:
        print(f'\n{color_text(menuOptions[optionSelected], rgb.BLUE)}')
        showStatistics()
        beginGame()
    elif optionSelected == 4:
        print(color_text('\nHasta luego!', rgb.BLUE))
        exit()


beginGame()
