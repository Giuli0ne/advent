import math
f = open("./12/data.txt", "r")

all_lines = f.read().split("\n")

class Instruction:
    def __init__(self, dir, val):
        super().__init__()
        if dir == "N":
            self.direction = 0
        elif dir == "E":
            self.direction = 1
        elif dir == "S":
            self.direction = 2
        elif dir == "W":
            self.direction = 3
        elif dir == "F":
            self.direction = 4
        elif dir == "R":
            self.direction = 5
        elif dir == "L":
            self.direction = 6
        self.value = val


countNS = 0
countWE = 0
actual_direction = 1

for el in all_lines:
    instr = Instruction(el[0], int(el[1:]))
    dir = instr.direction
    if instr.direction == 4:
        dir = actual_direction
    if dir == 0:
        countNS += instr.value
    elif dir == 2:
        countNS -= instr.value
    elif dir == 1:
        countWE += instr.value
    elif dir == 3:
        countWE -= instr.value
    elif dir == 5:
        actual_direction = (actual_direction + (instr.value / 90)) % 4
    elif dir == 6:
        actual_direction = (actual_direction - (instr.value / 90)) % 4
    #print(el, countNS, countWE)

print(abs(countWE) + abs(countNS))



actual_position = [0,0]
actual_waypoint = [10, 1]

for el in all_lines:
    instr = Instruction(el[0], int(el[1:]))
    dir = instr.direction
    if dir == 4:
        actual_position[0] += actual_waypoint[0] * instr.value
        actual_position[1] += actual_waypoint[1] * instr.value
    elif dir == 0:
        actual_waypoint[1] += instr.value
    elif dir == 2:
        actual_waypoint[1] -= instr.value
    elif dir == 1:
        actual_waypoint[0] += instr.value
    elif dir == 3:
        actual_waypoint[0] -= instr.value
    else:
        if dir == 5 :
            sign = 1
        else:
            sign = -1
        angle = sign * instr.value * math.pi / 180
        cosine = [i *math.cos(angle) for i in actual_waypoint]
        sine = [actual_waypoint[1] * math.sin(angle), - actual_waypoint[0] * math.sin(angle) ]
        actual_waypoint = [round(i + j, 0) for i, j in zip(cosine, sine)]
    print(el, actual_position, actual_waypoint)
    
print(abs(actual_position[0])+ abs(actual_position[1]))