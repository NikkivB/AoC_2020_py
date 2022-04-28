def get_input():
    file = open("../inputs/day9.txt", "r")
    data = file.read().split("\n")
    file.close()
    return data


def is_valid(input, index, value, preamble):
    for num in range(index-preamble, index):
        for num2 in range(index-preamble, index):
            if int(input[num]) + int(input[num2]) == int(value):
                return True
                break
    return False


def part1(input, preamble):
    for i in range(preamble, len(input)):
        if not is_valid(input, i, int(input[i]), preamble):
            return input[i]


def part2(input, value):
    for a in range(len(input)):
        values = []
        values.append(int(input[a]))
        for b in range(a+1, len(input)):
            values.append(int(input[b]))
            if sum(values) == int(value):
                return values
            if sum(values) >= int(value):
                break


gotten_input = get_input()
part1_answer = part1(gotten_input, 25)
part2_answer = part2(gotten_input, part1_answer)

print('part 1', part1_answer)
print('part 2', max(part2_answer) + min(part2_answer))
