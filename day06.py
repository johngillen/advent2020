lines = open('input/day06.txt').read().splitlines()

groups = [[]]

for line in lines:
    if line: groups[-1] += [set(line)]
    else: groups += [[]]

part1 = sum(len(set.union(*g)) for g in groups)
part2 = sum(len(set.intersection(*g)) for g in groups)

print(f'part 1: {part1}')
print(f'part 2: {part2}')
