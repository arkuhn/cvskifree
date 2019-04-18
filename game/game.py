import sys, pygame
from player import Player
pygame.init()

size = width, height = 640, 480
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
screen.fill([255, 255, 255])
player = Player(0, 0)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    player.handle_keys()
    player.draw(screen)


    pygame.display.flip()