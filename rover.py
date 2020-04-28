from enum import Enum, unique


@unique
class Direction(Enum):
    N = 'north'
    S = 'south'
    E = 'east'
    W = 'west'


class RoverSim:

    def __init__(self, x=0, y=0, d=Direction.N, x_max=10, y_max=10):
        if x < 0 or y < 0 or x_max < 0 or y_max < 0:
            raise ValueError('X and Y values must be positive!')

        self.x = x
        self.y = y
        self.d = d
        self.x_max = x_max
        self.y_max = y_max

    def _control(self, char: str):
        """
        Execute the correct action based on the given control character
        :param char: A control character. One of l, r, m
        :return: None
        """
        assert char in ('l', 'r', 'm')
        if char == 'l':
            self._turn_left()
        elif char == 'r':
            self._turn_right()
        elif char == 'm':
            self._move()

    def _turn_left(self):
        if self.d == Direction.N:
            self.d = Direction.W
        elif self.d == Direction.E:
            self.d = Direction.N
        elif self.d == Direction.S:
            self.d = Direction.E
        elif self.d == Direction.W:
            self.d = Direction.S

    def _turn_right(self):
        if self.d == Direction.N:
            self.d = Direction.E
        elif self.d == Direction.E:
            self.d = Direction.S
        elif self.d == Direction.S:
            self.d = Direction.W
        elif self.d == Direction.W:
            self.d = Direction.N

    def _move(self):
        # Magical walls prevent the rover from going beyond the limits
        if self.d == Direction.N and self.y < self.y_max:
            self.y += 1
        elif self.d == Direction.E and self.x < self.x_max:
            self.x += 1
        elif self.d == Direction.S and self.y > 0:
            self.y -= 1
        elif self.d == Direction.W and self.x > 0:
            self.x -= 1

        # Raise an exception if rover leaves the defined positive grid
        assert 0 <= self.x <= self.x_max
        assert 0 <= self.y <= self.y_max

    def command(self, instruction: str):
        """
        Execute a command string using the rovers current location subject
        to restriction of grid maximums.
        :param instruction:
        :return:
        """
        assert isinstance(instruction, str)
        for command in instruction:
            self._control(command.lower())

    def __str__(self):
        # We could optionally have the direction print only the compass character if that was required
        return f"{self.x} {self.y} {self.d}"


def _convert_direction(d: str) -> Direction:
    if d == 'N':
        return Direction.N
    elif d == 'S':
        return Direction.S
    elif d == 'W':
        return Direction.W
    elif d == 'E':
        return Direction.E
    else:
        raise Exception("Invalid Direction")


def parse_input(line1, line2, line3):
    x_max, y_max = line1.strip().split(' ')
    x, y, d = line2.strip().split(' ')
    instruction = line3.strip()

    # Convert input strings
    x = int(x)
    y = int(y)
    d = _convert_direction(d)
    x_max = int(x_max)
    y_max = int(y_max)
    return x, y, d, x_max, y_max, instruction


# Run the sim and print the final position
def run_rover_sim(x: int, y: int, d: Direction, x_max: int, y_max: int, instruction: str):
    sim = RoverSim(x, y, d, x_max, y_max)
    sim.command(instruction)
    print(sim)


if __name__ == "__main__":
    input_ = """
    5 5
    1 2 N
    LMLMLMLMM
    3 3 E
    MMRMMRMRRM
    """

    # Clean up input text
    lines = [line.strip() for line in input_.split('\n') if line.strip()]

    # Parse the first three lines and run the sim
    x, y, d, x_max, y_max, instruction = parse_input(*lines[0:3])
    run_rover_sim(x, y, d, x_max, y_max, instruction)

    # Parse the next two and run it again (reusing grid max)
    x, y, d, x_max, y_max, instruction = parse_input(lines[0], *lines[3:])
    run_rover_sim(x, y, d, x_max, y_max, instruction)
