WIDTH, HEIGHT = 800, 600
FPS = 60

moola = 0
profit = 10
profit_rate = 3
entities = []

import pygame
pygame.init()
shop_bounds = pygame.Rect(WIDTH - 425, 25, 400, 550)
shop_surf = pygame.Surface((400, 550))
shop_surf.fill((0, 255, 255))
font = pygame.font.Font("assets/NotoSansThai-Bold.ttf", 45)