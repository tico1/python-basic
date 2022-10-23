def buildGame(gessNumber, rangeNumberAttempts):
    # print(gessNumber)
    for attempt in rangeNumberAttempts:
        userValue = int(input(f'Intento #{attempt}. Por favor, indique el número buscado: '))        
        result = evaluateUserResponse(userValue, gessNumber)
        if result == True:
            print('\nExcelente! Lo ha encontrado.')
            player = input('Por favor, indique su nombre: ')
            print(f'\nJugador: {player}, Número Ganador: {userValue}, Obtenido en el intento#: {attempt}, Resultado: Ganó\n\n')
            # gameResult = f'{player}, {userValue}, {attempt}, Win'        
            # return gameResult
            return ((player, 'Win'))
    print('\nAlcanzó el número máximo de intentos sin adivinar :(')
    player = input('Por favor, indique su nombre: ')
    print(f'\nJugador: {player}, Número buscado: {gessNumber}, Intentos usados: {attempt}, Resultado: Perdió\n\n')
    # gameResult = f'{player}, {userValue}, {attempt}, Lose'
    # return gameResult
    return ((player, 'Lose'))

def evaluateUserResponse(userValue, validNumber):
        if userValue > validNumber:
            print('El número buscado es menor')
            return False
        elif userValue < validNumber:
            print('El número buscado es mayor')
            return False
        elif userValue == validNumber:
            return True    