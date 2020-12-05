myinput = []
with open('input3.txt') as f:
    myinput = f.read().splitlines()


def slopeFinder(right, down):
    position = 0
    trees = 0
    for line_index in range(0, len(myinput), down):
        current_line = myinput[line_index]
        current_index = position
        if position >= len(current_line):
            current_index = position % len(current_line)
        if current_line[current_index] == '#':
            trees += 1
        position += right
    return trees

# Day 1
print(slopeFinder(3,1)) # 151

# Day 2
print(slopeFinder(1, 1) * slopeFinder(3, 1) * slopeFinder(5, 1) * slopeFinder(7, 1) * slopeFinder(1, 2)) # 7540141059