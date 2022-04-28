file = open('../inputs/day4.txt', 'r')
gotten_input = file.read().split('\n\n')
file.close()

filtered_input = [string.replace("\n", " ") for string in gotten_input]
passports = [string.split() for string in filtered_input]
requirements = ['hcl', 'iyr', 'eyr', 'ecl', 'pid', 'byr', 'hgt']
eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
#################################################################
# part 1
amount_valid = 0

for passport in passports:
    temp = [string[0:3] for string in passport]
    if set(requirements).issubset(temp):
        amount_valid += 1

print('part 1:', amount_valid)

#################################################################
# part 2
amount_valid = 0

for passport in passports:

    temp = [string[0:3] for string in passport]
    value = [string[4:len(string)] for string in passport]

    if set(requirements).issubset(temp):
        hcl = value[temp.index('hcl')]
        iyr = value[temp.index('iyr')]
        eyr = value[temp.index('eyr')]
        ecl = value[temp.index('ecl')]
        pid = value[temp.index('pid')]
        byr = value[temp.index('byr')]
        hgt = value[temp.index('hgt')]

        hgt_num = hgt[0:len(hgt) - 2]
        hgt_unit = hgt[len(hgt) - 2:len(hgt)]

        if '#' in hcl and len(hcl) == 7:
            if len(iyr) == 4 and 2010 <= int(iyr) <= 2020:
                if len(eyr) == 4 and 2020 <= int(eyr) <= 2030:
                    if ecl in eye_colors:
                        if len(pid) == 9:
                            if len(byr) == 4 and 1920 <= int(byr) <= 2002:
                                if hgt_unit == 'cm' and 150 <= int(hgt_num) <= 193:
                                    amount_valid += 1
                                elif hgt_unit == 'in' and 59 <= int(hgt_num) <= 76:
                                    amount_valid += 1

print("part 2:", amount_valid)
