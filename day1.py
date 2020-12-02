myinput = []
with open('input1.txt') as f:
    myinput = f.read().splitlines()

#Part 1
for i in myinput:
    diff = 2020-int(i)            
    if str(diff) in myinput:
        print(diff * int(i))

#Part 2
for i in range(len(myinput)):
    for j in range(i + 1, len(myinput)):
        for k in range(j+1, len(myinput)):
            if int(myinput[i]) + int(myinput[j]) + int(myinput[k]) == 2020:
                print(int(myinput[i]) * int(myinput[j]) * int(myinput[k]))