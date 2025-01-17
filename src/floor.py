import pygame

class Floor(pygame.sprite.Sprite):
    """ Class representing the floor. 
    
    From: https://github.com/xbandrade/sokoban-solver-generator/blob/main/src/floor.py

    """
    def __init__(self, *groups, x, y):
        super().__init__(*groups)
        self.image = pygame.image.load('img/grass.png')
        self.image = pygame.transform.scale(self.image, [64, 64])
        self.rect = pygame.Rect(x * 64, y * 64, 64, 64)
        self.x = x
        self.y = y
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def __del__(self):
        self.kill()


class Goal(Floor):
    def __init__(self, *groups, x, y):
        super().__init__(*groups, x=x, y=y)
        self.image = pygame.image.load('img/hole.png')
        self.image = pygame.transform.scale(self.image, [64, 64])
        self.rect = pygame.Rect(x * 64, y * 64, 64, 64)