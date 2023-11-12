import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Goku Fighting Game")

# Colors
WHITE = (255, 255, 255)

# Goku character
goku_width, goku_height = 50, 50
goku_x, goku_y = WIDTH // 2 - goku_width // 2, HEIGHT - goku_height - 10
goku_speed = 5

# Main game loop
clock = pygame.time.Clock()

while True:
    clock.tick(30)  # 30 frames per second

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and goku_x > 0:
        goku_x -= goku_speed
    if keys[pygame.K_RIGHT] and goku_x < WIDTH - goku_width:
        goku_x += goku_speed

    # Draw everything
    win.fill(WHITE)
    pygame.draw.rect(win, (0, 128, 255), (goku_x, goku_y, goku_width, goku_height))

    pygame.display.flip()

pygame.quit()
pip install pygame
