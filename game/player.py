import sys, pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, walllist):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('../assets/forward.png')
        self.rect = self.image.get_rect()
        self.state = 'alive'
        self.rect.x = x
        self.rect.y = y
        self.walls = walllist

    def handle_keys(self):
        """ Handles Keys """
        if self.state == 'dead':
            return
        key = pygame.key.get_pressed()
        dist = 1 # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_DOWN]: # down key
            self.rect.y += dist # move down
        if key[pygame.K_UP]: # up key
            self.rect.y -= dist # move up
        if key[pygame.K_RIGHT]: # right key
            self.rect.x += dist # move right
        if key[pygame.K_LEFT]: # left key
            self.rect.x -= dist # move left


    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        # Did this update cause us to hit a wall?
        block_hit_list =  pygame.sprite.spritecollide(self, self.walls, False)
        if block_hit_list and self.state == 'alive':
            self.state = 'dead'
            self.image = pygame.image.load('../assets/hit.png')
            print('hit')
