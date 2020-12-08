import string
myinput = []
with open('input6.txt') as f:
    myinput = f.read().split('\n\n')

# Part 1
sum_yes = 0
for group in myinput:
    yes = []
    for person in group:
        answers = person.strip()
        for answer in answers:
            yes.append(answer)
    sum_yes += len(set(yes))
print(sum_yes)

# Part 2
alphabet = list(string.ascii_lowercase)
sum_yes = 0
for group in myinput:
    group_array = group.split('\n')
    for letter in alphabet:
        if all(letter in l for l in group_array):
            sum_yes += 1
print(sum_yes)