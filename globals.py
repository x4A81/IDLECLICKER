WIDTH, HEIGHT = 800, 600
FPS = 60

total_money = 0
profit = 40
tip_chance = 0.2
tip_amount = 200
profit_rate = 3
entities = []

import pygame
pygame.init()
cursor = None
shop_bounds = pygame.Rect(WIDTH - 425, 25, 400, 550)
shop_surf = pygame.Surface((400, 550))
shop_surf.fill((0, 255, 255))
font = pygame.font.Font("assets/NotoSansThai-Bold.ttf", 45)