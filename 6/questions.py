f = open("./6/data.txt", "r")

datagroups = f.read().split("\n\n")

count = 0
for group in datagroups:
    no_new_line = group.replace("\n", "")
    no_doubles = []
    for char in list(no_new_line):
        if char not in no_doubles:
            no_doubles.append(char)
    count += len(no_doubles)

print(count)

def contains(str, ch):
    for char in list(str):
        if char == ch:
            return True
    return False

def all_contains(list_, ch):
    for string in list_:
        if not contains(string, ch):
            return False
    return True

count = 0
for group in datagroups:
    persons = group.split("\n")
    if len(persons) == 1:
        count += len(persons[0])
        continue
    pivot = persons[0]
    others = persons[1:]
    for char in list(pivot):
        if all_contains(others, char):
            count += 1

print(count)
