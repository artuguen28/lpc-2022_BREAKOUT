import pygame
from pygame.locals import *
from sys import exit

# Initialize pygame for game machanics
pygame.init()
# Initialize pygame for game sounds
pygame.mixer.init()

s_width = 750
s_height = 900  # 1010
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


class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.velocity = [velocity, velocity]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = self.velocity[0]
        self.velocity[1] = -self.velocity[1]


ball = Ball(colors["White"], 10, 10)
ball.rect.x = s_width // 2 - 5
ball.rect.y = s_height // 2 - 5

all_sprites_list.add(ball)


def main_game():
    while True:

        global player_x
        global player_y

        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        pygame.draw.rect(
            screen, colors["Blue"], (player_x, player_y, p_height, p_width))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 10:
            player_x = player_x - 5
        if keys[pygame.K_RIGHT] and player_x < 686:
            player_x = player_x + 5

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
