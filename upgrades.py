import pygame
import globals
from profiteffects import add_profit

class Upgrade:
    def __init__(self, order, profit_inc, tip_chance_inc, cost, title, description):
        self.profit_inc = profit_inc
        self.tip_chance_inc = tip_chance_inc
        self.cost = cost
        self.isclickable = True
        self.ishoverable = True
        self.kill = False
        self.frames = []
        sheet = globals.sprites
        for i in range(3):
            self.frames.append(sheet.subsurface(8, 8*7 + i * 32, 18*8, 64))
        self.img = self.frames[1]
        self.rect = self.img.get_rect()
        self.x = 8
        self.order = order
        self.y = globals.HEIGHT
        self.rect.topleft = (self.x, self.y)
        self.title = title
        self.description = description

    def update(self, mouse_event : pygame.event):
        target_y = (32) * (self.order - 1) + 50
        if self.order > 4:
            self.x = -400
        else:
            self.x = 8
        
        if hasattr(self, 'current_y'):
            self.current_y += (target_y - self.current_y) * 0.3
        else:
            self.current_y = target_y
        self.rect.topleft = (self.x, self.current_y)
        self.img = self.frames[1]
        if self.rect.collidepoint(globals.get_mouse_pos()):
            globals.cursor.set_hover()
            self.img = self.frames[0]
            if mouse_event != None:
                if mouse_event.type == pygame.MOUSEBUTTONDOWN:
                    if globals.total_money >= self.cost:
                        self.kill = True
                        globals.total_money -= self.cost
                        globals.profit += self.profit_inc
                        globals.tip_chance += self.tip_chance_inc
                        add_profit(globals.profit, x=250, text=self.description, d=0.3)

    def draw(self, surface):
        if self.cost > globals.total_money:
            self.img = self.frames[2]
        surface.blit(self.img, self.rect)
        
        y = self.y
        if hasattr(self, "current_y"):
            y = self.current_y
        
        globals.font.size = 15
        globals.font.render_to(surface,( self.x + 16, y + 12), self.title, (255,255,255))
        cost = globals.format_money(self.cost)
        globals.font.render_to(surface, (self.rect.right - 40, y + 12), cost, (255, 255, 255))

        # globals.font.size = 10
        # globals.font.render_to(surface, (self.x + 14, y + 20), self.description, (0,0,0))
        globals.font.size = 34
