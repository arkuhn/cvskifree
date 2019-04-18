import sys, pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load('../assets/forward.png')
        self.rect = self.image.get_rect()

    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 0.2 # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_DOWN]: # down key
            self.y += dist # move down
        elif key[pygame.K_UP]: # up key
            self.y -= dist # move up
        if key[pygame.K_RIGHT]: # right key
            self.x += dist # move right
        elif key[pygame.K_LEFT]: # left key
            self.x -= dist # move left

    def draw(self, screen):
       screen.blit(self.image, (self.x, self.y))
