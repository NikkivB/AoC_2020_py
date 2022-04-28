import json

file = open("../inputs/day7.txt", "r")
bags_list = file.read().split("\n")
file.close()

#################################################################
# part 1
amount_of_bags = 0
bags = {}
bag_names = []
shiny_bags = []

for bag in bags_list:
    bag_name = bag.split(" bags contain ")[0]
    bag_names.append(bag_name)

    bag_contents = bag.split(" bags contain ")[1]
    if bag_contents == "no other bags.":
        bags[bag_name] = []
    else:
        contents = bag_contents.split(", ")
        current_contents = []
        for content in contents:
            amount = int(content.split(" ")[0])
            name = ' '.join(content.split(" ")[1:3])

            current_contents.append({
                'amount': amount,
                'name': name
            })
        bags[bag_name] = current_contents

amt_of_bags = len(bags)

for i in range(len(bag_names)):
    if bag_names[i] == "shiny gold":
        shiny_bags.append(bag_names[i])
        continue
    for a in range(0, 10):
        for bag in bags[bag_names[i]]:
            if bag['name'] == "shiny gold":
                shiny_bags.append(bag_names[i])
                break

for b in range(0, 10):
    for name in bag_names:
        for bag in bags[name]:
            if bag['name'] in shiny_bags:
                shiny_bags.append(name)

given_bags = []
for name in bag_names:
    temp = 0
    if name in shiny_bags:
        temp += 1
    else:
        for bag in bags[name]:
            if bag['name'] in shiny_bags:
                temp += 1
                break
    if temp > 0:
        given_bags.append(name)
        amount_of_bags += 1

print("part 1:", amount_of_bags-1)

#################################################################
# part 1

print("part 2: X")
