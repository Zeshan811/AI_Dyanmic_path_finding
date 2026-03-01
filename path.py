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


# ========== HEURISTICS ==========
def heuristic(a, b):
    if heuristic_choice == "Manhattan":
        return abs(a[0]-b[0]) + abs(a[1]-b[1])
    else:
        return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

# ========== PATHFINDING ==========
def get_neighbors(node):
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    result = []
    for d in dirs:
        r = node[0] + d[0]
        c = node[1] + d[1]
        if 0 <= r < ROWS and 0 <= c < COLS:
            if grid[r][c] != 1:
                result.append((r,c))
    return result

def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path

def search(start_node):
    global nodes_expanded, exec_time
    nodes_expanded = 0
    open_set = PriorityQueue()
    open_set.put((0, start_node))
    came_from = {}
    g_score = {start_node: 0}
    start_time = time.time()

    while not open_set.empty():
        current = open_set.get()[1]
        nodes_expanded += 1

        if current == goal:
            exec_time = (time.time() - start_time) * 1000
            return reconstruct_path(came_from, current)

        for neighbor in get_neighbors(current):
            tentative_g = g_score[current] + 1
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g

                if algorithm_choice == "A*":
                    f = tentative_g + heuristic(neighbor, goal)
                else:
                    f = heuristic(neighbor, goal)

                open_set.put((f, neighbor))
                if grid[neighbor[0]][neighbor[1]] == 0:
                    grid[neighbor[0]][neighbor[1]] = 5

        if current != start_node:
            grid[current[0]][current[1]] = 4

        draw_grid()
        pygame.time.delay(10)
    return None

