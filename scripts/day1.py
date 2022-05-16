file = open('../inputs/day1.txt', 'r')
gotten_input = file.read().split('\n')
file.close()

#################################################################
# part 1

answer = [int(a) * int(b) for a in gotten_input for b in gotten_input if int(a) + int(b) == 2020]
print("part 1: ", answer[0])

#################################################################
# part 2

answer = [int(a) * int(b) * int(c) for a in gotten_input for b in gotten_input for c in gotten_input if
          int(a) + int(b) + int(c) == 2020]
print("part 2: ", answer[0])

# AAAAAAAAAAAAAAAAAAAAAAAAAAA
