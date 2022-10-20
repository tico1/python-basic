# Adivina el Número
# El juego consiste en adivinar un número entre 1 y 1000, puede ser de uno o dos participantes.

from commons.menu import printMenu, printSubMenu
from game.main import playAlone, playWithPartner
import openpyxl

wb = openpyxl.Workbook()
activeSheet = wb.active
a1 = activeSheet['A1']
a1.value = 'Juego Adivina el Número Python Básico'
a2 = activeSheet['A2']
a2.value = ''
activeSheet.append(('Jugador', 'Intentos', 'Dificultad', 'Fecha', 'Estatus del juego'))
print(a1.value)


print('===================\n Adivina el Número\n===================')

def beginGame():
    printMenu()

    chooseAnOption = '\nEscoja una de las opciones entre 1 y 4: '
    gameTitles = { 1: 'Partida en modo solitario', 2: 'Partida de 2 jugadores', 3: 'Estadística', 4: 'Hasta luego!' }

    optionSelected = int(input(chooseAnOption))

    while optionSelected not in range(1, 5):
        print('\nOpción inválida \n')
        optionSelected = int(input(chooseAnOption))

    if optionSelected == 1:
        print(f'\n{gameTitles[optionSelected]}')
        printSubMenu()
        result = playAlone()
            
        # print(f'\n{result}\n')
        beginGame()
    elif optionSelected == 2:
        print(f'\n{gameTitles[optionSelected]}')
        gessNumber = int(input('\nJugador #1. Por favor, indique el número a adivinar entre 1 y 1000: '))
        while gessNumber not in range(1, 1001):
            print('\nNúmero inválido! Intente de nuevo. \n')
            gessNumber = int(input('\nJugador #1. Por favor, indique el número a adivinar entre 1 y 1000: '))        
        printSubMenu()
        result = playWithPartner(gessNumber)
        # print(f'\n{result}\n')
        beginGame()
    elif optionSelected == 3:
        print(f'\n{gameTitles[optionSelected]}')
    elif optionSelected == 4:
        print(f'\n{gameTitles[optionSelected]}')
        exit()
    # wb.save('adivina_el_numero.xlsx')

beginGame()        