import pygame
from Button import Button

class Container(Button):

    # Takes in drawing co-ordinates, height/width, background/fill colors, and
    # how much it is filled up
    def __init__(self, x, y, numerator=0, denominator=0, width=177, height=259, showText = True, \
                 color=(255, 0, 0), bg=(50, 50, 50)):
        self.fontObj = pygame.font.Font('freesansbold.ttf', 32)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.showText = showText
        self.selected = False
        self.numerator = numerator
        self.denominator = denominator
        self.fill(float(numerator)/float(denominator))
        self.color = color
        self.bg = bg

    # Take in filled percentage as a decimal, multiply it by the height of
    # container to get pixel height
    def fill(self, percent):
        self.filled = float(percent)
        self.fillHeight = round(self.filled * self.height)
        if(self.showText):
            self.text = str(self.numerator)+"/"+str(self.denominator)
            self.textObj = self.fontObj.render(self.text, True, (0, 255, 0))
            self.textRectObj = self.textObj.get_rect()
            self.textRectObj.center = (
                self.x + (self.width / 2), self.y + (self.height / 2))

    def draw(self, screen):
        base_filename = "assets/Eigthmeterbase.png"
        base_surface = pygame.image.load(base_filename)
        shade_filename = "assets/Eigthmetershading.png"
        shade_surface = pygame.image.load(shade_filename)
        screen.blit(base_surface,(self.x, self.y, 20, self.height))
        color = self.bg
        if self.selected:
            color = (0,0,0)
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height), 0)
        color = self.color
        if self.selected:
            color = (50,50,50)
        pygame.draw.rect(screen, color, (self.x, self.y + (self.height - self.fillHeight), self.width, self.fillHeight), 0)
        screen.blit(shade_surface,(self.x, self.y, 20, self.height))
        if(self.showText):
            screen.blit(self.textObj, self.textRectObj)

    
