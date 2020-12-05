myinput = []
with open('input4.txt') as f:
    myinput = f.read().split('\n\n')

valid = 0
for i in myinput:
    if (
        'hcl' in i and 
        'byr' in i and
        'iyr' in i and
        'eyr' in i and
        'hgt' in i and
        'hcl' in i and
        'ecl' in i and
        'pid' in i
    ):
        valid += 1
print(valid)

keys = ['hcl',
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid']

def getValue(line, key):
    line = line.split()
    for pair in line:
        if key in pair:
            return pair[4 : len(pair)]

def determineValidity(key: str, value: str) -> bool:
    if key == 'byr':
        return int(value) >= 1920 and int(value) <= 2002
    if key == 'iyr':
        return int(value) >= 2010 and int(value) <= 2020
    if key == 'eyr':
        return int(value) >= 2020 and int(value) <= 2030
    if key == 'hgt':
        if 'cm' in value:
            return int(value[0 : len(value)-2]) >= 150 and int(value[0 : len(value)-2]) <= 193
        elif 'in' in value:
            return int(value[0 : len(value)-2]) >= 59 and int(value[0 : len(value)-2]) <= 76
        else:
            return False
    if key == 'hcl':
        if value[0] != '#':
            return False
        for char in range(1, len(value)):
            if value[char].isalpha():
                if value[char] > 'f' or value[char] < 'a':
                    return False
            else:
                if value[char] < '0' or value[char] > '9':
                    return False
        return True
    if key == 'ecl':
        return value in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    if key == 'pid':
        return value.isnumeric() and len(value) == 9

total = 0
invalid = 0
for line in myinput:
    total += 1
    for key in keys:
        if key not in line:
            print(key, 'NOT FOUND')
            invalid += 1
            break
        elif not determineValidity(key, getValue(line, key)):
            print(key, 'INVALID')
            invalid += 1
            break

print(total)
print(total-invalid)