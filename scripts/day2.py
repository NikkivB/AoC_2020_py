file = open('../inputs/day2.txt', 'r')
gotten_input = file.read().split('\n')
file.close()

#################################################################
# part 1
amount = 0

for a in gotten_input:
    given_range = a.split(" ")[0].split("-")
    start = int(given_range[0])
    end = int(given_range[1])
    value = a.split(" ")[1][:-1]
    password = a.split(" ")[2]

    if password.count(value) in range(start, end + 1):
        amount += 1

print("part 1:", amount)

#################################################################
# part 2
amount = 0

for a in gotten_input:
    pos1 = int(a.split(" ")[0].split("-")[0])
    pos2 = int(a.split(" ")[0].split("-")[1])
    value = a.split(" ")[1][:-1]
    password = a.split(" ")[2]

    value_pos1 = password[pos1 - 1]
    value_pos2 = password[pos2 - 1]

    if (value in value_pos1 and value not in value_pos2) or (value not in value_pos1 and value in value_pos2):
        amount += 1

print("part 2:", amount)
