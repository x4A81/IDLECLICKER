import pygame
import globals

class Settings:
    def __init__(self):
        self.x, self.y = 15, 185
        self.icons = []
        for i in range(5):
            self.icons.append(globals.sprites.subsurface((8 + 2*i) * 16, 32, 16, 16))

        self.settings_pressed = False
        self.isclickable = True

        self.rects = []
        for i in range(5):
            self.rects.append(self.icons[i].get_rect())
            self.rects[i].topleft = (self.x + 25*i, self.y)


    def update(self, mouse_event):
        if mouse_event == None:
            return
        if self.rects[0].collidepoint(globals.get_mouse_pos()) and mouse_event.type == pygame.MOUSEBUTTONDOWN:
            self.settings_pressed = not self.settings_pressed

        if not self.settings_pressed:
            return
        
        for rect in self.rects:
            if rect.collidepoint(globals.get_mouse_pos()) and mouse_event.type == pygame.MOUSEBUTTONDOWN:
                if rect == self.rects[1]:
                    globals.volume = 0.3
                if rect == self.rects[2]:
                    globals.volume = 0.6
                if rect == self.rects[3]:
                    globals.volume = 1
                if rect == self.rects[4]:
                    globals.volume = 0
            
                globals.channel1.set_volume(globals.volume)

    def draw(self, surface):
        surface.blit(self.icons[0], self.rects[0])
        if self.settings_pressed:
            i = 1
            for rect in self.rects[1:]:
                surface.blit(self.icons[i], rect)
                i += 1
