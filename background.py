import pantalla as pan
import opciones as opt
import pygame
screen = pan.screen

# Carga imágenes
fondo = pygame.image.load('img\Escenario/fondo.png').convert_alpha()
fondo = pygame.transform.scale(
    fondo, (opt.SCREEN_WIDTH, opt.SCREEN_HEIGHT))

# Obtener la altura de la imagen del suelo
suelo = pygame.image.load("img\Escenario/suelo.png")
altura_suelo = 100
suelo = pygame.transform.scale(suelo, (opt.SCREEN_WIDTH, altura_suelo))  # Ajusta la altura según sea necesario

def Background():
    # Dibujar la imagen del fondo
    screen.blit(fondo,(0,0))
    # Dibujar una línea roja
    pygame.draw.line(screen, opt.RED, (0, 300), (opt.SCREEN_WIDTH, 300))


