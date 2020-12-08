import math
myinput = []
with open('input5.txt') as f:
    myinput = f.read().splitlines()

def findSeatID(line) -> int:
    fb_min = 0
    fb_max = 127
    lr_min = 0
    lr_max = 7
    row = 0
    col = 0
    for char in line:
        if char == 'F':
            dif = fb_max - fb_min
            med = math.ceil(dif/2)
            fb_max = fb_max - med
            if fb_min == fb_max:
                row = fb_min
                # print('FINAL ROW: ', row)
        if char == 'B':
            dif = fb_max - fb_min
            med = math.ceil(dif/2)
            fb_min = fb_min + med
            if fb_min == fb_max:
                row = fb_min
                # print('FINAL ROW: ', row)
        if char == 'R':
            dif = lr_max - lr_min
            med = math.ceil(dif/2)
            lr_min = lr_min + med
            if lr_min == lr_max:
                col = lr_min
                # print('FINAL COL: ', col)
        if char == 'L':
            dif = lr_max - lr_min
            med = math.ceil(dif/2)
            lr_max = lr_max - med
            if lr_min == lr_max:
                col = lr_min
                # print('FINAL COL: ', col)
    final = row * 8 + col
    return final

max_seatid = 0
min_seatid = 0
seats = []
for line in myinput:
    seats.append(findSeatID(line))
    if findSeatID(line) > max_seatid:
        max_seatid = findSeatID(line)

seats.sort()
range_list = [x for x in range(seats[0],seats[len(seats)-1])]
print(set(range_list) - set(seats))
print(max_seatid)