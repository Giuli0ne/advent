f = open("./11/data.txt", "r")

all_lines = f.read().split("\n")

seats = []

for line in all_lines:
    seats.append(list(line))



def square (seats, row, column):
    if row == 0 and column == 0:
        return [seats[row][column +1], seats[row +1][column], seats[row +1][column +1]]
    elif row == len(all_lines) -1 and column == len(seats[0]) -1:
        return [seats[row -1][column -1], seats[row -1][column], seats[row][column -1]]
    elif row == 0 and column == len(seats[0]) -1:
        return [seats[row][column -1], seats[row +1][column -1], seats[row +1][column]]
    elif row == len(all_lines)  -1 and column == 0:
        return [seats[row -1][column], seats[row -1][column +1], seats[row][column +1]]
    elif row == 0:
        return [seats[row][column -1],seats[row][column +1],
            seats[row +1][column -1],seats[row +1][column],seats[row +1][column +1]]
    elif row == len(all_lines) -1:
        return [seats[row -1][column -1],seats[row -1][column],seats[row -1][column +1],
            seats[row][column -1],seats[row][column +1]]
    elif column == 0:
        return [seats[row -1][column],seats[row -1][column +1],
            seats[row][column +1], seats[row +1][column],seats[row +1][column +1]]
    elif column == len(seats[0]) -1:
        return [seats[row -1][column -1],seats[row -1][column],
            seats[row][column -1], seats[row +1][column -1],seats[row +1][column]]
    else:
        return [seats[row -1][column -1],seats[row -1][column],seats[row -1][column +1],
            seats[row][column -1],seats[row][column +1],
            seats[row +1][column -1],seats[row +1][column],seats[row +1][column +1]]

     
def step(seats):
    result = [[0 for x in range(len(seats[0]))] for y in range(len(all_lines))] 
    for row in range(len(all_lines)):
        for column in range(len(seats[0])):
            if seats[row][column] == ".":
                result[row][column] = "."
            elif seats[row][column] == "#" and square(seats, row, column).count("#")>=4:
                result[row][column] = "L"
            elif seats[row][column] == "L" and square(seats, row, column).count("#")==0:
                result[row][column] = "#"
            else:
                result[row][column] = seats[row][column]
    return result

def equal(s1, s2):
    for row in range(len(all_lines)):
        for column in range(len(seats[0])):
            if s1[row][column] != s2[row][column]:
                return False
    return True

# temp = seats
# oldtemp = seats
# count = 0
# while True:
#     t2 = step(temp)
#     count += 1
#     if equal(temp, t2):
#         print("OK "+ str(count))
#         break
#     if equal(oldtemp, t2):
#         print("BAD " + str(count))
#         break
#     oldtemp = temp
#     temp = t2

# num_people = 0
# for s in temp:
#     num_people += s.count("#")

# print(num_people)

def see(seats, row, column, dir1, dir2):
    rowtemp = row
    coltemp = column
    if dir1 == 0 and dir2 == 0:
        return False

    rowtemp += dir1
    coltemp += dir2
    while rowtemp >= 0 and rowtemp <= len(all_lines) -1 and coltemp >= 0 and coltemp <= len(seats[0]) - 1:
        if seats[rowtemp][coltemp] == "#":
            return True
        elif seats[rowtemp][coltemp] == "L":
            return False
        rowtemp += dir1
        coltemp += dir2
    return False

directions = [-1, 0, 1]

def see_all(seats, row, column):
    cou = 0
    for d1 in directions:
        for d2 in directions:
            if see(seats, row, column, d1, d2):
                cou +=1
    return cou

def step2(seats):
    result = [[0 for x in range(len(seats[0]))] for y in range(len(all_lines))] 
    for row in range(len(all_lines)):
        for column in range(len(seats[0])):
            if seats[row][column] == "#" and see_all(seats, row, column)>=5:
                result[row][column] = "L"
            elif seats[row][column] == "L" and see_all(seats, row, column)==0:
                result[row][column] = "#"
            else:
                result[row][column] = seats[row][column]
    return result

# f = open("./11/testdata.txt", "r")

# all_lines = f.read().split("\n")


seats = []

for line in all_lines:
    seats.append(list(line))


temp = seats
oldtemp = seats
count = 0
while True:
    t2 = step2(temp)
    count += 1
    if equal(temp, t2):
        print("OK "+ str(count))
        break
    if equal(oldtemp, t2):
        print("BAD " + str(count))
        break
    oldtemp = temp
    temp = t2

num_people = 0
for s in temp:
    num_people += s.count("#")
print(num_people)
