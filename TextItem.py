import pygame

class TextItem:

    def __init__(self, x, y, width, height, text, color=(16, 65, 147), textColor=(90, 147, 243), CloseWhenClicked = False):
        self.fontObj = pygame.font.Font('freesansbold.ttf', 32)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.textColor = textColor
        self.setText(text)
        self.drawing = True
        self.color = color

    def draw(self, screen):
        if(self.drawing == True):
            pygame.draw.rect(screen, self.color, (
                self.x, self.y, self.width, self.height), 0)
            screen.blit(self.textObj, self.textRectObj)

    def setText(self, text):
        self.text = text
        self.textObj = self.fontObj.render(text, True, self.textColor)
        self.textRectObj = self.textObj.get_rect()
        self.textRectObj.center = (self.x + (self.width / 2), self.y + (self.height / 2))

    def is_under(self, pos):
        x, y = pos
        if (self.x < x and
            self.x + self.width > x and
            self.y < y and
            self.y + self.height > y
            ):
            #print 'You are under a button!'
            return pos
        else:
            return None

    def close(self):
        self.drawing = False

    def open(self):
        self.drawing = True
