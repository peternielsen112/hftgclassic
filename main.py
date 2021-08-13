# import statements
import pgzrun
from pygame.locals import *

#constants
WIDTH = 585
HEIGHT = 700
SPEED = 5
BACKGROUND_IMAGE = 'background1'

#game class definition
class Game():
    def __init__(self):
        self.score = 0
        self.mode = 'endless'
        self.view = 'spash'
        self.end = False
        self.kills = 0
        self.deaths = 0
        self.quota = -1
game = Game()

#actors
ship = Actor('xwing', (WIDTH/2, HEIGHT))
ship.y = HEIGHT - ship.height/2

tie = Actor('tiefighter', (WIDTH/2,HEIGHT/2))

#get keyboard input
def get_keyboard(speed):
    if keyboard.left:
        ship.x -= speed
    elif keyboard.right:
        ship.x += speed

#mainloop
def update():
    get_keyboard(SPEED)
def draw():
    if game.view == 'splash':
        screen.clear()
        screen.blit('logo', (WIDTH * 0.08,HEIGHT/3))
        screen.draw.text(str('<Press the DOWN key to begin>'), (WIDTH - 400, HEIGHT - 30))
    else:
        screen.clear()
        screen.blit('background1', (0,0))
        ship.draw()
        tie.draw()
pgzrun.go()