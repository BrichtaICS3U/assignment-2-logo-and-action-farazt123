import pygame
WHITE = (255, 255, 255)

class Fish(pygame.sprite.Sprite):
    #These are the fish going across the screen

    def __init__(self, color, width, height):

        super().__init__()

        #Give fishy some dimensions and stuff
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        #draw it
        pygame.draw.ellipse(self.image, color, [0,0,width,height])
        
        #see how big it is
        self.rect = self.image.get_rect()
