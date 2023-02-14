import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Set window size
WIDTH = 400
HEIGHT = 300

# Create window
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Set window title
pygame.display.set_caption("Snake Game")

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize clock
clock = pygame.time.Clock()

# Set block size
BLOCK_SIZE = 10

# Initialize snake and food positions
snake_x = WIDTH / 2
snake_y = HEIGHT / 2
food_x = random.randint(0, WIDTH - BLOCK_SIZE)
food_y = random.randint(0, HEIGHT - BLOCK_SIZE)

# Initialize snake velocity
velocity_x = 0
velocity_y = 0

# Initialize snake body as a list
snake_body = []

# Set game over flag
game_over = False

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                velocity_x = 0
                velocity_y = -BLOCK_SIZE
            if event.key == pygame.K_DOWN:
                velocity_x = 0
                velocity_y = BLOCK_SIZE
            if event.key == pygame.K_LEFT:
                velocity_x = -BLOCK_SIZE
                velocity_y = 0
            if event.key == pygame.K_RIGHT:
                velocity_x = BLOCK_SIZE
                velocity_y = 0

    # Update snake position
    snake_x += velocity_x
    snake_y += velocity_y

    # Check for collision with food
    if snake_x == food_x and snake_y == food_y:
        food_x = random.randint(0, WIDTH - BLOCK_SIZE)
        food_y = random.randint(0, HEIGHT - BLOCK_SIZE)

        # Add block to snake body
        snake_body.append((snake_x, snake_y))
    else:
        # Remove last block from snake body
        snake_body.pop(0)

    # Check for collision with walls
    if snake_x >= WIDTH or snake_x < 0 or snake_y >= HEIGHT or snake_y < 0:
        game_over = True

    # Check for collision with snake body
    for block in snake_body:
        if block[0] == snake_x and block[1] == snake_y:
            game_over = True

    # Clear window
    window.fill(WHITE)

    # Draw food
    pygame.draw.rect(window, RED, (food_x, food_
