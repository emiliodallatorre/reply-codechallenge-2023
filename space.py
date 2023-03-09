from agentpy import Model, AgentList, Grid, AttrIter
from numpy import array, shape

from snake import Snake


class Space(Model):
    grid: array
    snake_count: int
    snake_sizes: array
    space: Grid
    snakes: AgentList

    def __init__(self, grid: array, snake_count: int, snake_sizes: array):
        super().__init__()

        self.grid = grid
        self.snake_count = snake_count
        self.snake_sizes = snake_sizes

    def setup(self):
        self.space = Grid(self, shape(self.grid))
        self.snakes = AgentList(self, self.snake_count, Snake)
        self.snakes.size = AttrIter(list(self.snake_sizes))

        self.space.add_agents(self.snakes, random=True)

    def step(self):
        # Controllare validità dello stato (?)
        # Muovere i serpenti
        # Contare i punti
        # Se maggiori del max, salvare lo stato come migliore

        self.snakes.move()

