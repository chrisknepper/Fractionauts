import pygame


class Container:

    # Takes in drawing co-ordinates, height/width, background/fill colors, and
    # how much it is filled up
    def __init__(self, x, y, width, height, filled=0.0, color=(255, 0, 0), bg=(50, 50, 50)):
        self.fontObj = pygame.font.Font('freesansbold.ttf', 32)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fill(filled)
        self.color = color
        self.bg = bg

    # Take in filled percentage as a decimal, multiply it by the height of
    # container to get pixel height
    def fill(self, percent):
        self.filled = percent
        self.fillHeight = round(self.filled * self.height)
        self.text = str(round(self.filled * 100))
        self.textObj = self.fontObj.render(self.text, True, (0, 255, 0))
        self.textRectObj = self.textObj.get_rect()
        self.textRectObj.center = (
            self.x + (self.width / 2), self.y + (self.height / 2))

    def draw(self, screen):
        pygame.draw.rect(
            screen, self.bg, (self.x, self.y, self.width, self.height), 0)
        pygame.draw.rect(screen, self.color, (
            self.x, self.y + (self.height - self.fillHeight), self.width, self.fillHeight), 0)
        screen.blit(self.textObj, self.textRectObj)
