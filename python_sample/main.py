b = True
puntajes = []
while b == True:
    a = input("Ingrese una calificación de 1 a 5. Ingrese 6 para finalizar: ")
    if not a.isdigit():
        print("Ingrese un número.")
    else:
        a = int(a)
        if a >= 1 and a <= 5:
            comentario = input("Comentario: ")
            puntaje = [a, comentario]
            puntajes.append(puntaje)
            for i in puntajes:
                print("P | C")
                print(f"{i[0]} | {i[1]}")
        elif a == 6:
            b = False
            print("Saliendo...")
            puntajes = []
            break
            
2