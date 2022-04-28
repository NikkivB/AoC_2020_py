# functions
import json


def get_input():
    file = open("../inputs/day8.txt", "r")
    gotten_input = file.read().split("\n")
    file.close()

    return gotten_input


def create_list(gotten_input):
    instructions = []
    for i in gotten_input:
        instruction = {}

        temporary_list = i.split(" ")
        instruction['code'] = temporary_list[0]
        instruction['parameters'] = int(temporary_list[1])
        instructions.append(instruction)

    return instructions


def run_set(instructions):
    gotten_positions = []
    accumulator = 0
    position = 0

    for instruction in instructions[:-1]:
        if position >= len(instructions)-1:
            return accumulator, False

        current_instruction = instructions[position]
        if position not in gotten_positions:
            gotten_positions.append(position)

            match current_instruction["code"]:
                case "acc":
                    accumulator += current_instruction["parameters"]
                    position += 1
                case "jmp":
                    position += current_instruction["parameters"]
                case "nop":
                    position += 1
        else:
            return accumulator, True
    return accumulator, False


def replace_item(instruction):
    match instruction["code"]:
        case "nop":
            instruction["code"] = "jmp"
        case "jmp":
            instruction["code"] = "nop"


###############################################################################
# run code
gotten_input = get_input()
instructions = create_list(gotten_input)
part1_answer = run_set(instructions)[0]
part2_answer = "not yet"

for instruction in instructions:
    replace_item(instruction)
    temp_answer = run_set(instructions)
    if not temp_answer[1]:
        part2_answer = temp_answer[0]
    else:
        replace_item(instruction)

print("wanted: 1749")
print(part1_answer)
print("----------------\nwanted: 515")
print(part2_answer)
