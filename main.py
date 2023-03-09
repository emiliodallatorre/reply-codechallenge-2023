from itertools import combinations_with_replacement

from numpy import array, zeros

WORMHOLE_REPRESENTATION: int = -10001
DIRECTIONS: list = ["U", "D", "L", "R"]

grid_size: tuple
snake_count: int
snake_sizes: array
grid: array

with open("data/01-example.txt", "r") as f:
    lines: list = f.readlines()
    grid_size = tuple(map(int, lines[0].split()[0:2]))
    grid_size = (grid_size[1], grid_size[0])

    snake_count = int(lines[0].split()[2])
    snake_sizes = array(list(map(int, lines[1].split())))

    grid = zeros(grid_size, dtype=int)
    for i in range(grid_size[0]):
        line: list = lines[i + 2].split(" ")

        for j, cell in enumerate(line):
            if cell == "*":
                grid[i, j] = WORMHOLE_REPRESENTATION
            else:
                grid[i, j] = int(cell)


def move(start: tuple, direction: str):
    new_cell: tuple = start
    if direction == "U":
        new_cell = (start[0] - 1, start[1])
    elif direction == "D":
        new_cell = (start[0] + 1, start[1])
    elif direction == "L":
        new_cell = (start[0], start[1] - 1)
    elif direction == "R":
        new_cell = (start[0], start[1] + 1)

    if new_cell[0] < 0:
        new_cell = (grid_size[0] + (new_cell[0] % grid_size[0]), new_cell[1])
    elif new_cell[0] >= grid_size[0]:
        new_cell = (new_cell[0] % grid_size[0], new_cell[1])

    if new_cell[1] < 0:
        new_cell = (new_cell[0], grid_size[1] + (new_cell[1] % grid_size[1]))
    elif new_cell[1] >= grid_size[1]:
        new_cell = (new_cell[0], new_cell[1] % grid_size[1])

    return new_cell


def get_best_path_from_cell(cell: tuple, length: int) -> tuple:
    best_path: list = ["U" * length]
    best_score: int = WORMHOLE_REPRESENTATION

    current_cell: tuple = cell
    current_score: int = 0

    possible_paths: list = list(combinations_with_replacement(DIRECTIONS, length))

    for path in possible_paths:
        for direction in path:
            current_cell = move(current_cell, direction)
            current_score += grid[current_cell]

        if current_score > best_score:
            best_path = path
            best_score = current_score

        current_cell = cell
        current_score = 0

    occupied_cells: list = []
    for direction in best_path:
        current_cell = move(current_cell, direction)
        occupied_cells.append(current_cell)

    return best_path, best_score, occupied_cells


for snake in range(snake_count):