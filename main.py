import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_color= "black"
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    asteroid_field = AsteroidField()
    Shot.containers = (shots, updateable, drawable)

    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(background_color)

        updateable.update(dt)

        for entity in drawable:
            entity.draw(screen)

        for asteroid in asteroids:
            for shot in shots: 
                if asteroid.isColliding(shot):
                    shot.kill()
                    asteroid.split()
            if asteroid.isColliding(player):
                print("Game Over!")
                sys.exit()
            
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

