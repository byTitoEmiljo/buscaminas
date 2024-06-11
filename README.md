# Buscaminas

Este proyecto es una implementación del clásico juego de Buscaminas en Python, utilizando ´tkinter´ para la interfaz gráfica y ´numpy´ para la manipulación de la matriz del tablero. El objetivo del juego es descubrir todos los puntos seguros sin revelar las bombas.

### Características
* Configuración del tamaño del tablero y la cantidad de bombas.
* Interfaz gráfica intuitiva para jugar.
* Indicador de "Game Over" y "You Win" según el resultado del juego.

### Requisitos
* Python 3.x
* Bibliotecas: `numpy`, `tkinter`

### Instalación y Ejecución

1. Clona el repositorio: \
   `git clone https://github.com/tu_usuario/buscaminas.git`
3. Navega al directorio del proyecto: \
   `cd buscaminas`
5. Instala las dependencias necesarias (solo `numpy` ya que `tkinter` viene con Python): \
   `pip install numpy`
7. Ejecuta el script: \
   `python main.py`
   
### Uso
1. Al iniciar el programa, ingresa el tamaño del tablero (por ejemplo, 16 para un tablero 4x4) y la cantidad de bombas.
2. Haz clic en "Jugar" para generar el tablero.
3. Haz clic en las casillas para revelar los puntos. Si revelas una bomba, el juego termina.
4. El juego muestra un mensaje de "Game Over" si revelas 3 bombas, o "You Win" si descubres todos los puntos seguros.

### Ejemplo de Juego

1. Ingresa el tamaño del tablero y la cantidad de bombas:
  <img src='https://github.com/byTitoEmiljo/buscaminas/assets/119460094/7e0817ef-69d9-4dc0-9b17-2ed6e62861a4' width='250'>

2. Haz clic en "Jugar" para empezar a jugar.
  <img src='https://github.com/byTitoEmiljo/buscaminas/assets/119460094/01c48893-e19f-4409-9ba3-779729740121' width='250'>

3. Navega por el tablero haciendo clic en las casillas:
   * Las casillas seguras se muestran con "•".
    <img src='https://github.com/byTitoEmiljo/buscaminas/assets/119460094/1b30d693-f89b-4d97-95f3-a2490b502a9b' width='250'>

   * Las bombas se muestran con "X".
    <img src='https://github.com/byTitoEmiljo/buscaminas/assets/119460094/5b1dc16d-b7ac-4269-baea-95c769d722a8' width='250'>

4. Si revelas una bomba, aparecerá un mensaje de "Game Over".
<img src='https://github.com/byTitoEmiljo/buscaminas/assets/119460094/5aea66f5-b99f-41bd-b296-4648cbd7bd17' width='400'>

5. Si revelas todos los puntos seguros sin activar las bombas, aparecerá un mensaje de "You Win".
<img src='https://github.com/byTitoEmiljo/buscaminas/assets/119460094/4de523d9-52df-4bda-8649-1a8639199cbc' width='400'>

