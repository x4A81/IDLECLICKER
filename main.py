from profiteffects import *
import pygame
import random
import globals
from globals import font

pygame.init()
screen = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT))
pygame.display.set_caption("NOODLE SHOP CLICKER")
clock = pygame.time.Clock()
bg_img = pygame.image.load("assets/background.png").convert()

next_profit_time = 1000 * globals.profit_rate
next_tip_time = 2000

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    surface.blit(textobj, (x, y))

while True:
    dt = clock.tick(globals.FPS)
    mouse_event = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_event = event

    screen.blit(bg_img, (0, 0))
    screen.blit(globals.shop_surf, (globals.WIDTH - 425, 25))

    next_profit_time -= dt
    next_tip_time -= dt
    if next_profit_time <= 0:
        add_profit()
        next_profit_time = 1000 * globals.profit_rate
    if next_tip_time <= 0:
        add_tip()
        next_tip_time = random.randint(3000, 7000)

    for et in globals.entities[:]:
        if et.isclickable:
            et.update(mouse_event)
        else:
            et.update()
        et.draw(screen)
        if et.kill:
            globals.entities.remove(et)
    draw_text(f"${globals.moola}", 
              font, (255, 255, 255), screen, 170 - 17 * len(f"${globals.moola}"), 490)
    pygame.display.flip()