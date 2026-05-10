import pygame
import globals

import random

def add_profit(a=10, x=None, y=400):
    globals.moola += a
    rx = 10 + random.randint(globals.shop_bounds.left+75, globals.shop_bounds.right-75) if x == None else x
    globals.entities.append(ProfitEffects(rx, y, a))

def add_tip(a=50, x=None, y=350):
    rx = 10 + random.randint(globals.shop_bounds.left+75, globals.shop_bounds.right-75) if x == None else x
    globals.entities.append(Tips(rx, y, a))

class ProfitEffects:
    def __init__(self, x, y, amount):
        self.isclickable = False
        self.x = x
        self.y = y
        self.text = f"+{amount}฿"
        self.alpha = 255
        self.font = pygame.font.Font("assets/NotoSansThai-Bold.ttf", 36)
        self.colour = (0, 0, 0, self.alpha)
        self.kill = False

    def update(self):
        self.y -= 1  # Move the text up
        self.alpha -= 5
        if self.alpha <= 0:
            self.kill = True

    def draw(self, surface):
        text_surf = self.font.render(self.text, True, (0, 0, 0))
        # Create a copy to apply transparency
        final_surf = text_surf.convert_alpha()
        final_surf.set_alpha(self.alpha)
        
        surface.blit(final_surf, (self.x, self.y))

import random
from pygame.math import Vector2

class Tips:
    def __init__(self, x, y, amount):
        self.isclickable = True
        self.x = x
        self.y = y
        self.amount = amount
        self.vel = Vector2(random.uniform(-3, 3), random.uniform(-2, -6))
        self.colour = (200, 200, 0)
        self.kill = False
        self.img = pygame.image.load("assets/sprites/coin.png")
        self.img = pygame.transform.scale_by(self.img, 2)
        self.rect = self.img.get_rect()

    def update(self, mouse_event : pygame.event):
        if mouse_event != None and mouse_event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.kill = True
                add_profit(self.amount, self.x-10, self.y - 10)
                return

        g = 0.2
        if self.y > 500: 
            return
        if self.x < globals.shop_bounds.left + 37 or self.x > globals.shop_bounds.right - 37:
            return
        if self.y >= 0:
            self.vel.y += g * 1.5
        else:
            self.vel.y += g
        self.y += self.vel.y
        self.x += self.vel.x
        self.rect.center = (self.x, self.y)

    def draw(self, surface):
        surface.blit(self.img, self.rect)