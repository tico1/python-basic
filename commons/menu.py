menuOptions = { 1: '1. Partida en modo solitario', 2: '2. Partida de 2 jugadores', 3: '3. Estadística', 4: '4. Salir' }
def printMenu():
    for item in menuOptions:
        print(menuOptions[item])


subMenuOptions = { 1: '1. Fácil (20 intentos)', 2: '2. Medio (12 intentos)', 3: '3. Difícil (5 intentos)' }
def printSubMenu():
    print('\n')
    for item in subMenuOptions:
        print(subMenuOptions[item])