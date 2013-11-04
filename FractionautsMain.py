#!/usr/bin/python
#Fractionauts Main Class
import pygame
from gi.repository import Gtk

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

class Button:

    def __init__(self, x, y, width, height, text, color=BLUE):
        self.fontObj = pygame.font.Font('freesansbold.ttf', 32)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = self.fontObj.render(text, True, GREEN)
        self.textRectObj = self.text.get_rect()
        self.textRectObj.center = (x + (width / 2), y + (height / 2))
        self.color = color


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)
        screen.blit(self.text, self.textRectObj);

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



class FractionautsMain:
    def __init__(self):
        # Set up a clock for managing the frame rate.
        self.clock = pygame.time.Clock()
        self.buttons = []

        self.x = -100
        self.y = 100

        self.vx = 10
        self.vy = 0

        self.paused = False
        self.direction = 1
        self.btn = Button(300, 300, 200, 100, 'Other stuff!')
        self.buttons.append(self.btn);

    def on_click_me_clicked(self, button):
        print "\"Click me\" button was clicked"

    def set_paused(self, paused):
        self.paused = paused

    # Called to save the state of the game to the Journal.
    def write_file(self, file_path):
        pass

    # Called to load the state of the game from the Journal.
    def read_file(self, file_path):
        pass


    # The main game loop.
    def run(self):
        self.running = True

        screen = pygame.display.get_surface()

        fontObj = pygame.font.Font('freesansbold.ttf', 32)
        textSurfaceObj = fontObj.render('Fractionauts', True, GREEN, BLUE)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (200, 150)


        while self.running:
            # Pump GTK messages.
            while Gtk.events_pending():
                Gtk.main_iteration()

            # Pump PyGame messages.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.VIDEORESIZE:
                    pygame.display.set_mode(event.size, pygame.RESIZABLE)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.direction = -1
                    elif event.key == pygame.K_RIGHT:
                        self.direction = 1
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    #TODO: loop through buttons and check for colisions
                    for button in self.buttons:
                        if button.is_under(pygame.mouse.get_pos()):
                            print 'YOU JUST CLICKED THE BUTTON'

            # Move the ball
            if not self.paused:
                self.x += self.vx * self.direction
                if self.direction == 1 and self.x > screen.get_width() + 100:
                    self.x = -100
                elif self.direction == -1 and self.x < -100:
                    self.x = screen.get_width() + 100

                self.y += self.vy
                if self.y > screen.get_height() - 100:
                    self.y = screen.get_height() - 100
                    self.vy = -self.vy

                self.vy += 5

            # Clear Display
            screen.fill((255, 255, 255))  # 255 for white

            screen.blit(textSurfaceObj, textRectObj);

            # Draw the ball
            pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 100)
            self.btn.draw(screen);

            # Flip Display
            pygame.display.flip()

            # Try to stay at 30 FPS
            self.clock.tick(30)




# This function is called when the game is run directly from the command line:
# ./FractionautsMain.py
def main():
    pygame.init()
    pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    game = FractionautsMain()
    game.run()

if __name__ == '__main__':
    main()
