from numpy import array, zeros

WORMHOLE_REPRESENTATION: int = -10001

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
    print(grid)
    for i in range(grid_size[0]):
        line: list = lines[i + 2].split(" ")

        for j, cell in enumerate(line):
            if cell == "*":
                grid[i, j] = WORMHOLE_REPRESENTATION
            else:
                grid[i, j] = int(cell)
