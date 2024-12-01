
import pygame

import random

from functions import mover_nave, disparar_proyectil, generar_asteroides, detectar_colisiones

 

# Inicialización de PyGame

pygame.init()

 

# Configuración de la pantalla

screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

pygame.display.set_caption("Juego de Nave Espacial")

 

# Colores

BLACK = (0, 0, 0)

WHITE = (255, 255, 255)

 

# Cargar imágenes y redimensionarlas a 64x64

nave_img = pygame.transform.scale(pygame.image.load('nave.png'), (64, 64))

asteroide_img = pygame.transform.scale(pygame.image.load('asteroide.png'), (64, 64))

rayo_img = pygame.transform.scale(pygame.image.load('rayo.png'), (32, 32))  # Redimensionar la imagen del rayo a 32x32

 

# Variables de configuración

cantidad_asteroides = 5

velocidad_asteroides = 5

 

# Función para mostrar el menú

def mostrar_menu():

    global cantidad_asteroides, velocidad_asteroides

    menu = True

    while menu:

        screen.fill(BLACK)

        font = pygame.font.Font(None, 74)

        text = font.render("Menu", True, WHITE)

        screen.blit(text, (350, 50))

       

        font = pygame.font.Font(None, 36)

        text = font.render("1. Cantidad de Asteroides: " + str(cantidad_asteroides), True, WHITE)

        screen.blit(text, (200, 150))

        text = font.render("2. Velocidad de Asteroides: " + str(velocidad_asteroides), True, WHITE)

        screen.blit(text, (200, 200))

        text = font.render("Presiona Enter para comenzar", True, WHITE)

        screen.blit(text, (200, 300))

       

        pygame.display.flip()

       

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()

                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_1:

                    cantidad_asteroides += 1

                if event.key == pygame.K_2:

                    velocidad_asteroides += 1

                if event.key == pygame.K_3 and cantidad_asteroides > 1:

                    cantidad_asteroides -= 1

                if event.key == pygame.K_4 and velocidad_asteroides > 1:

                    velocidad_asteroides -= 1

                if event.key == pygame.K_RETURN:

                    menu = False

 

# Mostrar el menú antes de iniciar el juego

mostrar_menu()

 

# Posición inicial de la nave

nave_x = 370

nave_y = 480

nave_x_change = 0

 

# Lista de asteroides

asteroides = [{'x': random.randint(0, 736), 'y': random.randint(-100, -50), 'speed': velocidad_asteroides} for _ in range(cantidad_asteroides)]

 

# Bucle principal del juego

running = True

while running:

    screen.fill(BLACK)

   

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        if event.type == pygame.VIDEORESIZE:

            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:

                nave_x_change = -5

            if event.key == pygame.K_RIGHT:

                nave_x_change = 5

            if event.key == pygame.K_SPACE:

                disparar_proyectil(nave_x, nave_y)

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:

                nave_x_change = 0

 

    nave_x += nave_x_change

    if nave_x <= 0:

        nave_x = 0

    elif nave_x >= screen.get_width() - nave_img.get_width():

        nave_x = screen.get_width() - nave_img.get_width()

 

    mover_nave(screen, nave_img, nave_x, nave_y)

    generar_asteroides(screen, asteroide_img, asteroides)

   

    colision_detectada, asteroide_colisionado = detectar_colisiones(nave_x, nave_y, asteroides)

    if colision_detectada:

        # Mostrar imagen de colisión y mensaje en el centro de la colisión

        colision_x = (nave_x + asteroide_colisionado['x']) // 2

        colision_y = (nave_y + asteroide_colisionado['y']) // 2

        screen.blit(rayo_img, (colision_x - rayo_img.get_width() // 2, colision_y - rayo_img.get_height() // 2))

        font = pygame.font.Font(None, 74)

        text = font.render("¡Chocaste!", True, WHITE)

        screen.blit(text, (350, 250))

        pygame.display.flip()

        pygame.time.wait(2000)  # Esperar 2 segundos antes de cerrar

        running = False  # Finalizar el juego en caso de colisión

 

    pygame.display.flip()

    pygame.time.Clock().tick(60)  # Limitar la velocidad de fotogramas a 60 FPS

 

pygame.quit()