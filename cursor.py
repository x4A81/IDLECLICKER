import pygame
import globals
class Cursor:
    def __init__(self):
        self.is_clicking = False
        self.frame_index = 0
        sheet = pygame.image.load("assets/Sprites.png")
        self.frames = []
        for i in range(1,4):
            img = sheet.subsurface((i * 32, 0, 32, 32))
            self.frames.append(img)

        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.click_sfx = pygame.mixer.Sound("assets/sounds/click.wav")
        self.play_sound = False
        self.hovering = False
        self.just_pressed = False

    def update(self, mouse_event : pygame.event):
        self.x, self.y = pygame.mouse.get_pos()
        self.x = self.x // globals.SCALE
        self.y = self.y // globals.SCALE
        
        self.rect.topleft = (self.x-18, self.y-18)
        self.play_sound = False
        if mouse_event != None and mouse_event.type == pygame.MOUSEBUTTONDOWN:
            self.is_clicking = True
            self.play_sound = True            
        elif mouse_event != None and mouse_event.type == pygame.MOUSEBUTTONUP:
            self.is_clicking = False

        if self.hovering:
            if self.is_clicking:
                self.frame_index = 2
            else:
                self.frame_index = 1
        else:
            self.frame_index = 0


        if self.play_sound:
            self.click_sfx.play()
            self.play_sound = False

    def set_hover(self, hover=True):
        self.hovering = hover

    def draw(self, surface):
        self.image = self.frames[self.frame_index]
        surface.blit(self.image, self.rect)