import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys



def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()

    dt = 0


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()

    drawable = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()

    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)

    Shot.containers = (shots, updatable, drawable)

    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    astfield = AsteroidField()





    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        # player1.draw(screen)
        # player1.update(dt)


        updatable.update(dt)

        for asteroid in asteroids:
            
            if asteroid.collides_with(player1):
                sys.exit("Game over!")
        
        screen.fill('black')

        for thing in drawable:
            thing.draw(screen)



        pygame.display.flip()

    
        dt = clock.tick(60) /1000



if __name__ == "__main__":
    main()