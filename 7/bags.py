f = open("./7/data.txt", "r")

all_rules = f.read().split("\n")

target_color = "shiny gold"

count = 0
def find_color(rules, target):
    for rule in rules:
        if target in rule and rule[:len(target)] != target:
            global count
            count += 1
            new_target = rule.split(" ")[0] + " " + rule.split(" ")[1]
            all_rules.remove(rule)
            find_color(all_rules, new_target)

find_color(all_rules, target_color)
print(count)
