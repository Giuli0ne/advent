f = open("./2/data.txt", "r")

data = f.read()

lines = data.split("\n")
i=0

for line in lines:
    elements = line.split(":")
    rule = elements[0].split(" ")
    numbers = rule[0].split("-")
    letter = rule[1]
    pwd = elements[1]
    if pwd.count(letter) <= int(numbers[1]) and pwd.count(letter)>= int(numbers[0]):
        i += 1

print(i)

i=0
for line in lines:
    elements = line.split(":")
    rule = elements[0].split(" ")
    numbers = rule[0].split("-")
    letter = rule[1]
    pwd = elements[1]
    if bool(pwd[int(numbers[1])] == letter) != bool(pwd[int(numbers[0])] == letter):
        i += 1
print(i)