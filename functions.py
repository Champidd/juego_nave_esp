import pygame

import random

 

def mover_nave(screen, nave_img, x, y):

    screen.blit(nave_img, (x, y))

 

def disparar_proyectil(x, y):

    # Lógica para disparar proyectiles

    pass

 

def generar_asteroides(screen, asteroide_img, asteroides):

    asteroide_img = pygame.transform.scale(asteroide_img, (64, 64))  # Redimensionar la imagen del asteroide

    for asteroide in asteroides:

        screen.blit(asteroide_img, (asteroide['x'], asteroide['y']))

        asteroide['y'] += asteroide['speed']

        if asteroide['y'] > 600:

            asteroide['x'] = random.randint(0, 736)  # Nueva posición aleatoria en el eje x

            asteroide['y'] = random.randint(-100, -50)  # Nueva posición aleatoria en el eje y

 

def detectar_colisiones(nave_x, nave_y, asteroides):

    nave_rect = pygame.Rect(nave_x, nave_y, 64, 64)

    for asteroide in asteroides:

        asteroide_rect = pygame.Rect(asteroide['x'], asteroide['y'], 64, 64)

        if nave_rect.colliderect(asteroide_rect):

            return True, asteroide

    return False, None