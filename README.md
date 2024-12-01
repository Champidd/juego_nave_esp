Nave Espacial

----------------------------------------------------------------------------------------------------------------
 Este proyecto es un juego de nave espacial desarrollado en Python utilizando la biblioteca pygame. 
El objetivo del juego es controlar una nave espacial para evitar colisiones con asteroides que caen desde el espacio.

 

## Funcionalidades

1. **Inicialización y Configuración**:

   - Configuración de la pantalla de juego con un tamaño de 800x600 píxeles.

   - Carga y redimensionamiento de las imágenes de la nave y los asteroides a 64x64 píxeles.

 

2. **Menú de Opciones**:

   - Menú interactivo que permite al jugador personalizar la cantidad de asteroides y la velocidad de los asteroides.

   - Teclas para modificar las opciones:

     - 1: Aumentar la cantidad de asteroides.

     - 2: Aumentar la velocidad de los asteroides.

     - 3: Disminuir la cantidad de asteroides.

     - 4: Disminuir la velocidad de los asteroides.

     - `Enter`: Comenzar el juego.

 

3. **Movimiento de la Nave**:

   - Movimiento de la nave espacial hacia la izquierda y la derecha utilizando las teclas de flecha.


 

4. **Generación de Asteroides**:

   - Generación de asteroides en posiciones y tiempos aleatorios, cayendo desde la parte superior de la pantalla.

   - Reinicio de la posición de los asteroides cuando salen de la pantalla por la parte inferior.

 

5. **Detección de Colisiones**:

   - Detección de colisiones entre la nave y los asteroides utilizando `pygame.Rect.colliderect`.



## Mejoras Futuras

 

Algunas posibles mejoras para el juego podrían incluir:

- Añadir niveles de dificultad.

- Implementar un sistema de puntuación.

- Incluir efectos de sonido y música de fondo.

- Mejorar los gráficos y las animaciones.
