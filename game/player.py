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



    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        # Did this update cause us to hit a wall?
        block_hit_list =  pygame.sprite.spritecollide(self, self.walls, False)
        if block_hit_list and self.state == 'alive':
            self.state = 'dead'
            self.image = pygame.image.load('../assets/hit.png')
            print('hit')


    def check_collision(self, entities):
        gets_hit = pygame.sprite.spritecollide(self, entities, True)
        if gets_hit:
            self.state = 'dead'
            self.image = pygame.image.load('../assets/hit.png')
            print('hit')