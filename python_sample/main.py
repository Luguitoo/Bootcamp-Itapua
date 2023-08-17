b = True
puntajes = []

def introducir_puntajes():
        while True:
            a = input("Ingrese una calificación de 1 a 5. Ingrese 6 para finalizar: ")
            if not a.isdigit():
                print("Ingrese un número.")
            else:
                a = int(a)
                if a == 6:
                    break
                if a >= 1 and a <= 5:
                    comentario = input("Comentario: ")
                    puntaje = [a, comentario]
                    puntajes.append(puntaje)
                    with open("data.txt", 'a') as file:
                        file.write(f'{puntaje} \n')
                else:
                    print("Por favor, introduzca un valor entre 1 y 5")

def mostrar_resultados():
    print("Resultados guardados:")
    with open("data.txt", "r") as read_file:
        print(read_file.read())
aux = 0
while b == True:
    print( 'Seleccione el proceso que desea aplicar' )
    print( '1: Introduzca los puntos de valoración y los comentarios.' )
    print( '2: Comprueba los resultados obtenidos hasta ahora.' )
    print( '3: Terminación.' )
    num = input()
    if num.isdigit():
        num = int(num)
        if num == 1:
            introducir_puntajes()
        elif num == 2:
            mostrar_resultados()
        elif num == 3:
            b = False
            print("Saliendo...")
            puntajes = []
            break
        else:
            print("Por favor, introduzca del 1 a 3")
    