import pygame
from Button import Button

class Container(Button):

    # Takes in drawing co-ordinates, height/width, background/fill colors, and
    # how much it is filled up
    def __init__(self, x, y, numerator=0, denominator=0, width=130, height=200, showText = True, \
                 color=(215, 54, 54), bg=(50, 50, 50)):
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
        base_filename = "assets/Eigthmeterbase.png"
        shade_filename = "assets/Eigthmetershading.png"
        self.base_surface = pygame.image.load(base_filename).convert_alpha()
        self.shade_surface = pygame.image.load(shade_filename).convert_alpha()

        scale = (int(width),int(height));
        self.base_surface= pygame.transform.scale(self.base_surface, scale)
        self.shade_surface = pygame.transform.scale(self.shade_surface, scale)

    def helperSelect(self):
        self.selected = not self.selected
        return self.selected

    # Take in filled percentage as a decimal, multiply it by the height of
    # container to get pixel height
    def fill(self, percent):
        self.filled = float(percent)
        self.fillHeight = round(self.filled * self.height)
        if(self.showText):
            self.text = str(self.numerator)+"/"+str(self.denominator)
            self.textObj = self.fontObj.render(self.text, True, (80, 204, 80))
            self.textRectObj = self.textObj.get_rect()
            self.textRectObj.center = (
                self.x + (self.width / 2), self.y + (self.height / 2))

    def draw(self, screen):
        screen.blit(self.base_surface,(self.x, self.y, 20, self.height))
        color = self.bg
        if self.selected:
            color = (0,0,0)
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height), 0)
        color = self.color
        if self.selected:
            color = (50,50,50)
        pygame.draw.rect(screen, color, (self.x, self.y + (self.height - self.fillHeight), self.width, self.fillHeight), 0)
        screen.blit(self.shade_surface,(self.x, self.y, 20, self.height))
        if(self.showText):
            screen.blit(self.textObj, self.textRectObj)

    
