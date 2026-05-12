WIDTH, HEIGHT = 800, 600
FPS = 60

total_money = 0
profit = 40
tip_chance = 0.2
tip_amount = 200
profit_rate = 3
entities = []

import pygame
import pygame.freetype
pygame.init()
cursor = None
shop_bounds = pygame.Rect(WIDTH - 425, 25, 400, 550)
shop_surf = pygame.Surface((400, 550))
shop_surf.fill((0, 255, 255))
font_thai = pygame.freetype.Font("assets/NotoSansThai-Bold.ttf", 30)
font = pygame.freetype.Font("assets/VarelaRound-Regular.ttf", 24)

def format_money(amount):
    """
    Converts 1000 to 1k, 1000000 to 1M, etc.
    """
    # Define suffixes for Thousands, Millions, Billions, Trillions
    suffixes = ['', 'k', 'M', 'B', 'T']
    suffix_index = 0

    # Keep dividing by 1000 until the number is under 1000
    # or we run out of suffixes
    while abs(amount) >= 1000 and suffix_index < len(suffixes) - 1:
        amount /= 1000.0
        suffix_index += 1

    # Formatting the string:
    # If it's a whole number, show no decimals (e.g., 1k)
    # If it has a remainder, show 1 decimal place (e.g., 1.5k)
    if amount == 0:
        return "฿0"
        
    if amount % 1 == 0:
        return f"฿{int(amount)}{suffixes[suffix_index]}"
    else:
        return f"฿{amount:.1f}{suffixes[suffix_index]}"