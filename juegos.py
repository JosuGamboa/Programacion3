def escoger_juego():
    import Ahorcado
    import Adivinanza

    print('================================')
    print('Elija su Juego')
    print('================================')

    print("(1) Ahorcado (2) Adivinanza")

    juego = int(input("¿Cuál juego? "))

    if (juego == 1):
        print("Jugando ahorcado")
        Ahorcado.jugar()
    elif (juego == 2):
        print("Jugando adivinanza")
        Adivinanza.jugar()
if(__name__ == "__main__"):
    escoger_juego()
