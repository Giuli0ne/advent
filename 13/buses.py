import math
f = open("./13/data.txt", "r")

all_lines = f.read().split("\n")

arrival = int(all_lines[0])

buses = [int(el) for el in all_lines[1].split(",") if el != "x" ]

def min_bus(arriv, bus):
    count = 1
    while(count * bus < arriv):
        count += 1
    return count * bus

def min_bus2(arriv,bus):
    return math.ceil(arriv/bus) * bus


print(arrival)
#print([(min_bus(arrival, el), el) for el in buses])
print([(min_bus2(arrival, el), el) for el in buses])
minimum = min([(min_bus2(arrival, el), el) for el in buses], key = lambda t: t[0] - arrival)
print(minimum)
print((minimum[0] - arrival) * minimum[1])

temp = [int(el) if el != "x" else 0 for el in all_lines[1].split(",")]
all_buses = [[el, temp.index(el)] for el in buses]

print(all_buses)

def bus_condition(number, ab):
    for el in ab:
        if (number + el[1]) % el[0] != 0:
            return False
    return True

for el in all_buses:
    while el[1] - el[0] >=0:
        el[1] -= el[0]
print(all_buses)

all_buses_revised = []
for el in all_buses:
    if el[1] not in [el1[1] for el1 in all_buses_revised]:
        all_buses_revised.append(el)
    else:
        el_temp = next(el1 for el1 in all_buses_revised if el[1]==el1[1])
        all_buses_revised.remove(el_temp)
        el_temp = [el_temp[0] * el[0], el_temp[1]]
        all_buses_revised.append(el_temp)

print(all_buses_revised)



all_buses_revised.sort(key = lambda t: t[0], reverse = True)
print(all_buses_revised)
condition = False
count = -all_buses_revised[0][1]
while(condition == False):
    count += all_buses_revised[0][0]
    condition = bus_condition(count, all_buses_revised)

print(count)
