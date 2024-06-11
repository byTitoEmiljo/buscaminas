import numpy as np
import tkinter as tk
import math


bombasReveladas = 0
puntosRevelados = 0


def getTam():
    global tam
    tam = int(math.sqrt(int(tamano.get())))


def getBombs():
    global bombs
    bombs = int(bombas.get())


def printMatriz(matriz):
    for i in matriz:
        print('\t', end=' ')
        for j in i:
            if j == 0:
                print(f'\033[31m{j}\033[0m', end='  ')
            else:
                print(f'\033[34m{j}\033[0m', end='  ')
        print()


def generar_juego():
    global matriz
    getTam()
    getBombs()

    matriz = np.ones((tam, tam), dtype=int)

    while np.sum(matriz == 0) < bombs:
        fil = np.random.randint(tam)
        col = np.random.randint(tam)
        if matriz[fil, col] != 0:
            matriz[fil, col] = 0

    # printMatriz(matriz) # Descomenta esta linea para ver las respuestas ^_~


def clicado(fila, columna):
    global bombasReveladas
    global puntosRevelados

    boton = botones[fila][columna]
    if matriz[fila, columna] == 0:
        boton.config(text="X", bg='orange')
        bombasReveladas += 1
    else:
        boton.config(text="•", bg='white')
        puntosRevelados += 1
    boton.config(state="disabled")

    minPerce = int(((tam * tam) * 10) / 100)

    if bombasReveladas == minPerce or bombasReveladas > 3:
        fin('Game Over')
    elif puntosRevelados == (tam * tam - bombs):
        fin('You Win')


def fin(resultado):
    ventanaResultados = tk.Toplevel(ventana)
    ventanaResultados.geometry('300x200')
    ventanaResultados.title('Resultado')
    label3 = tk.Label(ventanaResultados, text=resultado, font=("Verdana", 24))
    label3.pack()

    if resultado == 'Game Over':
        label4 = tk.Label(ventanaResultados, text=f'Puntuacion {puntosRevelados}', font=("Verdana", 15))
        label4.pack()
    elif resultado == 'You Win':
        label4 = tk.Label(ventanaResultados, text=f'Puntuacion {puntosRevelados}', font=("Verdana", 15))
        label4.pack()


def cuadricula():
    global botones
    frame_cuadricula = tk.Frame(ventana)
    frame_cuadricula.pack()

    botones = []
    for i in range(len(matriz)):
        fila = []
        for j in range(len(matriz[0])):
            boton = tk.Button(frame_cuadricula, width=3, height=1, bg='gray', command=lambda fila=i, col=j: clicado(fila, col))
            boton.grid(row=i, column=j)
            fila.append(boton)
        botones.append(fila)


def buscaminas():
    global bombasReveladas, puntosRevelados
    bombasReveladas = 0
    puntosRevelados = 0
    generar_juego()
    cuadricula()


ventana = tk.Tk()
ventana.geometry('400x450')
ventana.title("Buscaminas")

label1 = tk.Label(ventana, text='Tamaño')
label1.pack()
tamano = tk.Entry(ventana)
tamano.pack()

label2 = tk.Label(ventana, text='Cantidad de Bombas')
label2.pack()
bombas = tk.Entry(ventana)
bombas.pack()

iniciar = tk.Button(ventana, text='Jugar', padx=10, pady=3, command=buscaminas)
iniciar.pack()

ventana.mainloop()
