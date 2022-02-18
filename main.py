import pygame
from pygame.locals import *
from sys import exit

# Initialize pygame for game machanics
pygame.init()
# Initialize pygame for game sounds
pygame.mixer.init()

s_width = 750
s_height = 800  # 1010
screen = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption("BREAKOUT")

player_x = (s_height // 2) - 100
player_y = 840
balls = 1
velocity = 4

# Colors dictionary
colors = {
    "Black": (0, 0, 0),
    "White": (255, 255, 255),
    "Grey": (212, 210, 212),
    "Orange": (183, 119, 0),
    "Green": (0, 127, 33),
    "Blue": (0, 97, 148),
    "Red": (162, 8, 0),
    "Yellow": (197, 199, 37),
}

all_sprites_list = pygame.sprite.Group()

brick_width = 55
brick_height = 16
x_gap = 7
y_gap = 5
wall_width = 16
p_height = 48
p_width = 15

#paddle colours
color = (0, 100, 255)

#define game variables
cols = 6
rows = 6
clock = pygame.time.Clock()
fps = 60


#creating the player
class player():
    def __init__(self):
        self.height = 13
        self.width = 52
        self.x = int((s_width / 2) - (self.width / 2))
        self.y = 760
        self.speed = 10
        self.rect = Rect(self.x, self.y, self.width, self.height)
        self.direction = 0


    def move(self):
        #reset movement direction
        self.direction = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
            self.direction = -1
        if key[pygame.K_RIGHT] and self.rect.right < s_width:
            self.rect.x += self.speed
            self.direction = 1

    def draw(self):
        pygame.draw.rect(screen, color, self.rect)

player_paddle = player()

#Creating the ball
class game_ball():
    def __init__(self, x, y):
        self.ball_rad = 10
        self.x = x - self.ball_rad
        self.y = y
        self.rect = Rect(self.x, self.y, self.ball_rad * 2, self.ball_rad * 2)
        self.speed_x = 4
        self.speed_y = -4
        self.game_over = 0


    def move(self):

        #check for collision with walls
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.speed_x *= -1

        #check for collision with top and bottom of the screen
        if self.rect.top < 0:
            self.speed_y *= -1
        if self.rect.bottom > screen_height:
            self.game_over = -1


        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        return self.game_over


    def draw(self):
        pygame.draw.circle(screen, (255,255,255),(375,300), 10)

ball = game_ball(player_paddle.x + (player_paddle.width // 2), player_paddle.y - player_paddle.height)

def main_game():
    while True:
        clock.tick(fps)
    
        screen.fill((0,0,0))

        #draw player
        player_paddle.draw()
        player_paddle.move()

        #draw ball
        ball.draw()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
                
        pygame.draw.line(screen, colors["Grey"], [0, 19], [s_width, 19], 40)
        pygame.draw.line(
            screen,
            colors["Grey"],
            [(wall_width / 2) - 1, 0],
            [(wall_width / 2) - 1, s_height],
            wall_width,
        )
        pygame.draw.line(
            screen,
            colors["Grey"],
            [(s_width - wall_width / 2) - 1, 0],
            [(s_width - wall_width / 2) - 1, s_height],
            wall_width,
        )

        pygame.draw.line(
            screen,
            colors["Blue"],
            [(wall_width / 2) - 1, s_height - 65 + p_height / 2 - 54 / 2],
            [(wall_width / 2) - 1, s_height - 65 + p_height / 2 - 54 / 2 + 54],
            wall_width,
        )
        pygame.draw.line(
            screen,
            colors["Blue"],
            [
                (s_width - wall_width / 2) - 1,
                s_height - 65 + p_height / 2 - 54 / 2,
            ],
            [
                (s_width - wall_width / 2) - 1,
                s_height - 65 + p_height / 2 - 54 / 2 + 54,
            ],
            wall_width,
        )

        pygame.draw.line(
            screen,
            colors["Red"],
            [(wall_width / 2) - 1, 212.5],
            [(wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap],
            wall_width,
        )
        pygame.draw.line(
            screen,
            colors["Red"],
            [(s_width - wall_width / 2) - 1, 212.5],
            [(s_width - wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap],
            wall_width,
        )

        pygame.draw.line(
            screen,
            colors["Orange"],
            [(wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap],
            [(wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap],
            wall_width,
        )
        pygame.draw.line(
            screen,
            colors["Orange"],
            [(s_width - wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap],
            [(s_width - wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap],
            wall_width,
        )

        pygame.draw.line(
            screen,
            colors["Green"],
            [(wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap],
            [(wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap],
            wall_width,
        )
        pygame.draw.line(
            screen,
            colors["Green"],
            [(s_width - wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap],
            [(s_width - wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap],
            wall_width,
        )

        pygame.draw.line(
            screen,
            colors["Yellow"],
            [(wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap],
            [(wall_width / 2) - 1, 212.5 + 8 * brick_height + 8 * y_gap],
            wall_width,
        )
        pygame.draw.line(
            screen,
            colors["Yellow"],
            [(s_width - wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap],
            [(s_width - wall_width / 2) - 1, 212.5 + 8 * brick_height + 8 * y_gap],
            wall_width,
        )
        pygame.display.update()


main_game()
