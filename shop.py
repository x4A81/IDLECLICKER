import globals
from upgrades import Upgrade
import pygame
class Shop:
    def __init__(self):
        self.setup_upgrades()
        self.images = []
        for i in range(3):
            self.images.append(pygame.image.load(f"assets/ShopBG{i+1}.png"))
        self.images.append(pygame.image.load("assets/ShopStand.png"))

    def setup_upgrades(self):
        globals.entities.append(Upgrade(1, 10, 0, 100, "Plastic Stools", "+10 profit"))
        globals.entities.append(Upgrade(2, 0, 0.02, 500, "Old Sign", "+2% Tip Chance"))

        globals.entities.append(Upgrade(3, 0, 0.05, 1500, "Radio", "+5% Tip Chance"))
        globals.entities.append(Upgrade(4, 15, 0, 1700, "Tables", "+15 profit"))

        globals.entities.append(Upgrade(5, 0, 0.07, 1500, "Chalk Board", "+7% Tip Chance"))
        globals.entities.append(Upgrade(6, 17, 0, 20000, "Cushions", "+17 profit"))

        globals.entities.append(Upgrade(7, 0, 0.1, 1500, "Upgrade Sign", "+10% Tip Chance"))
        globals.entities.append(Upgrade(8, 20, 0, 40000, "Wooden Stools", "+20 profit"))

        globals.entities.append(Upgrade(9, 0, 0.15, 2000, "Table Cloth", "+15% Tip Chance"))
        globals.entities.append(Upgrade(10, 30, 0, 60000, "Extra Stove", "+30 profit"))

    def draw(self, screen):
        for i in range(4):
            screen.blit(self.images[i], (globals.WIDTH//2 - self.images[i].get_width()//2, globals.HEIGHT//2 - self.images[i].get_height()//2))
    
    def draw_image(self, surface, image):
        surface.blit(self.images[image], (globals.WIDTH//2 - self.images[image].get_width()//2, globals.HEIGHT//2 - self.images[image].get_height()//2))

from random import randint as rand
class BG_Leaves:
    def __init__(self):
        self.x = rand(globals.shop_bounds.left+25, globals.shop_bounds.right-25)
        self.y = globals.shop_bounds.top+5
        
        self.images = []
        self.images.append(globals.sprites.subsurface((18 * 16, 2*16, 16, 16)))
        self.images.append(globals.sprites.subsurface((20 * 16, 2*16, 16, 16)))
        self.image = self.images[rand(0, len(self.images) - 1)]
        self.rect = self.image.get_rect()
        self.g = 0.7
        self.angle = rand(0, 45)
        self.rot_speed = 2
        self.img_c = self.image
        self.kill = False

    def update(self):
        self.y += self.g
        self.g *= 1.005

        if self.angle < 180:
            self.angle += self.rot_speed
            
            self.rot_speed *= 0.98 
            
            self.img_c = pygame.transform.rotate(self.image, self.angle)
            
            old_center = self.rect.center
            self.rect = self.img_c.get_rect()
            self.rect.center = old_center

        self.rect.y = self.y
        self.rect.x = self.x

        if self.y > globals.shop_bounds.bottom-100:
            self.kill = True
            globals.leaves_spawned -= 1

    def draw(self, screen):
        screen.blit(self.img_c, self.rect)