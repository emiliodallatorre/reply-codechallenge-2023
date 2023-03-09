from random import choice

from agentpy import Agent

POSSIBLE_DIRECTIONS: list = ["U", "D", "L", "R"]


class Snake(Agent):
    size: int
    occupied_cells: list[tuple]

    def __init__(self, model, *args, **kwargs):
        super().__init__(model, args, kwargs)
        self.space = None
        self.neighbors = None
        self.position = None

    def setup_pos(self, space, size: tuple):
        self.space = space
        self.neighbors = self.space.neighbors

    def get_current_position(self):
        return self.space.positions[self]

    def move(self):
        direction: str = self.decide_direction()

        if direction is not None:
            self.space.move_agent(self, direction)
            self.occupied_cells.pop(0)
            self.occupied_cells.append(self.get_current_position())

    def decide_direction(self) -> str:
        direction: str = choice(POSSIBLE_DIRECTIONS)
        first_attempt: str = direction

        while (self.get_next_position(direction) in self.occupied_cells) or (
                self.get_next_position(direction) in self.space.neighbors.occupied_cells):
            direction: str = POSSIBLE_DIRECTIONS[(POSSIBLE_DIRECTIONS.index(direction) + 1) % len(POSSIBLE_DIRECTIONS)]

        if direction == first_attempt:
            return None

        return direction

    def get_next_position(self, direction: str) -> tuple:
        current_position: tuple = self.get_current_position()
        next_position: tuple = current_position
        if direction == "U":
            next_position = (current_position[0] - 1, current_position[1])
        elif direction == "D":
            next_position = (current_position[0] + 1, current_position[1])
        elif direction == "L":
            next_position = (current_position[0], current_position[1] - 1)
        elif direction == "R":
            next_position = (current_position[0], current_position[1] + 1)

        if next_position[0] < 0:
            next_position = (self.space.shape[0] + (next_position[0] % self.space.shape[0]), next_position[1])
        elif next_position[0] >= self.space.shape[0]:
            next_position = (next_position[0] % self.space.shape[0], next_position[1])

        if next_position[1] < 0:
            next_position = (next_position[0], self.space.shape[1] + (next_position[1] % self.space.shape[1]))
        elif next_position[1] >= self.space.shape[1]:
            next_position = (next_position[0], next_position[1] % self.space.shape[1])

        return next_position
