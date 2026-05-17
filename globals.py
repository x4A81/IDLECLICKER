import pygame
import pygame.freetype

WIDTH, HEIGHT = 480, 270
SCALE = 3
WINDOW_WIDTH, WINDOW_HEIGHT = WIDTH * SCALE, HEIGHT * SCALE
FPS = 60

# Game State Variables
total_money = 0
profit = 10
tip_chance = 0.2
tip_amount = 50
profit_rate = 3
entities = []
volume = 1

pygame.init()
cursor = None
channel1 = pygame.mixer.Channel(1)
shop_bounds = pygame.Rect((WIDTH - 295), 20, 275, 230)
shop_surf = pygame.Surface((shop_bounds.width, shop_bounds.height))
shop_surf.fill((0, 255, 255))
pygame.freetype.set_default_resolution(72)
font = pygame.freetype.Font("assets/bytebounce.medium.ttf", 34)
font.antialiased = False
sprites = pygame.image.load("assets/Sprites.png")

def get_mouse_pos():
    x, y = pygame.mouse.get_pos()
    return x // SCALE, y // SCALE

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
        return "0"
        
    if amount % 1 == 0:
        return f"{int(amount)}{suffixes[suffix_index]}"
    else:
        return f"{amount:.1f}{suffixes[suffix_index]}"