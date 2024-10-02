import pygame
from player import Player

from constants import *

def main():
    #print("Starting asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # game loop
    pygame.event.pump() # no screen opens on mac without this for some reason
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # nothing above here


        player.update(dt)
        

        # updates above this line
        

        screen.fill(BLACK)
        player.draw(screen)
        

        # draw calls above this line
        pygame.display.flip()
        # tick returns time passed since last frame, / 1000 to convert to ms
        dt = clock.tick(60) / 1000 # tick(60) pause for 1/60th of a second



if __name__ == "__main__":
    main()
