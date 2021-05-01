start = [6,3,15,13,1,0]

def findDifference(list):
    last = list[-1]
    rest = list[:-1]
    rest.reverse()
    if last in rest:
        return rest.index(last) + 1
    else:
        return 0

while len(start) < 2020:
    start.append(findDifference(start))

print(start[-1])


start = {6:1, 3:2, 15:3, 13:4, 1:5, 0:6}
lastSeen = {}
key = 0
for i in range(7,30000001):
    key = start[key] - lastSeen[key] if key in lastSeen else 0
    if key in start:
        lastSeen[key] = start[key]
    start[key] = i



print(list(start.keys())[list(start.values()).index(30000000)]) 
