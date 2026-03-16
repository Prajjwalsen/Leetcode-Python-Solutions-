class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:

        m = len(grid)
        n = len(grid[0])

        sums = set()

        for i in range(m):
            for j in range(n):

                sums.add(grid[i][j])   # size 0 rhombus

                size = 1
                while True:

                    if i-size < 0 or i+size >= m or j-size < 0 or j+size >= n:
                        break

                    total = 0

                    # top -> right
                    r, c = i-size, j
                    for k in range(size):
                        total += grid[r+k][c+k]

                    # right -> bottom
                    r, c = i, j+size
                    for k in range(size):
                        total += grid[r+k][c-k]

                    # bottom -> left
                    r, c = i+size, j
                    for k in range(size):
                        total += grid[r-k][c-k]

                    # left -> top
                    r, c = i, j-size
                    for k in range(size):
                        total += grid[r-k][c+k]

                    sums.add(total)
                    size += 1

        return sorted(sums, reverse=True)[:3]