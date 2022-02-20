import pygame

# Initialize pygame for game machanics
pygame.init()
# Initialize pygame for game sounds
pygame.mixer.init()

s_width = 750
s_height = 800  # 1010
screen = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption("BREAKOUT")

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

# define game variables
cols = 6
rows = 6
clock = pygame.time.Clock()
fps = 60

points = 0
balls = 1
vel = 4

p_height = 48
p_width = 15

all_sprites_list = pygame.sprite.Group()

# Collision sounds
brick_sound = pygame.mixer.Sound("Sounds/sound_brick.wav")
paddle_sound = pygame.mixer.Sound("Sounds/sound_paddle.wav")
wall_sound = pygame.mixer.Sound("Sounds/sound_wall.wav")

# Creating the player


class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.color = color
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels
        if self.rect.x > s_width - wall_width - p_width - 33:
            self.rect.x = s_width - wall_width - p_width - 33

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        if self.rect.x < wall_width:
            self.rect.x = wall_width

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)


# Creating the ball
class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.vel = [vel, vel]

    def update(self):
        self.rect.x += self.vel[0]
        self.rect.y += self.vel[1]

    def bounce(self):
        self.vel[0] = self.vel[0]
        self.vel[1] = -self.vel[1]

    def draw(self):
        pygame.draw.circle(screen, colors["White"], (375, 300), 10)


class Brick(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()


# Creating object of player and ball

player = Paddle(colors["Blue"], p_height, p_width)
player.rect.x = s_width // 2
player.rect.y = 750
balls = 1
velocity = 4

ball = Ball(colors["White"], 10, 10)
ball.rect.x = s_width // 2 - 5
ball.rect.y = s_height // 2 - 5

all_bricks = pygame.sprite.Group()

brick_width = 55
brick_height = 16
x_gap = 7
y_gap = 5
wall_width = 16


# Function to create the wall of bricks


def bricks():
    for j in range(8):
        for i in range(14):
            if j < 2:
                if i == 0:
                    brick = Brick(colors["Red"], brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(colors["Red"], brick_width, brick_height)
                    brick.rect.x = (
                        wall_width
                        + brick_width
                        + x_gap
                        + (i - 1) * (brick_width + x_gap)
                    )
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
            if 1 < j < 4:
                if i == 0:
                    brick = Brick(colors["Orange"], brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(colors["Orange"], brick_width, brick_height)
                    brick.rect.x = (
                        wall_width
                        + brick_width
                        + x_gap
                        + (i - 1) * (brick_width + x_gap)
                    )
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
            if 3 < j < 6:
                if i == 0:
                    brick = Brick(colors["Green"], brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(colors["Green"], brick_width, brick_height)
                    brick.rect.x = (
                        wall_width
                        + brick_width
                        + x_gap
                        + (i - 1) * (brick_width + x_gap)
                    )
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
            if 5 < j < 8:
                if i == 0:
                    brick = Brick(colors["Yellow"], brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(colors["Yellow"], brick_width, brick_height)
                    brick.rect.x = (
                        wall_width
                        + brick_width
                        + x_gap
                        + (i - 1) * (brick_width + x_gap)
                    )
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)


brick_wall = bricks()

all_sprites_list.add(player)
all_sprites_list.add(ball)


def main_game(points, balls):

    step = 0

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.moveLeft(8)
        if keys[pygame.K_RIGHT]:
            player.moveRight(8)

        all_sprites_list.update()

        # Colision and velocity

        if ball.rect.y > s_height:
            ball.rect.x = s_width // 2 - 5
            ball.rect.y = s_height // 2 - 5
            ball.vel[1] = ball.vel[1]
            balls += 1

            if balls == 4:
                font = pygame.font.Font("freesansbold.ttf", 75)
                text = font.render("GAME OVER", 1, "White")
                text_rect = text.get_rect(center=(s_width / 2, 430))
                screen.blit(text, text_rect)
                pygame.display.update()
                pygame.time.wait(2000)
                run = False

        if pygame.sprite.collide_mask(ball, player):
            ball.rect.x += ball.vel[0]
            ball.rect.y -= ball.vel[1]
            ball.bounce()
            paddle_sound.play()

        if ball.rect.y < 40:
            ball.vel[1] = -ball.vel[1]
            wall_sound.play()

        if ball.rect.x >= s_width - wall_width - 10:
            ball.vel[0] = -ball.vel[0]
            wall_sound.play()

        if ball.rect.x <= wall_width:
            ball.vel[0] = -ball.vel[0]
            wall_sound.play()

        brick_collision_list = pygame.sprite.spritecollide(
            ball, all_bricks, False)

        for brick in brick_collision_list:
            ball.bounce()
            brick_sound.play()

            if len(brick_collision_list) > 0:
                step += 1
                for i in range(0, 448, 28):
                    if step == i:
                        ball.vel[0] += 1
                        ball.vel[1] += 1

            if 380.5 > brick.rect.y > 338.5:
                points += 1
                brick.kill()
            elif 338.5 > brick.rect.y > 294:
                points += 3
                brick.kill()
            elif 294 > brick.rect.y > 254.5:
                points += 5
                brick.kill()
            else:
                points += 7
                brick.kill()

            if len(all_bricks) == 0:
                font = pygame.font.Font("freesansbold.ttf", 70)
                text = font.render("SCREEN CLEARED", 1, colors["White"])
                text_rect = text.get_rect(center=(s_width / 2, s_height / 2))
                all_sprites_list.add(ball)
                screen.blit(text, text_rect)
                pygame.display.update()
                pygame.time.wait(2000)
                run = False

        screen.fill(colors["Black"])

        # Screen scenario

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
            [(wall_width / 2) - 1, 212.5 + (2 * brick_height + 2 * y_gap)],
            wall_width,
        )
        pygame.draw.line(
            screen,
            colors["Red"],
            [(s_width - wall_width / 2) - 1, 212.5],
            [(s_width - wall_width / 2) - 1, 212.5 + (
                2 * brick_height + 2 * y_gap)],
            wall_width,
        )

        pygame.draw.line(
            screen,
            colors["Orange"],
            [(wall_width / 2) - 1, 212.5 + (2 * brick_height + 2 * y_gap)],
            [(wall_width / 2) - 1, 212.5 + (4 * brick_height + 4 * y_gap)],
            wall_width,
        )
        pygame.draw.line(
            screen,
            colors["Orange"],
            [(s_width - wall_width / 2) - 1, 212.5 + (
                2 * brick_height + 2 * y_gap)],
            [(s_width - wall_width / 2) - 1, 212.5 + (
                4 * brick_height + 4 * y_gap)],
            wall_width,
        )

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
            colors["Green"],
            [(wall_width / 2) - 1, 212.5 + (4 * brick_height + 4 * y_gap)],
            [(wall_width / 2) - 1, 212.5 + (6 * brick_height + 6 * y_gap)],
            wall_width,
        )
        pygame.draw.line(
            screen,
            colors["Green"],
            [(s_width - wall_width / 2) - 1, 210 + (
                4 * brick_height + 4 * y_gap)],
            [(s_width - wall_width / 2) - 1, 210 + (
                6 * brick_height + 6 * y_gap)],
            wall_width,
        )

        pygame.draw.line(
            screen,
            colors["Yellow"],
            [(wall_width / 2) - 1, 212.5 + (6 * brick_height + 6 * y_gap)],
            [(wall_width / 2) - 1, 212.5 + (8 * brick_height + 8 * y_gap)],
            wall_width,
        )
        pygame.draw.line(
            screen,
            colors["Yellow"],
            [(s_width - wall_width / 2) - 1, 212.5 + (
                6 * brick_height + 6 * y_gap)],
            [(s_width - wall_width / 2) - 1, 212.5 + (
                8 * brick_height + 8 * y_gap)],
            wall_width,
        )

        font = pygame.font.Font("freesansbold.ttf", 70)
        text = font.render(str(f"{points:03}"), 1, "White")
        screen.blit(text, (80, 120))
        text = font.render(str(balls), 1, "White")
        screen.blit(text, (520, 41))
        text = font.render("000", 1, "White")
        screen.blit(text, (580, 120))
        text = font.render("1", 1, "White")
        screen.blit(text, (20, 40))

        all_sprites_list.draw(screen)

        pygame.display.update()

        clock.tick(fps)


main_game(points, balls)
