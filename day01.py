lines = open('input/day01.txt').read().splitlines()

part1 = None
part2 = None

expenses = [int(line) for line in lines]
for i, entry in enumerate(expenses):
    if not part1 and 2020 - entry in expenses[i:]:
        part1 = entry * (2020 - entry)
    if not part2:
        for j, entry2 in enumerate(expenses[i:]):
            if 2020 - entry - entry2 in expenses[i+j:]:
                part2 = entry * entry2 * (2020 - entry - entry2)

print(f'part 1: {part1}')
print(f'part 2: {part2}')
