lines = open('input/day02.txt').read().splitlines()

import re
ints = lambda line: [int(x) for x in re.findall(r'\d+', line)]

part1 = 0
part2 = 0

for line in lines:
    lo, hi = ints(line)
    hash = line.split(' ')[1][0]
    password = line.split(': ')[-1]
    if lo <= password.count(hash) <= hi: part1 += 1
    if (password[lo - 1] == hash) ^ (password[hi - 1] == hash): part2 += 1

print(f'part 1: {part1}')
print(f'part 2: {part2}')
