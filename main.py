'''
Hope For the Galaxy Classic
A game by Peter Nielsen (@peternielsen112)
Licensed under GNU General Public License 3.0 (see LICENSE.md for details)
For instructions on how to play, see README.md
Run this file with python3 main.py
'''

# import statements
import pgzrun
import random
import pygame
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
        self.view = 'splash'
        self.kills = 0
        self.deaths = 0
game = Game()

#actors
ship = Actor('xwing', (WIDTH/2, HEIGHT))
ship_height = HEIGHT - ship.height/2 - 5
ship.y = ship_height

tie = Actor('tiefighter', (WIDTH/2,HEIGHT/2))

laser = Actor('laser', (-WIDTH,-HEIGHT))

explosion = Actor('explosion', (-WIDTH,-HEIGHT))
explosion.active = False
explosion.inTimes = 0

#laser functions
def laser_motion(speed):
    laser.y -= speed
def fire():
    lasery = ship.y - ship.height/2 - laser.height/2
    laser.pos = (ship.x,lasery)
def reset_laser():
    laser.pos = (-HEIGHT, -WIDTH)

#end game
def end_game():
    print(f'\n\n\n\nGame Ended!\n\nScore: {game.score}\nKills: {game.kills}\nDeaths: {game.deaths}\nTie Speed: {SPEED + game.score / 3500}')

#stop score from going below zero
def score_check():
    if game.score < 0:
        game.score = 0

#get keyboard input
def get_keyboard(speed):
    if keyboard.left:
        ship.x -= speed
    elif keyboard.right:
        ship.x += speed
    elif keyboard.space:
        fire()
    elif keyboard.down and game.view == 'splash':
        game.score = 0
        game.kills = 0
        game.deaths = 0
        game.view = 'level-1'
    elif keyboard.q:
        end_game()
        quit()

#tie motion
def tie_motion(TIE_SPEED):
    tie.y += TIE_SPEED

#reset tie
def reset_tie():
    explosion.active = True
    explosion.pos = tie.pos
    tiestart = random.randint(5,WIDTH-5)
    tie.pos = (tiestart, 0)

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
        game.score -= 100
        reset_tie()

#testing hits
def test_hit():
    if tie.colliderect(ship):
        death()
        reset_tie()
    elif tie.colliderect(laser):
        reset_laser()
        game.score += round(100+tie.x/5)
        game.kills += 1
        reset_tie()

def explosion_check():
    if explosion.active == True:
        if explosion.inTimes >= 15:
            explosion.active = False
            explosion.pos = (-WIDTH, -HEIGHT)
            explosion.inTimes = 0
        else:
            explosion.inTimes += 1

#mainloop
def update():
    get_keyboard(SPEED)
    out_screen()
    tie_motion(SPEED + game.score / 3500)
    test_hit()
    laser_motion(SPEED)
    score_check()
    explosion_check()
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
        explosion.draw()
        screen.draw.text(str(f'Score: {game.score}'), (WIDTH/20, HEIGHT/20))
        screen.draw.text(str(f'Kills: {game.kills}'), (WIDTH/20, HEIGHT/30 - 5))
        screen.draw.text(str(f'Deaths: {game.deaths}'), (WIDTH/20, HEIGHT/10 - 15))
        screen.draw.text(str(f'Tie Speed: {round(SPEED + game.score / 3500)}'), (WIDTH/20, HEIGHT/10))
pgzrun.go()
end_game()