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
ship_height = HEIGHT - ship.height/2 - 5
ship.y = ship_height

tie = Actor('tiefighter', (WIDTH/2,HEIGHT/2))

laser = Actor('laser', (-WIDTH,-HEIGHT))

#laser functions
def laser_motion(speed):
    laser.y -= speed
def fire():
    lasery = ship.y - ship.height/2 - laser.height/2
    laser.pos = (ship.x,lasery)

#get keyboard input
def get_keyboard(speed):
    if keyboard.left:
        ship.x -= speed
    elif keyboard.right:
        ship.x += speed
    elif keyboard.space:
        fire()

#tie motion
def tie_motion():
    tie_speed = 7 + game.score / 500
    tie.y += tie_speed

#reset tie
def reset_tie():
    tie.pos = (WIDTH/2, 0)

#death
def death():
    ship.pos = (WIDTH/2, ship_height)
    game.score -= 100
    game.deaths += 1

#out of screen function
def out_screen():
    if ship.x < 0 or ship.x > WIDTH:
        death()
    elif tie.y > HEIGHT:
        reset_tie()

#testing hits
def test_hit():
    if tie.colliderect(ship):
        death()
        reset_tie()

#mainloop
def update():
    get_keyboard(SPEED)
    out_screen()
    tie_motion()
    test_hit()
    laser_motion(SPEED)
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
        laser.draw()
pgzrun.go()