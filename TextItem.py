import pygame

class TextItem:

    def __init__(self, x, y, width, height, text, color=(16, 65, 147), textColor=(90, 147, 243), CloseWhenClicked = False, background = False, showRect = True, fontSize = 32):
        self.fontObj = pygame.font.Font('freesansbold.ttf', fontSize)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.textColor = textColor
        self.textObj = []
        self.textRectObj = []
        self.setText(text)
        self.drawing = True
        self.color = color
        self.showRect = showRect
        self.background = background

    def draw(self, screen): #Draw the rectange, then the background image, then the text lines
        if(self.drawing == True):
            if(self.showRect != False):
                pygame.draw.rect(screen, self.color, (
                    self.x, self.y, self.width, self.height), 0)
            if(self.background != False):
                self.background.draw(screen)
            counter = 0;
            for text in self.textObj:
                screen.blit(text, self.textRectObj[counter])
                counter = counter + 1  

    def setText(self, text):
        self.text = text
        counter = 0
        if(len(self.text) > 1):
            for line in self.text:
                temp_text = self.fontObj.render(line, True, self.textColor)
                self.textObj.append(temp_text)
                temp_rect = temp_text.get_rect()
                temp_rect.center = (self.x + (self.width / 2), self.y + 40 + (counter * 40))
                self.textRectObj.append(temp_rect)
                counter = counter + 1
        else:
            self.textObj = [self.fontObj.render(self.text[0], True, self.textColor)]
            self.textRectObj = [self.textObj[0].get_rect()]
            self.textRectObj[0].center = (self.x + (self.width / 2), self.y + (self.height / 2))

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
