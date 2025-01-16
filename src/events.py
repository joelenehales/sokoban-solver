# From: https://github.com/xbandrade/sokoban-solver-generator/blob/main/src/events.py

import pygame

RESTART_EVENT = pygame.USEREVENT + 1
PREVIOUS_EVENT = pygame.USEREVENT + 2
NEXT_EVENT = pygame.USEREVENT + 3
SOLVE_DFS_EVENT = pygame.USEREVENT + 4
SOLVE_ASTARMAN_EVENT = pygame.USEREVENT + 5