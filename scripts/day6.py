file = open('../inputs/day6.txt', 'r')
gotten_input = file.read().split('\n\n')
file.close()

#################################################################
# part 1
filtered_input = [string.replace('\n', '') for string in gotten_input]
filtered_input = [string.replace(' ', '') for string in filtered_input]
answers = ["".join(set(string)) for string in filtered_input]
amount_of_answers = 0

for a in answers:
    amount_of_answers += len(a)

print('part 1:', amount_of_answers)

#################################################################
# part 2
filtered_input = [string.replace(' ', '') for string in gotten_input]
answers = ["".join(set(string)) for string in filtered_input]
groups = []

temp = 0
groups.append([])
for a in answers:
    if a == '':
        temp += 1
        groups.append([])
    else:
        groups[temp].append(a)

amount = 0
total_amount = 0

for group in groups:
    group_amount = 0
    first_person = group[0]

    for letter in first_person:
        amount = 0

        for person in group:
            if letter in person:
                amount += 1

        if amount == len(group):
            group_amount += 1

    total_amount += group_amount

print('part 2:', total_amount)
