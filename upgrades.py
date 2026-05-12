import pygame
import pygame.image
import globals

class Upgrade:
    def __init__(self, order, profit_inc, tip_chance_inc, cost, title, description):
        self.profit_inc = profit_inc
        self.tip_chance_inc = tip_chance_inc
        self.cost = cost
        self.isclickable = True
        self.ishoverable = True
        self.kill = False
        self.frames = []
        sheet = pygame.image.load("assets/sprites/upgrade-tile.png")
        for i in range(3):
            self.frames.append(sheet.subsurface(0, i * 64, 300, 64))
        self.img = self.frames[0]
        self.rect = self.img.get_rect()
        self.x = 20
        self.order = order
        self.y =  globals.HEIGHT
        self.rect.topleft = (self.x, self.y)
        self.title = title
        self.description = description

    def update(self, mouse_event : pygame.event):
        target_y = (64+10) * (self.order - 1) + 100
        if self.order > 4:
            self.x = -400
        else:
            self.x = 20
        
        if hasattr(self, 'current_y'):
            self.current_y += (target_y - self.current_y) * 0.3
        else:
            self.current_y = target_y
        self.rect.topleft = (self.x, self.current_y)
        self.img = self.frames[0]
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            globals.cursor.set_hover()
            self.img = self.frames[2]
            if mouse_event != None:
                if mouse_event.type == pygame.MOUSEBUTTONDOWN:
                    if globals.total_money >= self.cost:
                        self.kill = True
                        globals.total_money -= self.cost
                        globals.profit += self.profit_inc
                        globals.tip_chance += self.tip_chance_inc

    def draw(self, surface):
        if self.cost > globals.total_money:
            self.img = self.frames[1]
        surface.blit(self.img, self.rect)
        
        y = self.y
        if hasattr(self, "current_y"):
            y = self.current_y
        
        globals.font.size = 24
        globals.font.strong = True
        globals.font.render_to(surface,( self.x + 14, y + 12), self.title, (0,0,0))

        globals.font.strong = False
        globals.font.size = 14
        globals.font.render_to(surface, (self.x + 14, y + 38), self.description, (0,0,0))
        cost = globals.format_money(self.cost)
        globals.font_thai.render_to(surface, (self.rect.right - 90, y + 16), cost, (255, 255, 255))
