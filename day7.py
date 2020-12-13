import string
myinput = []
with open('input7.txt') as f:
    myinput = f.read().split('\n')

    # find the parent bags that contain a shiny gold bag
    # add the parent bags to a set
    # find the parent to those parent bags
    # add them to the set of bags that could contain a shiny gold bag

bags = []
def findBags(bagColor):
    newBags = []
    for line in myinput:
        if bagColor in line and line[0:len(bagColor)] != bagColor:
                bags.append(line[0:line.find(' bags')])
                newBags.append(line[0:line.find(' bags')])
    for newBag in newBags:
        findBags(newBag)

findBags('shiny gold')
print(len(set(bags))) # part 1

# find how many bags are in a shiny gold bag
# add this number to bag sum
# find how many bags are inside the colors of a shiny gold bag
# add this number to bag sum

# def findNumberOfBags(bagColor, n):
#     newBags = {}
#     print('start n', n, 'start color', bagColor)
#     for line in myinput:
#         if line[0:len(bagColor)] == bagColor:
#             contentsOfBag = line[line.find('contain ') + 8 : len(line) - 1].split(', ')
#             if 'no other bags' in contentsOfBag:
#                 return 0
#             numBags = sum([int(i[0]) for i in contentsOfBag])
#             for bag in contentsOfBag:
#                 newBags[bag[bag.find(' ') + 1 : bag.find(' bag')]] = int(bag[0 : bag.find(' ')])
#             for newBag in newBags:
#                 print('n ', n, 'numBags', numBags, newBag, newBags[newBag])
#                 print('calc', newBags[newBag] * n)
#                 findNumberOfBags(newBag, n)
# print('this', findNumberOfBags('shiny gold', 1))

summation = 0
previousBagSize = 0

def findNumberOfBags(bagColor):
    global summation
    global previousBagSize
    newBags = {}
    # print('previous bag size,', previousBagSize)
    for line in myinput:
        if line[0:len(bagColor)] == bagColor:
            contentsOfBag = line[line.find('contain ') + 8 : len(line) - 1].split(', ')
            if 'no other bags' in contentsOfBag:
                print('no other bags in ', line)
                previousBagSize = 0
                return
            for bag in contentsOfBag:
                newBags[bag[bag.find(' ') + 1 : bag.find(' bag')]] = int(bag[0 : bag.find(' ')])
            for newBag in newBags:
                print('previous bag size', previousBagSize, 'new bag size', newBags[newBag])
                previousBagSize = newBags[newBag]
                findNumberOfBags(newBag)
    print(previousBagSize, bagColor)

# findNumberOfBags('shiny gold')

import re
from collections import defaultdict

# bags = defaultdict(dict)
# for l in myinput:
#     bag = re.match(r'(.*) bags contain', l).groups()[0]
#     print('a bag is:', bag)
#     for count, b in re.findall(r'(\d+) (\w+ \w+) bag', l):
#         bags[bag][b] = int(count)
#         print('b is:', b, int(count))
# print(bags)

## Part 2 is not my solution, I had to look for help :(
bags = defaultdict(dict)
for line in myinput:
    bag = line[0:line.find(' bags contain')]
    contentsOfBag = line[line.find('contain ') + 8 : len(line) - 1].split(', ')
    for currBag in contentsOfBag:
        bagName = currBag[currBag.find(' ') + 1 :currBag.find(' bag')]
        if 'no other bags' in currBag:
            break
        else:
            bags[bag][bagName] = int(currBag[0:currBag.find(' ')])

print(bags)
def part2():
    def search(bag):
        count = 1
        for s in bags[bag]:
            multiplier = bags[bag][s]
            count += multiplier * search(s)
        return count
    return search('shiny gold') - 1

print(part2())