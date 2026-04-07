class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.x = 0
        self.y = 0
        self.dir = 0  # 0=East, 1=North, 2=West, 3=South

        # Directions: East → North → West → South
        self.dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        self.perimeter = 2 * (self.w + self.h) - 4

    def step(self, num: int) -> None:
        if self.perimeter == 0:
            return

        num %= self.perimeter

        # Important edge case
        if num == 0:
            num = self.perimeter

        for _ in range(num):
            nx = self.x + self.dirs[self.dir][0]
            ny = self.y + self.dirs[self.dir][1]

            # Out of bounds → turn left
            if not (0 <= nx < self.w and 0 <= ny < self.h):
                self.dir = (self.dir + 1) % 4
                nx = self.x + self.dirs[self.dir][0]
                ny = self.y + self.dirs[self.dir][1]

            self.x = nx
            self.y = ny

    def getPos(self) -> list:
        return [self.x, self.y]

    def getDir(self) -> str:
        return ["East", "North", "West", "South"][self.dir]