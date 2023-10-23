from entidades import Entidad
import pantalla as pan
import opciones as opt
import pygame


class Cotton (Entidad):
    def __init__(self):
        super().__init__()
        img = pygame.image.load(f'img\{self.tipo}.png')
        self.imagen = pygame.transform.scale(
            img, ((img.get_width() * opt.ESCALA), (img.get_height() * opt.ESCALA)))
    def mover(self, moverIzquierda, moverDerecha):
        x1 = 0
        y1 = 0

        # Lógica de movimiento izquierda/derecha
        if moverIzquierda:
            x1 = -self.velocidad
            self.flip = True
            self.direccion = -1
        if moverDerecha:
            self.flip = False
            self.direccion = 1
            x1 = self.velocidad

        # Lógica de salto
        if self.saltando and self.rect.y == opt.SCREEN_HEIGHT - self.rect.height:
            y1 = self.velocidad_salto
            self.saltando = False

        # Actualización de la posición del jugador
        self.rect.x += x1
        self.rect.y += y1

        # Manejo del escudo
        if self.escudo_activado:
            self.escudo_tiempo -= 1
            if self.escudo_tiempo <= 0:
                self.escudo_activado = False

    def activar_escudo(self):
        if not self.escudo_activado:
            self.escudo_activado = True
            self.escudo_tiempo = 300  # Ajusta la duración del escudo según sea necesario
