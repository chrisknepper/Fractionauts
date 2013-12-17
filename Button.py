import pygame


class Button:

    def __init__(self, x, y, width, height, text, color=(16, 65, 147), textColor=(90, 147, 243)):
        self.fontObj = pygame.font.Font('freesansbold.ttf', 32)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.textColor = textColor
        self.textObj = self.fontObj.render(text, True, self.textColor)
        self.textRectObj = self.textObj.get_rect()
        self.textRectObj.center = (x + (width / 2), y + (height / 2))
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (
            self.x, self.y, self.width, self.height), 0)
        screen.blit(self.textObj, self.textRectObj)

    def is_under(self, pos):
        x, y = pos
        if (self.x < x and
            self.x + self.width > x and
            self.y < y and
            self.y + self.height > y
            ):
            return pos
        else:
            return None
