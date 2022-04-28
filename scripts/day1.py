file = open('../inputs/day1.txt', 'r')
gotten_input = file.read().split('\n')
file.close()

#################################################################
# part 1
answer = ''

for a in gotten_input:
    for b in gotten_input:
        c = int(a) + int(b)
        if c == 2020:
            answer = int(a) * int(b)
            break
        if answer != '':
            break

print("part 1: ", answer)

#################################################################
# part 2
answer = ""

for a in gotten_input:
    for b in gotten_input:
        for c in gotten_input:
            d = int(a) + int(b) + int(c)
            if d == 2020:
                answer = int(a) * int(b) * int(c)
                break
        if answer != '':
            break
    if answer != '':
        break
print("part 2: ", answer)
