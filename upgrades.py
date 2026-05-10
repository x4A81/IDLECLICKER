import pygame
import globals

class Upgrade:
    def __init__(self, order, profit_inc, tip_chance_inc, cost):
        self.x = 20
        self.y = 50 * order
        self.profit_inc = profit_inc
        self.tip_chance_inc = tip_chance_inc
        self.cost = cost
        self.isclickable = True
        self.ishoverable = True
        self.kill = False
        self.rect = pygame.Rect(self.x, self.y, 300, 30)
        self.bought = False

    def update(self, mouse_event : pygame.event):
        if self.bought: return
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            globals.cursor.set_hover()
            if mouse_event != None:
                if mouse_event.type == pygame.MOUSEBUTTONDOWN:
                    if globals.moola >= self.cost:
                        self.bought = True
                        globals.moola -= self.cost
                        globals.profit += self.profit_inc
                        globals.tip_chance += self.tip_chance_inc

    def draw(self, surface):
        if self.bought:
            pygame.draw.rect(surface, (100, 100, 100), self.rect)
        else:
            pygame.draw.rect(surface, (255, 255, 255), self.rect)