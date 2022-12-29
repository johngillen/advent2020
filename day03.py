lines = open('input/day03.txt').read().splitlines()

import numpy

grid = [[(1 if c == '#' else 0) for c in line] for line in lines]

def slide(dx, dy):
    x, y = 0, 0
    trees = 0
    while y < len(grid):
        trees += grid[y][x]
        x = (x + dx) % len(grid[0])
        y += dy
    return trees

part1 = slide(3, 1)
part2 = numpy.product([slide(dx, dy) for dx, dy in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]])

print(f'part 1: {part1}')
print(f'part 2: {part2}')
