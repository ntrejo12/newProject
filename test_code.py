import pygame
import sys

# Initialize Pygame
# will go in main function?
pygame.init()

# Set up the display
width = 750
height = 750
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sudoku Grid")

# Define colors
PINK = (255, 182, 193)
BLACK = (0, 0, 0)

def __init__(self, width, height, screen, difficulty):
    self.width = width
    self.height = height
    self.screen = screen
    self.difficulty = difficulty

def draw():
    # gives us a pink background
    screen.fill(PINK)
    # draws outside rectangle
    pygame.draw.rect(screen, BLACK, pygame.Rect(15, 15, 720, 720), 10)
    i = 1
    while (i * 80) < 720:
        if i % 3 != 0:
            line_width = 5
        else:
            line_width = 10

        # draws vertical lines
        pygame.draw.line(screen, BLACK, pygame.Vector2(((i * 80) + 15), 15), pygame.Vector2(((i * 80) + 15), 735), line_width)
        # draws horizontal lines
        pygame.draw.line(screen, BLACK, pygame.Vector2(15, ((i * 80) + 15)), pygame.Vector2(735, ((i * 80) + 15)), line_width)
        i += 1

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
