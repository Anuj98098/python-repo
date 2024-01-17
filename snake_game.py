
import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
FPS = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Snake class
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN

    def get_head_position(self):
        return self.positions[0]

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * GRID_SIZE)) % SCREEN_WIDTH), (cur[1] + (y * GRID_SIZE)) % SCREEN_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def draw(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, self.color, (p[0], p[1], GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, BLACK, (p[0], p[1], GRID_SIZE, GRID_SIZE), 1)

    def handle_keys(self, keys):
        if keys[pygame.K_UP]:
            self.direction = UP
        elif keys[pygame.K_DOWN]:
            self.direction = DOWN
        elif keys[pygame.K_LEFT]:
            self.direction = LEFT
        elif keys[pygame.K_RIGHT]:
            self.direction = RIGHT

# Food class
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, BLACK, (self.position[0], self.position[1], GRID_SIZE, GRID_SIZE), 1)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Game setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
snake = Snake()
food = Food()

# Fonts
font = pygame.font.SysFont(None, 36)

# Main game loop
running = True
while running:
    screen.fill(WHITE)
    snake.handle_keys(pygame.key.get_pressed())
    snake.move()

    # Collision with food
    if snake.get_head_position() == food.position:
        snake.length += 1
        food.randomize_position()

    snake.draw(screen)
    food.draw(screen)

    # Collision with wall
    head_x, head_y = snake.get_head_position()
    if head_x < 0 or head_x >= SCREEN_WIDTH or head_y < 0 or head_y >= SCREEN_HEIGHT:
        snake.reset()

    # Collision with itself
    for pos in snake.positions[1:]:
        if pos == snake.get_head_position():
            snake.reset()

    # Display score
    text = font.render(f"Score: {snake.length - 1}", True, BLACK)
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
