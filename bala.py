
import pantalla as pan
import opciones as opt
import pygame

# Carga imágenes
imgBala = pygame.image.load('img\Balas/Cotton/0.png').convert_alpha()
imgBala = pygame.transform.scale(
    imgBala, ((imgBala.get_width() * opt.ESCALA), (imgBala.get_height() * opt.ESCALA)))

# Carga imágenes


class Bala(pygame.sprite.Sprite):
    def __init__(self, x, y, direccion):
        pygame.sprite.Sprite.__init__(self)
        self.velocidad = 10
        self.image = imgBala
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direccion = direccion

    def update(self):
        # Mueve la bala
        self.rect.x += (self.direccion*self.velocidad)

        # Verifica que la si la bala sale de la pantalla
        if self.rect.right < 0 or self.rect.left > opt.SCREEN_WIDTH:
            self.kill
