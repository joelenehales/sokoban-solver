import pygame
from .box import Box, Obstacle

SPRITE_SIZE_PIX = 64

class Player(pygame.sprite.Sprite):
    """ Class representing the player.
    
    Sprite loading/movement code largely from:
    https://github.com/xbandrade/sokoban-solver-generator/blob/main/src/player.py
    
    """

    def __init__(self, *groups, x, y, game):
        """ Creates an instance of the player. 
        
        Parameters
        ----------
        *groups : Pygame groups
        x : Player's x coordinate
        y : Player's y coordinate
        game : Instance of Sokoban game
        
        """

        super().__init__(*groups)
        self.game = game

        # Load sprite images
        self.up = pygame.image.load('img/player_up.png')
        self.down = pygame.image.load('img/player_down.png')
        self.left = pygame.image.load('img/player_left.png')
        self.right = pygame.image.load('img/player_right.png')

        # Resize        
        self.up = pygame.transform.scale(self.up, [SPRITE_SIZE_PIX, SPRITE_SIZE_PIX])
        self.down = pygame.transform.scale(self.down, [SPRITE_SIZE_PIX, SPRITE_SIZE_PIX])
        self.left = pygame.transform.scale(self.left, [SPRITE_SIZE_PIX, SPRITE_SIZE_PIX])
        self.right = pygame.transform.scale(self.right, [SPRITE_SIZE_PIX, SPRITE_SIZE_PIX])
        
        # Initialize image
        self.image = self.down

        # Set position
        self.rect = pygame.Rect(x * SPRITE_SIZE_PIX, y * SPRITE_SIZE_PIX, SPRITE_SIZE_PIX, SPRITE_SIZE_PIX)
        self.x = x
        self.y = y

    def update(self, key=None):
        """ Updates the player's position and sprite to match. 
        
        Parameters
        ----------
        key : Character representing directional move.
                Up:    'U'
                Down:  'D'
                Left:  'L'
                Right: 'R' 
        
        Returns
        -------
        1 if player made a move, or 0 otherwise

        """

        # Define direction to move in
        move = None
        if key:
            if key == 'R':
                self.image = self.right
                move = (SPRITE_SIZE_PIX, 0)
            elif key == 'L':
                self.image = self.left
                move = (-SPRITE_SIZE_PIX, 0)
            elif key == 'U':
                self.image = self.up
                move = (0, -SPRITE_SIZE_PIX)
            elif key == 'D':
                self.image = self.down
                move = (0, SPRITE_SIZE_PIX)
        
        # Make move
        if move:
            curr = self.y, self.x
            target_tile = self.y + move[1] // SPRITE_SIZE_PIX, self.x + move[0] // SPRITE_SIZE_PIX
            target_elem = self.game.puzzle[target_tile]
            is_obstacle = isinstance(target_elem.obj, Obstacle)
            
            if not (target_elem and target_elem.obj and is_obstacle): # Not against an obstacle
                
                is_box = isinstance(target_elem.obj, Box)
                if not is_box or (is_box and target_elem.obj.can_move(move)):  # Empty space or moveable box
                    curr_elem = self.game.puzzle[curr]
                    self.rect.y, self.rect.x = target_tile[0] * SPRITE_SIZE_PIX, target_tile[1] * SPRITE_SIZE_PIX
                    self.y, self.x = target_tile

                    # Move box off space player is moving from
                    curr_elem.char = '-' if not curr_elem.ground else 'O'  
                    curr_elem.obj = None

                    # Move player to new tile
                    target_elem.char = 'P' if not target_elem.ground else '%'
                    target_elem.obj = self
                    return 1  # Player moved
    
        return 0  # Player did not move
    
    def __del__(self):
        """ Deletes instance of player. """
        self.kill()