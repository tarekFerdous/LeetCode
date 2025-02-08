import re
from collections import deque
from typing import List


class Solution_200:
    '''
    The complexity is O(m*n). The loop is controlled in a way that each position in the grid is traversed only once.
    Hence, O(m*n).
    '''
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if 0 <= r <= len(grid) - 1 and 0 <= c <= len(grid[0]) - 1 and grid[r][c] == '1' and (
                    r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))

        count = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    count += 1

        return count

    '''
    This solution has the same complexity as before. However, I have tried to optimize it even more by not using any
    visited list. We can change the value to something else other than '0' and '1'. By doing that we can easily track
    the positions that are already visited.
    '''
    def numIsland_space(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = 'v'

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if 0 <= r <= len(grid) - 1 and 0 <= c <= len(grid[0]) - 1 and grid[r][c] == '1':
                        q.append((r, c))
                        grid[r][c] = 'v'

        count = 0
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    bfs(r, c)
                    count += 1

        return count

        return count


solution = Solution_200()

matrix = [[elem[1:len(elem) - 1] for elem in st.split(",")] for st in re.findall('\[(.*?)\]', input()[1:])]

print(solution.numIslands(matrix))
print(solution.numIsland_space(matrix))
