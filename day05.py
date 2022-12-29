lines = open('input/day05.txt').read().splitlines()

seats = set()

for line in lines:
    row, col = 0, 0
    for i in range(7): row += (line[i] == 'B') * 2 ** (6 - i)
    for i in range(3): col += (line[i + 7] == 'R') * 2 ** (2 - i)
    seats.add(row * 8 + col)

part1 = max(seats)
part2 = (set(range(min(seats), max(seats))) - seats).pop()

print(f'part 1: {part1}')
print(f'part 2: {part2}')
