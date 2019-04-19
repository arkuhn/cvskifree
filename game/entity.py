import sys, pygame
from random import randint
sprites = [pygame.image.load('../assets/tree1.png'),
           pygame.image.load('../assets/tree2.png'),
           pygame.image.load('../assets/tree3.png'),
           pygame.image.load('../assets/tree4.png'),
           pygame.image.load('../assets/stump.png'),
           pygame.image.load('../assets/rock.png'),
           pygame.image.load('../assets/snowbank.png') ]


class Entity(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image =  sprites[randint(0, len(sprites) - 1)]
        self.rect = self.image.get_rect()
        self.state = 'alive'
        self.rect.x = randint(0, 640)
        self.rect.y = randint(480, 840)
        self.speedModifier =  0.0001
        self.speed = 1

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        if self.rect.y < 0:
            self.kill()

        self.rect.y -= self.speed
        self.speed += self.speedModifier
