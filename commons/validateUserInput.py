from commons.color import color_text, rgb
import getpass


def validateUserInput(rangeOptions, maxRange):
    inputLabel = f'\nEscoja una de las opciones entre {rangeOptions[0]} y {rangeOptions[1]}: '
    try:
        optionSelected = int(input(color_text(inputLabel, rgb.MAGENTA)))
        while optionSelected not in range(1, maxRange):
            print(color_text('\nOpción inválida \n', rgb.RED))
            optionSelected = int(input(color_text(inputLabel, rgb.MAGENTA)))

        return optionSelected
    except ValueError:
        print(color_text('\nOpción inválida \n', rgb.RED))

        return False


def validateUserTwoGessNumber():
    try:
        inputLabel = '\nJugador #1. Por favor, indique el número a adivinar entre 1 y 1000: '
        gessNumber = int(getpass.getpass(inputLabel))
        while gessNumber not in range(1, 1001):
            print('\nNúmero inválido! Intente de nuevo. \n')
            gessNumber = int(getpass.getpass(inputLabel))

        return gessNumber
    except ValueError:
        print(color_text('\nOpción inválida \n', rgb.RED))

        return False


def validateUserInput2(message):
    try:
        optionSelected = int(input(color_text(message, rgb.MAGENTA)))

        return optionSelected
    except ValueError:
        print(color_text('\nOpción inválida \n', rgb.RED))

        return False

