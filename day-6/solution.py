import sys
import re
from collections import defaultdict, Counter, deque
import pyperclip as pc
def pr(s):
    print(s)
    pc.copy(s)
    
sys.setrecursionlimit(10**6)
infile = sys.argv[1] if len(sys.argv)>=2 else 'input.txt'
part1_result = 0
part2_result = 0
data = open(infile).read().strip()

grid = data.split('\n')
rows = len(grid)
cols = len(grid[0])
for row in range(rows):
    for col in range(cols):
        if grid[row][col] == '^':
            start_row, start_col = row, col

for outer_row in range(rows):
    for outer_col in range(cols):
        row, col = start_row, start_col
        direction = 0 # 0=up, 1=right, 2=down, 3=left
        seen_positions = set()
        seen_row_col = set()
        while True:
            if (row, col, direction) in seen_positions:
                part2_result += 1
                print(f"Loop detected at ({row}, {col}) with direction {direction}")
                break
            seen_positions.add((row, col, direction))
            seen_row_col.add((row, col))
            delta_row, delta_col = [(-1, 0), (0, 1), (1, 0), (0, -1)][direction]
            new_row = row + delta_row
            new_col = col + delta_col
            if not (0 <= new_row < rows and 0 <= new_col < cols):
                if grid[outer_row][outer_col] == '#':
                    part1_result = len(seen_row_col)
                    print(f"Boundary hit at ({outer_row}, {outer_col}), unique positions: {part1_result}")
                break
            if grid[new_row][new_col] == '#' or (new_row == outer_row and new_col == outer_col):
                direction = (direction + 1) % 4
                print(f"Obstacle at ({new_row}, {new_col}), changing direction to {direction}")
            else:
                row = new_row
                col = new_col
                print(f"Moving to ({row}, {col}) in direction {direction}")

pr(part1_result)
pr(part2_result)