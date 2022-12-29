lines = open('input/day04.txt').read().splitlines()

import re

part1 = 0
part2 = 0

passports = [{}]

for line in lines:
    if line:
        line = line.split()
        for k, v in [x.split(':') for x in line]:
            passports[-1][k] = v
    else:
        passports += [{}]

for p in passports:
    for k in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
        if k not in p: break
    else:
        part1 += 1

        if not (1920 <= int(p['byr']) <= 2002): continue
        if not (2010 <= int(p['iyr']) <= 2020): continue
        if not (2020 <= int(p['eyr']) <= 2030): continue
        
        if p['hgt'][-2:] == 'cm':
            if not (150 <= int(p['hgt'][:-2]) <= 193): continue
        elif p['hgt'][-2:] == 'in':
            if not (59 <= int(p['hgt'][:-2]) <= 76): continue
        else: continue

        if not re.match(r'^#[0-9a-f]{6}$', p['hcl']): continue
        if not re.match(r'^amb|blu|brn|gry|grn|hzl|oth$', p['ecl']): continue
        if not re.match(r'^\d{9}$', p['pid']): continue

        part2 += 1

print(f'part 1: {part1}')
print(f'part 2: {part2}')
