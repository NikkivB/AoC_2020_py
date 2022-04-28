file = open('../inputs/day5.txt', 'r')
gotten_input = file.read().split('\n')
file.close()

#################################################################
# part 1
highest_value = 0
length = len(gotten_input[1]) - 3
total_length = len(gotten_input[1])

for seat in gotten_input:
    bottom_value = 0
    top_value = 127
    top_row = 8
    bottom_row = 0

    for a in range(0, length):
        if seat[a] == 'F':
            temp_value = top_value - bottom_value
            top_value = top_value - round(temp_value / 2)
            if a == length - 1:
                row = top_value
        elif seat[a] == 'B':
            temp_value = top_value - bottom_value
            bottom_value = top_value - round(temp_value / 2)
            if a == length - 1:
                row = bottom_value

    for b in range(length, total_length):
        if seat[b] == 'R':
            temp_value = top_row - bottom_row
            bottom_row = top_row - round(temp_value / 2)
            if b == total_length - 1:
                column = bottom_row
        elif seat[b] == 'L':
            temp_value = top_row - bottom_row
            top_row = top_row - round(temp_value / 2)
            if b == total_length - 1:
                column = bottom_row

    product = row * 8 + column

    if product > highest_value:
        highest_value = product

print('part 1: ', highest_value)

#################################################################
# part 2
highest_value = 0
length = len(gotten_input[1]) - 3
total_length = len(gotten_input[1])
seat_ids = []

for seat in gotten_input:
    bottom_value = 0
    top_value = 127
    top_row = 8
    bottom_row = 0

    for a in range(0, length):
        if seat[a] == 'F':
            temp_value = top_value - bottom_value
            top_value = top_value - round(temp_value / 2)
            if a == length - 1:
                row = top_value
        elif seat[a] == 'B':
            temp_value = top_value - bottom_value
            bottom_value = top_value - round(temp_value / 2)
            if a == length - 1:
                row = bottom_value

    for b in range(length, total_length):
        if seat[b] == 'R':
            temp_value = top_row - bottom_row
            bottom_row = top_row - round(temp_value / 2)
            if b == total_length - 1:
                column = bottom_row
        elif seat[b] == 'L':
            temp_value = top_row - bottom_row
            top_row = top_row - round(temp_value / 2)
            if b == total_length - 1:
                column = bottom_row

    product = row * 8 + column
    seat_ids.append(product)

seat_ids.sort()

for i in range(0, len(seat_ids) - 1):
    if 5 < i < len(seat_ids) - 6:
        temp = seat_ids.count(seat_ids[i])
        if temp == 1:
            print('part 2: ', seat_ids[i])
            break
