import ahorcado2
import adivinanza2

print('*********************************')
print('Elija su Juego')
print('*********************************')


print('(1) Ahorcado (2) Adivinanza')

juego = int(input("¿Cual juego? "))

if (juego == 1):
    print("Jugando Ahorcado")
    ahorcado.jugar_ahorcado()
elif (juego == 2):
    print("Jugando Adivinanza")
    adivinanza.jugar_adivinanza()