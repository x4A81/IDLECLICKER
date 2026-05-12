from profiteffects import *
from music import *
from cursor import Cursor
from upgrades import *
import pygame
import random
import globals
from globals import font_thai
import shop

pygame.init()
screen = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT))
pygame.display.set_caption("NOODLE SHOP CLICKER")
clock = pygame.time.Clock()
bg_img = pygame.image.load("assets/sprites/background.png").convert()

next_profit_time = 1000 * globals.profit_rate
next_tip_time = 2000

pygame.mouse.set_visible(False)

def draw_text(text, font, colour, surface, rect):
    font.render_to(surface, rect, text, colour)

play_next_song()
globals.cursor = Cursor()
shop.setup_upgrades()

deleted_update = 0
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
        if random.uniform(0, 1) <= globals.tip_chance: add_tip(globals.tip_amount)
        next_tip_time = 3000

    for et in globals.entities[:]:
        if et.isclickable:
            et.update(mouse_event)
        else:
            et.update()
        et.draw(screen)
        if et.kill:
            if hasattr(et, "order"):
                deleted_update = et.order
                globals.entities.remove(et)
            
                for other in globals.entities:
                    if isinstance(other, Upgrade) and other.order > deleted_update:
                        other.order -= 1
            else:
                globals.entities.remove(et)

    money_st = globals.format_money(globals.total_money)
    draw_text(money_st, 
              font_thai, (255, 255, 255), screen, (167 - 17 * len(money_st), 495))

    globals.cursor.update(mouse_event)
    globals.cursor.draw(screen)
    pygame.display.flip()