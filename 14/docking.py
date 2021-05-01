f = open("./14/data.txt", "r")
all_lines = f.read().split("\n")

elements = []
for line in all_lines:
    if line[:4] == "mask":
        temp = line.split(" = ")
        elements.append((temp[0], temp[1]))
    else:
        temp = line.split(" = ")
        elements.append((int(temp[0].replace("mem[","").replace("]","")), (bin(int(temp[1]))[2:]).rjust(36, '0')))

def result(value, mask):
    res = ""
    for i in range(len(value)):
        res += value[i] if mask[i] == "X" else mask[i]
    return res

indexes = [i[0] for i in elements if i[0] != "mask"]
maxIndex = max(indexes)
mem = {}
activeMask = ""
for el in elements:
    if el[0] == "mask":
        activeMask = el[1]
    else:
        mem[el[0]] = result(el[1], activeMask)

mem = [int(i,2) for i in mem.values()]
print(sum(mem))

def decodeLocations(value):
    resBin = []
    for ch in value:
        if ch != "X":
            if len(resBin)==0:
                resBin.append(ch)
            else:
                resBin = [el + ch for el in resBin]
        else:
            if len(resBin)==0:
                resBin.append("0")
                resBin.append("1")
            else:
                resBinCopy = resBin.copy()
                resBin = [el + "0" for el in resBin]
                resBinCopy = [el + "1" for el in resBinCopy]
                resBin += resBinCopy
    return [int(i,2) for i in resBin]
    


def findLocations(value, mask):
    mask = mask.rjust(36, '0')
    res = []
    valueBin = (bin(value)[2:]).rjust(36, '0')
    decoded = ""
    for i in range(len(valueBin)):
        decoded += valueBin[i] if mask[i] == "0" else mask[i]
    return decodeLocations(decoded)

mem = {}
activeMask = ""
for el in elements:
    if el[0] == "mask":
        activeMask = el[1]
    else:
        locations = findLocations(el[0], activeMask)
        for loc in locations:
            mem[loc] = el[1]

mem = [int(i,2) for i in mem.values()]
print(sum(mem))


