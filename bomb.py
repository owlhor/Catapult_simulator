import pygame
import pygame.math
import math
import time
from pygame.locals import *

G_grav = -9.81

class Bomb:
    def __init__(self, x, y, v0, alpha, timestep,imaga):
        self.image = pygame.image.load(imaga)
        self.alpha = alpha
        self.pos = pygame.Vector2()
        self.init_pos = pygame.Vector2(x, y)
        self.init_veloc = pygame.Vector2(math.cos(alpha * math.pi / 180) * v0, math.sin(alpha * math.pi / 180) * v0)
        self.init_aclerat = pygame.Vector2(0, G_grav)
        self.time = 0
        self.timestep = timestep
        self.y_po = y

    def draw(self, surface,stx,sty,sx,sy):
        self.image = pygame.transform.scale(self.image, (sx, sy))
        surface.blit(self.image, [self.pos.x * 15 + stx,  400 - self.pos.y * 15 + sty])
        time.sleep(.001)

    def sentxy (self,stx,sty,sx,sy):
        return self.pos.x * 15 + stx , 400 - self.pos.y * 15 + sty

    def update(self):

        if self.pos.y >= 0:  # s=ut+1/2at**2
            self.pos = self.init_pos + self.init_veloc * self.time + (self.init_aclerat * (self.time ** 2) / 2)
            self.time += self.timestep

    def draw_bg(self,surface):
        self.image = pygame.transform.scale(self.image, (20, 20))
        #pygame.draw.rect(surface, (0, 0, 0), (0, 0, 1000, 250))
        surface.blit(self.image, [self.pos.x * 16, 200 - self.pos.y * 12])
        time.sleep(.002)
        #self.image.fill((0,0,0,0))

    def update_bg(self):
        #print(self.pos.x,self.pos.y, "    ", self.y_po)
        if self.pos.y >= 0:  # s=ut+1/2at**2
            self.pos = self.init_pos + self.init_veloc * self.time + (self.init_aclerat * (self.time ** 2) / 2)
            self.time += self.timestep


