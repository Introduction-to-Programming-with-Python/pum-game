def jugar_PUM(jugadores: int, numero: int)-> str:

    jugadas = 0 
    conteo = 0
    i = 0

    numeros = range(1,20)

    while conteo < 20:

        conteo += 1
        i += 1

        if i == (jugadores+1):
            i = 1

        if conteo % numero == 0:
            jugada = "pum"
        else:
            jugada = conteo

        print(i,jugada)

    return ""

print(jugar_PUM(3, 5))