import pygame
import pantalla as pan
import opciones as opt
from entidades import Entidad
import background as bg
from bala import Bala
# from cotton import Cotton
pygame.init()


pygame.display.set_caption('Mapache-juego')

# Variables de control del jugador
izquierda = False
derecha = False
dispara = False


# Configuración del reloj y FPS
clock = pygame.time.Clock()


# Creación de grupos de balas
grupoBalas = pygame.sprite.Group()


# Creación del jugador
cotton = Entidad('Cotton')

# Bucle principal del juego
run = True
while run:
    clock.tick(opt.FPS)
    bg.Background()

    # Actualiza y muestra los grupos
    grupoBalas.update()
    grupoBalas.draw(pan.screen)

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                izquierda = True
            if event.key == pygame.K_d:
                derecha = True
            if event.key == pygame.K_w and cotton.vivo:
                salt = True
                cotton.saltando = True
            if event.key == pygame.K_s:
                cotton.activarEscudo()
            if event.key == pygame.K_SPACE:
                dispara = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                izquierda = False
            if event.key == pygame.K_d:
                derecha = False
            if event.key == pygame.K_SPACE:
                dispara = False

    if cotton.vivo:
        if dispara:
            cotton.actualizarAccion(2)  # 2: disparar
            cotton.disparar()
            grupoBalas.add(cotton.disparar())
        elif cotton.enAire:
            cotton.actualizarAccion(4)  # 4: saltar

        elif izquierda or derecha:
            cotton.actualizarAccion(1)  # 1: correr
        else:
            cotton.actualizarAccion(0)  # 0: base

    # Actualización del jugador
    cotton.actualizarAnimacion()
    cotton.mover(izquierda, derecha)
    cotton.aplicarGravedad()

    # Muestra al jugador
    cotton.mostrar()

    # Actualización de la pantalla
    pygame.display.update()

# Cierre del juego
pygame.quit()
