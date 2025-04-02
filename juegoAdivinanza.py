# -------------------------
# JUEGO DE ADIVINANZA
# -------------------------

"""" INTRODUCCIÓN:
Voy a programar el juego de adivinar un número pero con algunas 
personalizaciones de parte de usuario: se le va a permitir elegir hasta
qué número quiere adivinar y se le ofrecerá diferentes niveles de
difucultades para elegir. """

import random

# Establezco las variables a utilizar

numeroMaximo = 0
numeroSecreto = 0
intentosPromedio = 0
intentosMaximos = 0
intentos = 1
dificultad = 0
adivinado = False

# Bienvenida e introduccción de variables

print("¡Bienvenido al juego de adivinar el número secreto!")

while numeroMaximo < 50:
    numeroMaximo = int(input("Introduce el número máximo para adivinar, a partir del 50\n"))

numeroSecreto = random.randint(1,numeroMaximo)

"""" NIVELES DE DIFICULTAD:
Si se va tomando la media entre el número seleccionado y el número a adivinar
existe un número limitado de pasos para llegar a cualquier número.
Por ejemplo, entre 1 y 100, con 7 pasos podemos llegar a cualquier número, 
entre 1 y 200, necesitamos 8 pasos.
Voy a programar un algoritmo que me calcule esa cantidad de pasos y voy a proponer
diferentes niveles para el juego, dependiendo se número. """

i = float(numeroMaximo)

while i > 1.0:
    intentosPromedio += 1
    i = i / 2

while dificultad < 1 or dificultad > 5:
    dificultad = int(input("""\nElija el nivel de dificultad:
    1 - Siempre sale
    2 - Facil
    3 - (Pro)Medio
    4 - Complicado
    5 - Total adivino\n"""))

if dificultad == 1:
    intentosMaximos = numeroMaximo // 2
    print("\nVas a adivinar un número entre 1 y", numeroMaximo)
    print("Y tenes", intentosMaximos, "intentos para lograrlo.")
elif dificultad == 2:
    intentosMaximos = intentosPromedio * 2
    print("\nVas a adivinar un número entre 1 y", numeroMaximo)
    print("Y tenes", intentosMaximos, "intentos para lograrlo.")
elif dificultad == 3:
    intentosMaximos = intentosPromedio
    print("\nVas a adivinar un número entre 1 y", numeroMaximo)
    print("Y tenes", intentosMaximos, "intentos para lograrlo.")
elif dificultad == 4:
    intentosMaximos = intentosPromedio - 2
    print("\nVas a adivinar un número entre 1 y", numeroMaximo)
    print("Y tenes", intentosMaximos, "intentos para lograrlo.")
else:
    intentosMaximos = intentosPromedio - 4
    print("\nVas a adivinar un número entre 1 y", numeroMaximo)
    print("Y tenes", intentosMaximos, "intentos para lograrlo.")

# A partir de acá, va el código correspondiente al juego

while not adivinado and intentos <= intentosMaximos:
    print("\nEste es tu intento", intentos, "de", intentosMaximos)
    print("Introduce un número entre 1 y",numeroMaximo)
    numero = int(input(""))
    intentos += 1

    if numero == numeroSecreto:
        print("\n¡Felicitaciones! Adivinaste el número.")
        adivinado = True

    elif numero < numeroSecreto:
        print("Tu número es menor que el secreto.")
    else:
        print("Tu número es mayor que el secreto.")

if not intentos <= intentosMaximos:
    print("\nLo siento, te quedaste sin intentos...")
    print("El número secreto era el", numeroSecreto)
    print("Mejor suerte la próxima.")