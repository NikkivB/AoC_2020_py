import json


def get_input():
    file = open("../inputs/day10.txt", "r")
    data = file.read().split("\n")
    file.close()
    return data


def part1(gotten_input):
    sorted_list = sorted(gotten_input, key=int)
    sorted_list.insert(0, 0)
    sorted_list.append(int(sorted_list[-1]) + 3)

    inputs = {
        1: 0,
        2: 0,
        3: 0
    }
    for a in range(1, len(sorted_list)):
        pindakaas = int(sorted_list[a]) - int(sorted_list[a - 1])
        inputs[pindakaas] += 1

    return inputs


def part2(gotten_input):
    sorted_list = sorted(gotten_input, key=int)
    sorted_list.insert(0, 0)
    sorted_list.append(int(sorted_list[-1]) + 3)

    scores = {}
    sorted_list.reverse()
    for key, number in enumerate(sorted_list):
        next_numbers = sorted_list[:key][-3:]

        if not next_numbers:
            scores[number] = 1
            continue

        scores[number] = 0
        for next_number in next_numbers:
            is_valid = int(next_number) - int(number) <= 3
            if is_valid:
                scores[number] += scores[next_number]

    return scores[0]


################################
gotten_input = get_input()
part1 = part1(gotten_input)

print("part 1:", part1[1] * (part1[3]))
print("part 2:", part2(gotten_input))

