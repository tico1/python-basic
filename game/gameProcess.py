from commons.color import color_text, rgb

def buildGame(gessNumber, rangeNumberAttempts):
    for attempt in rangeNumberAttempts:
        userValue = int(input(f'Intento #{attempt}. Por favor, indique el número buscado: '))        
        result = evaluateUserResponse(userValue, gessNumber)
        if result == True:
            print(color_text('\nExcelente! Lo ha encontrado.', rgb.GREEN))
            player = input('Por favor, indique su nombre: ')
            print(color_text(f'\nJugador: {player}, Número Ganador: {userValue}, Obtenido en el intento#: {attempt}, Resultado: Ganó\n\n', rgb.GREEN))
            
            return ((player, 'Win'))
    print(color_text('\nAlcanzó el número máximo de intentos sin adivinar :(', rgb.RED))
    player = input('Por favor, indique su nombre: ')
    print(color_text(f'\nJugador: {player}, Número buscado: {gessNumber}, Intentos usados: {attempt}, Resultado: Perdió\n\n', rgb.RED))
    
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