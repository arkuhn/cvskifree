import sys, pygame
from player import Player
from wall import Wall
from entity import Entity
pygame.init()
from pygame.locals import *

size = width, height = 650, 490
speed = [2, 2]
black = 0, 0, 0
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
screen.fill([255, 255, 255])
pygame.display.set_caption('CVSkiFree')
myfont = pygame.font.SysFont("monospace", 16)

wall_list = pygame.sprite.Group()
entity_list = pygame.sprite.Group()
 
wall = Wall(0, 0, 10, 490)
wall_list.add(wall)

wall = Wall(640, 0, 10, 490)
wall_list.add(wall)

wall = Wall(0, 0, 640, 0)
wall_list.add(wall)

wall = Wall(0, 490, 650, 0)
wall_list.add(wall)


player = Player(325, 245, wall_list)

score = 0


def addMoreEntities():
    global entity_list
    if len(entity_list.sprites()) < 10:
        for i in range(0, 5):
            entity = Entity()
            entity_list.add(entity)

def increaseDifficulty():
    pass

dist = 20
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if player.state == 'alive':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    player.rect.x -= dist
                    print('left')
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    player.rect.x += dist
                    print('right')

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    print('left stop')
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    print('right stop')
                if event.key == ord('q'):
                    pygame.quit()
                    sys.exit()
                    main = False 


    increaseDifficulty()

    addMoreEntities()

    if (player.state == 'dead'):
        titletext = myfont.render("GAME OVER", 1, (0,0,0))
        screen.blit(titletext, (320, 240))
        scoretext = myfont.render("Score = "+str(score), 1, (0,0,0))
        screen.blit(scoretext, (320, 220))
        for entity in entity_list.sprites():
            entity.speed = 0
            entity.speedModifier = 0
    else:
        score += 1


    entity_list.update()
    entity_list.draw(screen)
       
    wall_list.update()
    wall_list.draw(screen)

    player.check_collision(entity_list)
    player.update()
    player.draw(screen)

    scoretext = myfont.render("Score = "+str(score), 1, (0,0,0))
    screen.blit(scoretext, (10, 10))
    

    pygame.display.flip()
    screen.fill([255, 255, 255])
    clock.tick(30)