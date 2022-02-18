from re import X
import pygame
from pygame.locals import *
from sys import exit

# Initialize pygame for game machanics
pygame.init()
# Initialize pygame for game sounds
pygame.mixer.init()

s_width = 900
s_height =800       #1010
screen = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption("BREAKOUT")

player_x = 450
player_y = 740

def main_game():
    while True:
        global player_x
        global player_y
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            pygame.draw.rect(screen, (0,150,255), (player_x, player_y, 48, 15))

            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    player_x = player_x - 15
            if event.type == KEYUP:
                if event.key == K_LEFT:
                    player_x = player_x
            
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    player_x = player_x + 15
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    player_x = player_x

            pygame.display.update()
        

main_game()