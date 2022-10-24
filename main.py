# Adivina el Número
# El juego consiste en adivinar un número entre 1 y 1000, puede ser de uno o dos participantes.

from commons.menu import printMenu, printSubMenu
from game.main import playAlone, playWithPartner
from game.saveGameToFile import saveGameToFile
from game.statistics import showStatistics
from commons.color import color_text, rgb

def beginGame():
    print(
        color_text('=========================================\
                  \n            Adivina el Número\
                  \n=========================================', 
            rgb.YELLOW
        )
    )
    printMenu()

    chooseAnOption = '\nEscoja una de las opciones entre 1 y 4: '
    gameTitles = { 1: 'Partida en modo solitario', 2: 'Partida de 2 jugadores', 3: 'Estadística', 4: 'Hasta luego!' }

    optionSelected = int(input(color_text(chooseAnOption, rgb.MAGENTA)))

    while optionSelected not in range(1, 5):
        print(color_text('\nOpción inválida \n', rgb.RED))
        optionSelected = int(input(color_text(chooseAnOption, rgb.MAGENTA)))

    if optionSelected == 1:
        print(f'\n{color_text(gameTitles[optionSelected], rgb.BLUE)}')
        printSubMenu()
        result = playAlone()
            
        print(f'\n{result}\n')
        saveGameToFile(result)
        beginGame()
    elif optionSelected == 2:
        print(f'\n{color_text(gameTitles[optionSelected], rgb.BLUE)}')
        gessNumber = int(input('\nJugador #1. Por favor, indique el número a adivinar entre 1 y 1000: '))
        while gessNumber not in range(1, 1001):
            print('\nNúmero inválido! Intente de nuevo. \n')
            gessNumber = int(input('\nJugador #1. Por favor, indique el número a adivinar entre 1 y 1000: '))        
        printSubMenu()
        result = playWithPartner(gessNumber)

        print(f'\n{result}\n')
        saveGameToFile(result)
        beginGame()
    elif optionSelected == 3:
        print(f'\n{color_text(gameTitles[optionSelected], rgb.BLUE)}')
        showStatistics()
        beginGame()
    elif optionSelected == 4:
        print(f'\n{color_text(gameTitles[optionSelected], rgb.BLUE)}')
        exit()

beginGame()        