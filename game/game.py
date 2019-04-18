import sys, pygame
from player import Player
from wall import Wall
pygame.init()

size = width, height = 650, 490
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
screen.fill([255, 255, 255])


pygame.display.set_caption('CVSkiFree')

all_sprite_list = pygame.sprite.Group()
# Make the walls. (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()
 
wall = Wall(0, 0, 10, 480)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(640, 0, 10, 480)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(0, 0, 640, 10)
wall_list.add(wall)
all_sprite_list.add(wall)
 
wall = Wall(0, 480, 650, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

player = Player(325, 245, wall_list)

all_sprite_list.add(player)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    player.handle_keys()
    player.update()
    all_sprite_list.update()
    all_sprite_list.draw(screen)
    player.draw(screen)


    pygame.display.flip()
    screen.fill([255, 255, 255])