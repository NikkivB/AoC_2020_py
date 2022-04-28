file = open('../inputs/day3.txt', 'r')
gotten_input = file.read().split('\n')
file.close()

#################################################################
# part 1
x = 0
trees = 0

for line in gotten_input:
    while len(line) < x:
        line = line + line

    temp = line[x]
    x += 3
    if temp == '#':
        trees += 1

print("part 1:", trees)

#################################################################
# part 2

x = 0
y = 0
amount1 = 0
amount2 = 0
amount3 = 0
amount4 = 0
amount5 = 0

for line in gotten_input:

    while len(line) <= x:
        line = line + line

    temp = line[x]  # error
    x += 1
    if temp == '#':
        amount1 += 1

x = 0
for line in gotten_input:
    while len(line) < x:
        line = line + line

    temp = line[x]
    x += 3
    if temp == '#':
        amount2 += 1

x = 0
for line in gotten_input:
    while len(line) < x:
        line = line + line

    temp = line[x]
    x += 5
    if temp == '#':
        amount3 += 1

x = 0
for line in gotten_input:
    while len(line) < x:
        line = line + line

    temp = line[x]
    x += 7
    if temp == '#':
        amount4 += 1

x = 0
for y in range(0, len(gotten_input), 2):
    line = gotten_input[y]

    while len(line) <= x:
        line = line + line

    temp = line[x]
    x += 1
    if temp == '#':
        amount5 += 1

product = amount1 * amount2 * amount3 * amount4 * amount5

print("part 2:", product)
