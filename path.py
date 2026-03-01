import pygame
import random
import math
import time
from queue import PriorityQueue

# ========== SETTINGS ==========
CELL_SIZE = 25
ROWS = 20
COLS = 20
WINDOW_WIDTH = COLS * CELL_SIZE
WINDOW_HEIGHT = ROWS * CELL_SIZE
FPS = 60

# ========== COLORS ==========
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)   # Start
PURPLE = (128, 0, 128)   # Goal
BLUE = (0, 0, 255)       # Visited
YELLOW = (255, 255, 0)   # Frontier
GREEN = (0, 255, 0)      # Final Path
GRAY = (200, 200, 200)



# ========== INITIAL GRID ==========
grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
start = (0, 0)
goal = (ROWS-1, COLS-1)
grid[start[0]][start[1]] = 2
grid[goal[0]][goal[1]] = 3

dynamic_mode = True
algorithm_choice = "A*"        # Options: "A*" or "GBFS"
heuristic_choice = "Manhattan" # Options: "Manhattan" or "Euclidean"
density = 0.3                  # 30% obstacles

nodes_expanded = 0
path_cost = 0
exec_time = 0

# ========== PYGAME INIT ==========
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT + 50))
pygame.display.set_caption("Dynamic Pathfinding Agent (Pygame)")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

# ========== GRID FUNCTIONS ==========
def draw_grid():
    screen.fill(WHITE)
    for i in range(ROWS):
        for j in range(COLS):
            x = j * CELL_SIZE
            y = i * CELL_SIZE
            color = WHITE
            if grid[i][j] == 0:
                color = WHITE
            elif grid[i][j] == 1:
                color = BLACK
            elif grid[i][j] == 2:
                color = ORANGE
            elif grid[i][j] == 3:
                color = PURPLE
            elif grid[i][j] == 4:
                color = BLUE
            elif grid[i][j] == 5:
                color = YELLOW
            elif grid[i][j] == 6:
                color = GREEN
            pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, GRAY, (x, y, CELL_SIZE, CELL_SIZE), 1)
    # Draw metrics
    metrics_text = font.render(f"Nodes Visited: {nodes_expanded} | Path Cost: {path_cost} | Time: {exec_time:.2f} ms", True, (0,0,0))
    screen.blit(metrics_text, (5, WINDOW_HEIGHT + 5))
    pygame.display.update()

def generate_random_grid():
    global grid
    for i in range(ROWS):
        for j in range(COLS):
            if (i, j) != start and (i, j) != goal:
                grid[i][j] = 1 if random.random() < density else 0
    draw_grid()

def toggle_obstacle(pos):
    x, y = pos
    row = y // CELL_SIZE
    col = x // CELL_SIZE
    if (row, col) != start and (row, col) != goal:
        grid[row][col] = 0 if grid[row][col] == 1 else 1
    draw_grid()

