import pantalla as pan
import opciones as opt
import pygame
screen = pan.screen


def Background():
    screen.fill(opt.BG)
    pygame.draw.line(screen, opt.RED, (0, 400), (opt.SCREEN_WIDTH, 400))
