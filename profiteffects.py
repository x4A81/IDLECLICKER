import pygame
import random
import globals

def add_profit(a=40, x=None, y=globals.WIDTH - 250, text=None, d=0):
    globals.total_money += a
    rx = 10 + random.randint(globals.shop_bounds.left+25, globals.shop_bounds.right-25) if x == None else x
    globals.entities.append(ProfitEffects(rx, y, a, text, d))

def add_tip(a=200, x=None, y=globals.HEIGHT - 140):
    rx = 10 + random.randint(globals.shop_bounds.left+10, globals.shop_bounds.right-10) if x == None else x
    globals.entities.append(Tips(rx, y, a))

class ProfitEffects:
    def __init__(self, x, y, amount, text=None, d=0):
        self.x = x
        self.y = y
        self.text = f"+{amount}" if not text else text
        self.alpha = 255
        self.font = globals.font
        self.colour = (0, 0, 0, self.alpha)
        self.kill = False
        self.duration = 1-d

    def update(self):
        self.y -= 1  # Move the text up
        self.alpha -= 5 * self.duration
        if self.alpha <= 0:
            self.kill = True

    def draw(self, surface):
        text_surf = self.font.render(self.text, (0, 0, 0))
        # Create a copy to apply transparency
        final_surf = text_surf[0].convert_alpha()
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
        sheet = globals.sprites
        self.img = sheet.subsurface((0,32,16,16))
        self.rect = self.img.get_rect(center=(self.x, self.y))

    def update(self, mouse_event : pygame.event):
        if mouse_event != None and mouse_event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(globals.get_mouse_pos()):
                self.kill = True
                add_profit(self.amount, self.x-10, self.y - 10)
                return

        g = 0.2
        if self.y > globals.WIDTH - 250: 
            return
        if self.x < globals.shop_bounds.left + 10 or self.x > globals.shop_bounds.right - 10:
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