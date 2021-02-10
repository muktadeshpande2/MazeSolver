import pygame
import time
import random

WIDTH = 600
HEIGHT = 600
FPS = 30

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Solver - Mukta Girish Deshpande")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
GREEN = (0, 255, 0,)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)


x, y = 20, 20
w = 20
x_st, y_st = x, y
x_end, y_end = 20*20, 20*20
grid = []
visited = []
stack = []
solution = {}


def build_maze(x, y, w):
    for i in range(20):
        x = 20
        y = y + 20
        for j in range(20):
            pygame.draw.line(screen, WHITE, [x, y], [x + w, y])
            pygame.draw.line(screen, WHITE, [x + w, y], [x + w, y + w])
            pygame.draw.line(screen, WHITE, [x + w, y + w], [x, y + w])
            pygame.draw.line(screen, WHITE, [x, y + w], [x, y])
            grid.append((x, y))
            x = x + 20


def push_up(x, y):
    pygame.draw.rect(screen, BLUE, (x + 1, y - w + 1, 19, 39), 0)
    pygame.display.update()


def push_down(x, y):
    pygame.draw.rect(screen, BLUE, (x + 1, y + 1, 19, 39), 0)
    pygame.display.update()


def push_left(x, y):
    pygame.draw.rect(screen, BLUE, (x - w + 1, y + 1, 39, 19), 0)
    pygame.display.update()


def push_right(x, y):
    pygame.draw.rect(screen, BLUE, (x + 1, y + 1, 39, 19), 0)
    pygame.display.update()


def single_cell(x, y):
    pygame.draw.rect(screen, GREEN, (x + 1, y + 1, 18, 18), 0)
    pygame.display.update()


def backtracking_cell(x, y):
    pygame.draw.rect(screen, BLUE, (x + 1, y + 1, 18, 18), 0)
    pygame.display.update()


def solution_cell(x, y):
    pygame.draw.rect(screen, YELLOW, (x+8, y+8, 5, 5), 0)
    pygame.display.update()


def solve_maze(x, y):
    single_cell(x, y)
    stack.append((x, y))
    visited.append((x, y))
    while len(stack) > 0:
        # time.sleep(.1)
        cell = []
        if (x + w, y) not in visited and (x + w, y) in grid:
            cell.append("right")

        if (x - w, y) not in visited and (x - w, y) in grid:
            cell.append("left")

        if (x, y + w) not in visited and (x, y + w) in grid:
            cell.append("down")

        if (x, y - w) not in visited and (x, y - w) in grid:
            cell.append("up")

        if len(cell) > 0:
            cell_chosen = (random.choice(cell))

            if cell_chosen == "right":
                push_right(x, y)
                solution[(x + w, y)] = x, y
                x = x + w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "left":
                push_left(x, y)
                solution[(x - w, y)] = x, y
                x = x - w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "down":
                push_down(x, y)
                solution[(x, y + w)] = x, y
                y = y + w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "up":
                push_up(x, y)
                solution[(x, y - w)] = x, y
                y = y - w
                visited.append((x, y))
                stack.append((x, y))
        else:
            x, y = stack.pop()
            single_cell(x, y)
            # time.sleep(.05)
            backtracking_cell(x, y)


def plot_route_back(x, y):
    solution_cell(x, y)
    while (x, y) != (x_st, y_st):
        x, y = solution[x, y]
        solution_cell(x, y)
        time.sleep(.1)


build_maze(40, 0, 20)
solve_maze(x_st, y_st)
plot_route_back(x_end, y_end)

alive = True
while alive:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            alive = False
            break
