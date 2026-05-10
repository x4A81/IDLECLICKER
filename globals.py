WIDTH, HEIGHT = 800, 600
FPS = 60

moola = 0
profit = 10
profit_rate = 3
entities = []

import pygame
pygame.init()
shop_surf = pygame.Surface((400, 550))
shop_surf.fill((0, 255, 255))
font = pygame.font.SysFont("arial", 45)