myinput = []
with open('input2.txt') as f:
    myinput = f.read().splitlines()

#Part 1
valid_pass_count = 0

for line in myinput:
    split_line = line.split()
    split_range = split_line[0].split('-')
    lower_range = int(split_range[0])
    upper_range = int(split_range[1])
    letter = split_line[1][0]
    password = split_line[2]
    if password.count(letter) >= lower_range and password.count(letter) <= upper_range:
        valid_pass_count += 1

print(valid_pass_count)

# Part 2
new_valid_pass_count = 0

for line in myinput:
    split_line = line.split()
    split_range = split_line[0].split('-')
    pos1 = int(split_range[0]) - 1
    pos2 = int(split_range[1]) - 1
    letter = split_line[1][0]
    password = split_line[2]
    if password[pos1] != password[pos2]:
        if password[pos1] == letter or password[pos2] == letter:
            new_valid_pass_count += 1
print(new_valid_pass_count)