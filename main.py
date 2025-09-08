import sys
import pygame
from asteroid import Asteroid
from constants import *
from player import Player
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    
    while(True):
        #quit button in gui screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #fills the screen with black color
        screen.fill((0,0,0))
        
        #renders updatables
        updatable.update(dt)
        
        #check for collisions
        for object in asteroids:
            if object.collision(player):
                print("Game over!")
                sys.exit()
        
        #render drawables
        for drawab in drawable:
            drawab.draw(screen)
        
        #refreshes screen
        pygame.display.flip()
        
        #limit the framerate to 60 fps
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
