f = open("./16/data1.txt", "r")
all_lines = f.read().split("\n")

temp = [line.split(": ")[1] for line in all_lines]
temp1 = [line.split(" or ") for line in temp]
intervals = [(int(line[0].split("-")[0]),int(line[0].split("-")[1]),int(line[1].split("-")[0]),int(line[1].split("-")[1])) for line in temp1]
print(intervals[0])

f1 = open("./16/data.txt", "r")
all_lines = f1.read().split("\n")
all_lines = all_lines[1:]

tickets = [[int(v) for v in line.split(",")] for line in all_lines]

def check_interval(value, i):
    return value in range(i[0], i[1] + 1) or value in range(i[2], i[3]+1)

def check_intervals(value):
    for i in intervals:
        if check_interval(value, i):
            return True
    return False

scanning_rate = 0
for ticket in tickets:
    for v in ticket:
        if not check_intervals(v):
            scanning_rate += v

print(scanning_rate)

def valid_ticket(ticket):
    for v in ticket:
        if not check_intervals(v):
            return False
    return True


tickets = [t for t in tickets if valid_ticket(t)]

def good_interval(values):
    good =[]
    for i in range(len(intervals)):
        for v in values:
            if not check_interval(v, intervals[i]):
                break
        else:
            good.append(i)
    return good

        

correspondence = []
for i in range(len(tickets[0])):
    vals = [t[i] for t in tickets]
    correspondence.append((i, good_interval(vals)))

print(correspondence)

clean_correspondence = {}
while len(correspondence)>0:
    for cor in correspondence:
        if len(cor[1]) == 1:
            clean_correspondence[cor[1][0]] = cor[0]
            temp = cor
            break
    correspondence.remove(temp)
    for cor in correspondence:
        cor[1].remove(temp[1][0])

print(clean_correspondence)

f2 = open("./16/data2.txt", "r")
lines = f2.read().split("\n")
line = lines[1]

myticket = [int(v) for v in line.split(",")]

final_result = 1
for i in range(6):
    final_result *= myticket[clean_correspondence[i]]
print(final_result)






