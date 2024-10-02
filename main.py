import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    #print("Starting asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
   
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()


    # game loop
    pygame.event.pump() # no screen opens on mac without this for some reason
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # nothing above here

        for entity in updatable:
            entity.update(dt)
       
        for entity in asteroids:
            if entity.check_collision(player):
                print("Game over!")
                sys.exit() # return 

        for shot in shots:
            for asteroid in asteroids:
                if shot.check_collision(asteroid):
                    print("shot made contact")

        # updates above this line
        screen.fill(BLACK)
        
        for entity in drawable:
            entity.draw(screen)
        
        # draw calls above this line
        pygame.display.flip()
        # tick returns time passed since last frame, / 1000 to convert to ms
        dt = clock.tick(60) / 1000 # tick(60) pause for 1/60th of a second



if __name__ == "__main__":
    main()
