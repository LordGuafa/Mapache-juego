import pygame
import opciones as opt
import pantalla as pan
import os
from bala import Bala


class Entidad(pygame.sprite.Sprite):
    def __init__(self, tipo):
        # Inicialización de la clase base Sprite
        pygame.sprite.Sprite.__init__(self)
        self.vivo = True
        # Atributos del jugador
        self.contBalas = 0
        self.contSaltos = 0
        self.tipo = tipo
        self.velocidad = opt.VELOCIDAD
        self.direccion = 1
        self.flip = False
        self.saltando = False
        self.enAire = True
        self.velocidad_salto = 0
        self.escudo_activado = False
        self.escudoTiempo = 0
        self.accion = 0
        self.vida = 100
        self.escudo = 100
        self.listaAnimacion = []
        self.indiceFrame = 0
        self.tiempoActual = pygame.time.get_ticks()
        tipoAnimaciones = ['Base', 'Correr',
                           'Disparar', 'Morir', 'Saltar']

        for animacion in tipoAnimaciones:
            tempList = []
            # Cuenta cuántas imágenes hay por carpeta
            numImg = len(os.listdir(f'img\{self.tipo}\{animacion}'))
            for i in range(numImg):
                img = pygame.image.load(
                    f'img\{self.tipo}\{animacion}\{i}.png').convert_alpha()
                img = pygame.transform.scale(
                    img, ((img.get_width() * opt.ESCALA), (img.get_height() * opt.ESCALA)))
                tempList.append(img)
            self.listaAnimacion.append(tempList)

        self.listaAnimacion.append(tempList)
        self.imagen = self.listaAnimacion[self.accion][self.indiceFrame]
        # Rectángulo que representa la posición del jugador en la pantalla
        self.rect = self.imagen.get_rect()
        self.rect.center = (opt.POSX, opt.POSY)

    # Método para manejar el movimiento del jugador
    def mover(self, moverIzquierda, moverDerecha):
        x1 = 0
        y1 = 0

        # Lógica de movimiento izquierda/derecha
        if moverIzquierda:
            x1 = -self.velocidad
            self.flip = False
            self.direccion = -1
        if moverDerecha:
            self.flip = True
            self.direccion = 1
            x1 = self.velocidad
        # Lógica de salto
        if self.saltando == True and self.enAire == False and self.contSaltos <= 2:
            self.contSaltos += 1
            self.velocidad_salto = opt.VEL_SALTO
            self.saltando = False
            if self.contSaltos == 2:
                self.contSaltos = 0
                self.enAire = True

        y1 += self.velocidad_salto

        # Actualización de la posición del jugador
        self.rect.x += x1
        self.rect.y += y1

        # Manejo del escudo
        if self.escudo_activado:
            self.escudo_tiempo -= 1
            if self.escudo_tiempo <= 0:
                self.escudo_activado = False

    # Actualiza las animaciones
    def actualizarAnimacion(self):
        cooldownAnimacion = 500
    # Actualiza la imagen dependiendo del cuadro
        self.imagen = self.listaAnimacion[self.accion][self.indiceFrame]
    # Verifica cuánto ha pasado desde la última actualización
        if pygame.time.get_ticks() - self.tiempoActual > cooldownAnimacion:
            self.tiempoActual = pygame.time.get_ticks()
            self.indiceFrame += 1
    # Reinicia la animación
        if self.indiceFrame >= len(self.listaAnimacion[self.accion]):
            self.indiceFrame = 0

    def actualizarAccion(self, nuevaAccion):
        if nuevaAccion != self.accion:
            self.accion = nuevaAccion
            self.indiceFrame = 0
            self.tiempoActual = pygame.time.get_ticks()

    # Método para aplicar la gravedad al jugador
    def aplicarGravedad(self):
        if self.rect.y < opt.SCREEN_HEIGHT - self.rect.height:
            self.velocidad_salto += opt.GRAVEDAD
            self.rect.y += self.velocidad_salto

        else:
            self.velocidad_salto = 0
            self.rect.y = opt.SCREEN_HEIGHT - self.rect.height
            self.enAire = False
            self.contSaltos = 0
    # Método para manejar el salto del jugador
    # def saltar(self):
    #     if not self.saltando and self.rect.y == opt.SCREEN_HEIGHT - self.rect.height:
    #         self.velocidad_salto = -15
    #         self.saltando = True

    # Método para activar el escudo del jugador
    def activarEscudo(self):
        if not self.escudo_activado:
            self.escudo_activado = True
            self.escudo_tiempo = 300  # Ajusta la duración del escudo según sea necesario

    def disparar(self) -> Bala:
        """La entidad dispara
        Returns:
            Bala: Bala que es alojada en el grupo del main
        """
        bala = Bala(self.rect.centerx + (0.6*self.rect.size[0]*self.direccion),
                    self.rect.centery, self.direccion)
        return bala

    # Método para mostrar al jugador en la pantalla
    def mostrar(self):
        # Dibuja el escudo si está activado
        if self.escudo_activado:
            pygame.draw.rect(pan.screen, (0, 0, 255), (self.rect.x - 5,
                             self.rect.y - 5, self.rect.width + 10, self.rect.height + 10), 2)
        # Dibuja al jugador en la pantalla
        pan.screen.blit(pygame.transform.flip(
            self.imagen, self.flip, False), self.rect)

        # Dibuja la barra de vida
        pygame.draw.rect(pan.screen, (255, 0, 0), (10, 10, self.vida * 2, 10))
        # Dibujar la barra de escudo justo debajo de la barra de vida
        if self.escudo_activado:
            # Ajusta la velocidad de disminución según sea necesario
            escudo_length = max(0, (self.escudo_tiempo / 300) * 200)
            pygame.draw.rect(pan.screen, (0, 0, 255),
                             (10, 25, escudo_length, 10))

    def update(self):
        self.actualizarAnimacion()

        # Actualiza cooldown
        if self.contBalas > 0:
            self.contBalas -= 1
