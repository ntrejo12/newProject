import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((750, 750))
pygame.display.set_caption("Sudoku Grid")

# Define colors
PINK = (255, 182, 193)
BLACK = (0, 0, 0)

def draw():
    # gives us a pink background
    screen.fill(PINK)
    pygame.draw.rect(screen, BLACK, pygame.Rect(15, 15, 720, 720), 10)
    i = 1
    while (i * 80) < 720:
        pygame.draw.line(screen, BLACK, pygame.Vector2(((i * 80) + 15), 15), pygame.Vector2(((i * 80) + 15), 15), 5)



def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Fill the screen with white color
        # screen.fill(PINK)

        # calls draw grid function
        draw()

        # Update the display
        pygame.display.flip()

while 1:
    game_loop()

# Box dimensions and position
# box_width = 100
# box_height = 100
# box_x = (800 - box_width) // 2
# box_y = (600 - box_height) // 2

# grid width + height


# Main game loop
