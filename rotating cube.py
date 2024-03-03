import pygame
import math
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Screen size and initialization
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rotating Cube")

# Cube data
vertices = [(-100, -100, -100), (100, -100, -100),
            (100, 100, -100), (-100, 100, -100),
            (-100, -100, 100), (100, -100, 100),
            (100, 100, 100), (-100, 100, 100)]

edges = [(0, 1), (1, 2), (2, 3), (3, 0),
         (4, 5), (5, 6), (6, 7), (7, 4),
         (0, 4), (1, 5), (2, 6), (3, 7)]

# Rotation variables
angle_x = 0
angle_y = 0
angle_z = 0
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    screen.fill((0, 0, 0))
    
    # Handling rotation
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_LEFT:
                angle_y += 0.1
            elif event.key == K_RIGHT:
                angle_y -= 0.1
            elif event.key == K_UP:
                angle_x += 0.1
            elif event.key == K_DOWN:
                angle_x -= 0.1
    
    # Drawing the cube
    for edge in edges:
        points = []
        for vertex in edge:
            x, y, z = vertices[vertex]
            # Rotation around the three axes
            x = x * math.cos(angle_y) - z * math.sin(angle_y)
            z = x * math.sin(angle_y) + z * math.cos(angle_y)
            y = y * math.cos(angle_x) - z * math.sin(angle_x)
            z = y * math.sin(angle_x) + z * math.cos(angle_x)
            y = y * math.cos(angle_z) - x * math.sin(angle_z)
            x = y * math.sin(angle_z) + x * math.cos(angle_z)
            # Translation to the center
            x += WIDTH / 2
            y += HEIGHT / 2
            points += [(x, y)]
        pygame.draw.line(screen, (255, 255, 255), points[0], points[1], 2)
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
