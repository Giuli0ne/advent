f = open("./7/data.txt", "r")

all_rules = f.read().split("\n")

target_color = "shiny gold"

count = 0
good_rules = []
def find_color(rules, target):
    for rule in rules:
        if target in rule and rule[:len(target)] != target:
            #global count
            #count += 1
            if rule not in good_rules:
                good_rules.append(rule)
            new_target = rule.split(" ")[0] + " " + rule.split(" ")[1]
            #all_rules.remove(rule)
            find_color(all_rules, new_target)

find_color(all_rules, target_color)
print(len(good_rules))

rules_dict = {}
for rule in all_rules:
    new_key = rule.split(" ")[0] + " " + rule.split(" ")[1]
    content = rule.split(" bags contain ")[1]
    single_content = content.split(", ")
    content_dict = {el.split(" ")[1] + " " + el.split(" ")[2] : el.split(" ")[0] for el in single_content}
    rules_dict[new_key] = content_dict

#print(rules_dict["posh salmon"])

def count_bags(target):
    if "other bags." in rules_dict[target]:
        return 0
    else:
        total = 0
        for k in rules_dict[target].keys():
            total += (count_bags(k) + 1) * int(rules_dict[target][k])
        return total

print(count_bags("shiny gold"))

