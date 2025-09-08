from pydoc import locate
import random
import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
        
    def update(self,dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        left = self.velocity.rotate(random.uniform(20,50))
        right = self.velocity.rotate(-random.uniform(20,50))
        newRadius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x,self.position.y,newRadius)
        asteroid.velocity = left * 1.2
        asteroid = Asteroid(self.position.x,self.position.y,newRadius)
        asteroid.velocity = right * 1.2
        