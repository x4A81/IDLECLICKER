from profiteffects import *
from music import *
from cursor import Cursor
from upgrades import *
import pygame
import random
import globals
from globals import font

pygame.init()
screen = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT))
pygame.display.set_caption("NOODLE SHOP CLICKER")
clock = pygame.time.Clock()
bg_img = pygame.image.load("assets/sprites/background.png").convert()

next_profit_time = 1000 * globals.profit_rate
next_tip_time = 2000

pygame.mouse.set_visible(False)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    surface.blit(textobj, (x, y))

play_next_song()
globals.cursor = Cursor()
globals.entities.append(Upgrade(1, 10, 0, 100))
globals.entities.append(Upgrade(2, 0, 0.02, 150))

while True:
    dt = clock.tick(globals.FPS)
    mouse_event = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEMOTION:
            mouse_event = event

        if event.type == SONG_END:
            play_next_song()

    screen.blit(bg_img, (0, 0))
    screen.blit(globals.shop_surf, (globals.WIDTH - 425, 25))
    globals.cursor.set_hover(False)
    next_profit_time -= dt
    next_tip_time -= dt
    if next_profit_time <= 0:
        add_profit(globals.profit)
        next_profit_time = 1000 * globals.profit_rate
    if next_tip_time <= 0:
        if random.uniform(0, 1) <= globals.tip_chance: add_tip()
        next_tip_time = 3000

    for et in globals.entities[:]:
        if et.isclickable:
            et.update(mouse_event)
        else:
            et.update()
        et.draw(screen)
        if et.kill:
            globals.entities.remove(et)
    draw_text(f"{globals.moola}฿", 
              font, (255, 255, 255), screen, 170 - 17 * len(f"{globals.moola}฿"), 475)

    globals.cursor.update(mouse_event)
    globals.cursor.draw(screen)
    pygame.display.flip()