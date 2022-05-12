import json


def get_input():
    file = open("../inputs/day11.txt", "r")
    data = file.read().split("\n")
    file.close()
    return data

def part1(get_input):
    for seat in get_input:
        empty_seats = seat.count("L")
        taken_seats = seat.count("#")
        print(seat, empty_seats, taken_seats)
        for single in seat:
            if single == "#" and taken_seats >= 4:
                single = "L"
            elif single == "L" and empty_seats >= 1:
                single = "#"

                
            print(single)


#################################################################
gotten_input = get_input()
part1(gotten_input)

